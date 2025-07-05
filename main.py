import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QFrame, QScrollArea,
    QGraphicsDropShadowEffect
)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QColor
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal

from config.prompts import get_prompt
from config.ui_text import UI_TEXT
from config.styles import get_app_stylesheet, get_chat_bubble_style

try:
    from dotenv import load_dotenv
    load_dotenv("config/.env")
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class GeminiWorker(QThread):
    """Worker thread for Gemini API calls to avoid blocking the UI."""
    response_ready = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, message, mode, language, api_key):
        super().__init__()
        self.message = message
        self.mode = mode
        self.language = language
        self.api_key = api_key

    def run(self):
        try:
            if not GEMINI_AVAILABLE:
                self.error_occurred.emit("Gemini API not available. Install google-generativeai package.")
                return

            genai.configure(api_key=self.api_key)
            model = genai.GenerativeModel('gemini-2.0-flash')

            prompt = get_prompt(self.mode, self.language, self.message)

            response = model.generate_content(prompt)
            self.response_ready.emit(response.text)

        except Exception as e:
            self.error_occurred.emit(f"API Error: {str(e)}")


class ModernButton(QPushButton):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0, 0, 0, 50))
        self.shadow.setOffset(0, 2)
        self.setGraphicsEffect(self.shadow)


class ModernChatBubble(QFrame):

    def __init__(self, message, sender, is_user=False, theme="light"):
        super().__init__()
        self.is_user = is_user
        self.theme = theme
        self.setMaximumWidth(600)
        self.setContentsMargins(0, 5, 0, 5)

        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(15, 10, 15, 10)

        sender_label = QLabel(sender)
        sender_label.setObjectName("senderLabel")

        message_label = QLabel()
        message_label.setWordWrap(True)
        message_label.setTextFormat(Qt.TextFormat.RichText)
        message_label.setText(self._format_message(message))
        message_label.setObjectName("messageLabel")

        layout.addWidget(sender_label)
        layout.addWidget(message_label)

        self._apply_bubble_style()

    def _format_message(self, message):
        import re

        message = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', message)
        message = re.sub(r'\*(.*?)\*', r'<i>\1</i>', message)
        message = message.replace('\n', '<br>')

        lines = message.split('<br>')
        formatted_lines = []
        in_list = False

        for line in lines:
            line = line.strip()
            if re.match(r'^\d+\.\s+', line) or line.startswith('•') or line.startswith('-'):
                if not in_list:
                    formatted_lines.append('<ul style="margin: 8px 0; padding-left: 20px;">')
                    in_list = True
                if re.match(r'^\d+\.\s+', line):
                    item_text = re.sub(r'^\d+\.\s+', '', line)
                else:
                    item_text = re.sub(r'^[•\-]\s*', '', line)
                formatted_lines.append(f'<li style="margin: 2px 0; line-height: 1.5;">{item_text}</li>')
            else:
                if in_list:
                    formatted_lines.append('</ul>')
                    in_list = False
                if line:
                    formatted_lines.append(f'<p style="margin: 8px 0; line-height: 1.6;">{line}</p>')

        if in_list:
            formatted_lines.append('</ul>')
        result = ''.join(formatted_lines)

        result = re.sub(r'<p[^>]*>\s*</p>', '', result)
        
        return result

    def _apply_bubble_style(self):
        style = get_chat_bubble_style(self.is_user, self.theme)
        self.setStyleSheet(style)


class HealthBotDemoWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.language = "en"
        self.theme = "dark"


        self.api_key = self._load_api_key()
        self.gemini_worker = None
        self.is_typing = False
        self.chat_history = []
        self._load_custom_fonts()
        self.ui_text = UI_TEXT
        self._configure_window()
        self._create_widgets()
        self._create_layout()
        self._apply_styles()
        self._connect_signals()

        self.update_ui_text()
        self.set_health_query_mode()
        self._show_welcome_message()

    def _load_custom_fonts(self):
        font_path = "assets/Dangrek-Regular.ttf"
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"Warning: Could not load font at '{font_path}'. Using system fonts.")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print(f"Successfully loaded font: '{font_family}'")

    def _load_api_key(self):
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            print("Warning: GEMINI_API_KEY not found or not properly configured.")
            print("Please set a valid API key in your config/.env file or environment variables.")
            if not DOTENV_AVAILABLE:
                print("Consider installing python-dotenv: pip install python-dotenv")
            else:
                print("Make sure you have a valid .env file in the 'config' folder.")
                print("You can copy config/.env.example to config/.env and add your API key.")
            return None
        return api_key

    def _configure_window(self):
        """Set up the main window properties."""
        self.setGeometry(100, 100, 900, 800)
        self.setMinimumSize(600, 500)
        try:
            self.setWindowIcon(QIcon("assets/icon.png"))
        except Exception as e:
            print(f"Icon not found: {e}. Using default icon.")

    def _create_widgets(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.header_frame = QFrame()
        self.header_frame.setMinimumHeight(70)
        self.title_label = QLabel()
        self.language_toggle_button = ModernButton()
        self.theme_toggle_button = ModernButton()
        self.chat_scroll = QScrollArea()
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_widget)
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.chat_layout.setSpacing(12)
        self.chat_layout.setContentsMargins(16, 16, 16, 16)

        self.chat_scroll.setWidget(self.chat_widget)
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.chat_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mode_button_frame = QFrame()
        self.mode_button_frame.setMinimumHeight(60)
        self.mode_label = QLabel()
        self.health_query_button = ModernButton()
        self.health_query_button.setCheckable(True)
        self.symptom_checker_button = ModernButton()
        self.symptom_checker_button.setCheckable(True)
        self.input_frame = QFrame()
        self.input_frame.setMinimumHeight(60)
        self.user_input = QLineEdit()
        self.user_input.setMinimumHeight(40)
        self.send_button = ModernButton()
        self.send_button.setMinimumSize(80, 40)

    def _create_layout(self):
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        header_layout = QHBoxLayout(self.header_frame)
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.language_toggle_button)
        header_layout.addWidget(self.theme_toggle_button)
        header_layout.setContentsMargins(24, 16, 24, 16)
        header_layout.setSpacing(12)
        mode_buttons_layout = QHBoxLayout()
        mode_buttons_layout.addWidget(self.health_query_button)
        mode_buttons_layout.addWidget(self.symptom_checker_button)
        mode_buttons_layout.addStretch()
        mode_buttons_layout.setSpacing(12)

        mode_layout = QVBoxLayout(self.mode_button_frame)
        mode_layout.addWidget(self.mode_label)
        mode_layout.addLayout(mode_buttons_layout)
        mode_layout.setContentsMargins(24, 12, 24, 12)
        input_layout = QHBoxLayout(self.input_frame)
        input_layout.addWidget(self.user_input, 1)
        input_layout.addWidget(self.send_button)
        input_layout.setContentsMargins(24, 12, 24, 12)
        input_layout.setSpacing(12)
        self.main_layout.addWidget(self.header_frame)
        self.main_layout.addWidget(self.chat_scroll, 1)
        self.main_layout.addWidget(self.mode_button_frame)
        self.main_layout.addWidget(self.input_frame)

    def _connect_signals(self):
        self.send_button.clicked.connect(self.send_message)
        self.user_input.returnPressed.connect(self.send_message)
        self.health_query_button.clicked.connect(lambda: self.set_health_query_mode(True))
        self.symptom_checker_button.clicked.connect(lambda: self.set_symptom_checker_mode(True))
        self.language_toggle_button.clicked.connect(self.toggle_language)
        self.theme_toggle_button.clicked.connect(self.toggle_theme)

        if GEMINI_AVAILABLE:
            print("Gemini API integration ready. Make sure to set GEMINI_API_KEY in .env file.")

    def _show_welcome_message(self):
        welcome_bubble = ModernChatBubble(
            self.ui_text[self.language]["welcome_message"],
            self.ui_text[self.language]["bot"],
            False,
            self.theme
        )
        self.chat_layout.addWidget(welcome_bubble)

    def _add_chat_bubble(self, message, sender, is_user, save_to_history=True):
        if save_to_history and sender != "✍️ AI is thinking..." and sender != "✍️ AI កំពុងគិត...":
            self.chat_history.append((message, sender, is_user))

        bubble = ModernChatBubble(message, sender, is_user, self.theme)
        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)

        if is_user:
            container_layout.addStretch()
            container_layout.addWidget(bubble)
        else:
            container_layout.addWidget(bubble)
            container_layout.addStretch()

        self.chat_layout.addWidget(container)
        QTimer.singleShot(50, lambda: self.chat_scroll.verticalScrollBar().setValue(
            self.chat_scroll.verticalScrollBar().maximum()
        ))

    def _post_system_message(self, message):
        system_label = QLabel(message)
        system_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        system_label.setObjectName("systemMessage")

        container = QWidget()
        container_layout = QHBoxLayout(container)
        container_layout.addWidget(system_label)
        container_layout.setContentsMargins(20, 10, 20, 10)

        self.chat_layout.addWidget(container)

    def update_ui_text(self):
        """Updates all UI text elements based on the current language."""
        lang = self.language
        self.setWindowTitle(self.ui_text[lang]["window_title"])
        self.title_label.setText(self.ui_text[lang]["window_title"])
        self.health_query_button.setText(self.ui_text[lang]["health_query_btn"])
        self.symptom_checker_button.setText(self.ui_text[lang]["symptom_checker_btn"])
        self.language_toggle_button.setText(self.ui_text[lang]["language_btn"])
        self.theme_toggle_button.setText(self.ui_text[lang]["theme_btn"])
        self.user_input.setPlaceholderText(self.ui_text[lang]["input_placeholder"])
        self.send_button.setText(self.ui_text[lang]["send_btn"])

        if self.health_query_button.isChecked():
            self.mode_label.setText(self.ui_text[lang]["mode_label_health"])
        else:
            self.mode_label.setText(self.ui_text[lang]["mode_label_symptom"])

    def toggle_language(self):
        """Toggles the language and updates the UI."""
        self.language = "km" if self.language == "en" else "en"
        self.update_ui_text()
        self._post_system_message(
            self.ui_text[self.language]["switched_to_km" if self.language == "km" else "switched_to_en"])

    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"
        UI_TEXT["en"]["theme_btn"] = "☀️" if self.theme == "dark" else "🌙"
        UI_TEXT["km"]["theme_btn"] = "☀️" if self.theme == "dark" else "🌙"
        
        self.update_ui_text()
        self._apply_styles()
        self._refresh_chat_bubbles()

    def _refresh_chat_bubbles(self):
        for i in reversed(range(self.chat_layout.count())):
            self.chat_layout.itemAt(i).widget().setParent(None)
        for message, sender, is_user in self.chat_history:
            self._add_chat_bubble(message, sender, is_user, save_to_history=False)
        self._show_welcome_message()

    def send_message(self):
        user_message = self.user_input.text().strip()
        if not user_message or self.is_typing:
            return

        lang = self.language
        self._add_chat_bubble(user_message, self.ui_text[lang]["you"], True)
        self.user_input.clear()
        self.is_typing = True
        self._show_typing_indicator()
        if GEMINI_AVAILABLE and self.api_key:
            mode = 'health' if self.health_query_button.isChecked() else 'symptom'
            self.gemini_worker = GeminiWorker(user_message, mode, lang, self.api_key)
            self.gemini_worker.response_ready.connect(self._handle_gemini_response)
            self.gemini_worker.error_occurred.connect(self._handle_gemini_error)
            self.gemini_worker.start()
        else:
            QTimer.singleShot(1000, lambda: self._send_mock_response(lang))

    def _show_typing_indicator(self):
        lang = self.language
        system_msg = "✍️ " + (
            "AI is thinking..." if lang == "en" else "AI កំពុងគិត..."
        )
        self._post_system_message(system_msg)

    def _handle_gemini_response(self, response_text):
        self._remove_typing_indicator()
        lang = self.language
        self._add_chat_bubble(response_text, self.ui_text[lang]["bot"], False)
        self.is_typing = False

    def _handle_gemini_error(self, error_message):
        self._remove_typing_indicator()
        lang = self.language
        self._post_system_message(f"⚠️ {error_message}")
        self._send_mock_response(lang)

    def _remove_typing_indicator(self):
        if self.chat_layout.count() > 0:
            last_item = self.chat_layout.itemAt(self.chat_layout.count() - 1).widget()
            last_item.setParent(None)

    def _send_mock_response(self, lang):
        if self.health_query_button.isChecked():
            bot_response = self.ui_text[lang]["mock_health_response"]
        else:
            bot_response = self.ui_text[lang]["mock_symptom_response"]

        self._add_chat_bubble(bot_response, self.ui_text[lang]["bot"], False)
        self.is_typing = False

    def set_health_query_mode(self, from_click=False):
        self.health_query_button.setChecked(True)
        self.symptom_checker_button.setChecked(False)
        self.mode_label.setText(self.ui_text[self.language]["mode_label_health"])
        if from_click:
            self._post_system_message(self.ui_text[self.language]["switched_to_health"])

    def set_symptom_checker_mode(self, from_click=False):
        self.symptom_checker_button.setChecked(True)
        self.health_query_button.setChecked(False)
        self.mode_label.setText(self.ui_text[self.language]["mode_label_symptom"])
        if from_click:
            self._post_system_message(self.ui_text[self.language]["switched_to_symptom"])

    def _apply_styles(self):
        font = QFont("Segoe UI", 15)
        font.setStyleHint(QFont.StyleHint.System)
        QApplication.setFont(font)
        stylesheet = get_app_stylesheet(self.theme)
        self.setStyleSheet(stylesheet)
        self.header_frame.setObjectName("header_frame")
        self.title_label.setObjectName("title_label")
        self.mode_button_frame.setObjectName("mode_button_frame")
        self.mode_label.setObjectName("mode_label")
        self.input_frame.setObjectName("input_frame")
        self.send_button.setObjectName("send_button")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Healthcare Assistant")
    app.setApplicationVersion("2.0")

    demo_window = HealthBotDemoWindow()
    demo_window.show()
    sys.exit(app.exec())