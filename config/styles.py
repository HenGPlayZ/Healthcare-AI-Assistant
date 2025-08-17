

def get_app_stylesheet(theme="light"):
    if theme == "light":
        main_bg = "#f8fafc"
        card_bg = "#ffffff"
        chat_bg = "#f1f5f9"
        text_primary = "#1e293b"
        text_secondary = "#64748b"
        text_muted = "#94a3b8"
        border_color = "#e2e8f0"
        accent_color = "#667eea"
        input_bg = "#ffffff"
        shadow = "rgba(0, 0, 0, 0.08)"
        header_gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #667eea, stop:1 #764ba2)"
    else:  # dark theme
        main_bg = "#0f172a"
        card_bg = "#1e293b"
        chat_bg = "#0f172a"
        text_primary = "#f1f5f9"
        text_secondary = "#cbd5e1"
        text_muted = "#94a3b8"
        border_color = "#334155"
        accent_color = "#60a5fa"
        input_bg = "#1e293b"
        shadow = "rgba(0, 0, 0, 0.3)"
        header_gradient = "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1e3a8a, stop:1 #3730a3)"

    # Construct and return the complete stylesheet
    return f"""
        QMainWindow {{
            background-color: {main_bg};
            color: {text_primary};
            font-size: 15px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
        }}

        QFrame#header_frame {{
            background: {header_gradient};
            border: none;
            border-radius: 0px;
        }}

        QLabel#title_label {{
            color: white;
            font-size: 24px;
            font-weight: 600;
            letter-spacing: -0.5px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
        }}

        ModernButton {{
            background-color: {card_bg};
            color: {text_primary};
            border: 1px solid {border_color};
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            padding: 10px 16px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
        }}

        ModernButton:hover {{
            background-color: {accent_color};
            color: white;
            border-color: {accent_color};
        }}

        ModernButton:checked {{
            background-color: {accent_color};
            color: white;
            border-color: {accent_color};
            font-weight: 600;
        }}

        QScrollArea {{
            background-color: {chat_bg};
            border: none;
            border-radius: 8px;
        }}

        QFrame#mode_button_frame {{
            background-color: {card_bg};
            border: none;
            border-top: 1px solid {border_color};
        }}

        QLabel#mode_label {{
            color: {text_secondary};
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 8px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
        }}

        QFrame#input_frame {{
            background-color: {card_bg};
            border: none;
            border-top: 1px solid {border_color};
        }}

        QLineEdit {{
            background-color: {input_bg};
            border: 2px solid {border_color};
            border-radius: 12px;
            padding: 15px 16px;
            font-size: 15px;
            color: {text_primary};
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
            min-height: 25px;
            line-height: 1.6;
        }}

        QLineEdit:focus {{
            border-color: {accent_color};
            background-color: {input_bg};
        }}

        QPushButton#send_button {{
            background-color: {accent_color};
            color: white;
            border: none;
            border-radius: 12px;
            font-weight: 600;
            font-size: 14px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
            padding: 12px 20px;
        }}

        QPushButton#send_button:hover {{
            background-color: #5a67d8;
        }}

        QPushButton#send_button:pressed {{
            background-color: #4c51bf;
        }}

        QLabel#systemMessage {{
            color: {text_muted};
            font-style: italic;
            font-size: 13px;
            padding: 12px 16px;
            background-color: {border_color};
            border-radius: 8px;
            font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
            margin: 8px 0;
        }}

        QScrollBar:vertical {{
            background: transparent;
            width: 6px;
            border-radius: 3px;
            margin: 0;
        }}

        QScrollBar::handle:vertical {{
            background: {text_muted};
            border-radius: 3px;
            min-height: 20px;
            opacity: 0.5;
        }}

        QScrollBar::handle:vertical:hover {{
            background: {text_secondary};
            opacity: 0.8;
        }}

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
    """

def get_chat_bubble_style(is_user, theme="light"):
    if is_user:
        if theme == "light":
            return """
                ModernChatBubble {
                    background-color: #667eea;
                    border: none;
                    border-radius: 16px;
                    margin-left: 80px;
                    margin-right: 16px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                }
                #senderLabel { 
                    color: rgba(255,255,255,0.9); 
                    font-weight: 600; 
                    font-size: 12px; 
                    margin-bottom: 4px;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
                #messageLabel { 
                    color: white; 
                    font-size: 15px; 
                    line-height: 1.5;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
            """
        else:
            return """
                ModernChatBubble {
                    background-color: #60a5fa;
                    border: none;
                    border-radius: 16px;
                    margin-left: 80px;
                    margin-right: 16px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                }
                #senderLabel { 
                    color: rgba(255,255,255,0.9); 
                    font-weight: 600; 
                    font-size: 12px; 
                    margin-bottom: 4px;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
                #messageLabel { 
                    color: white; 
                    font-size: 15px; 
                    line-height: 1.5;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
            """
    else:  # bot message
        if theme == "light":
            return """
                ModernChatBubble {
                    background-color: white;
                    border: 1px solid #e2e8f0;
                    border-radius: 16px;
                    margin-right: 80px;
                    margin-left: 16px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                }
                #senderLabel { 
                    color: #667eea; 
                    font-weight: 600; 
                    font-size: 12px; 
                    margin-bottom: 4px;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
                #messageLabel { 
                    color: #1e293b; 
                    font-size: 15px; 
                    line-height: 1.6;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
            """
        else:
            return """
                ModernChatBubble {
                    background-color: #1e293b;
                    border: 1px solid #334155;
                    border-radius: 16px;
                    margin-right: 80px;
                    margin-left: 16px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                }
                #senderLabel { 
                    color: #60a5fa; 
                    font-weight: 600; 
                    font-size: 12px; 
                    margin-bottom: 4px;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
                #messageLabel { 
                    color: #f1f5f9; 
                    font-size: 15px; 
                    line-height: 1.6;
                    font-family: "Segoe UI", "Roboto", "Inter", sans-serif;
                }
            """
