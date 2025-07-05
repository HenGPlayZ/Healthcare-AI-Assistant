# 🏥 Healthcare AI Assistant

A modern, bilingual (English/Khmer) healthcare chatbot built with PyQt6 and powered by Google's Gemini AI. This desktop application provides health information and symptom analysis in an intuitive, professional interface.
## 🖼️ Preview
### ENG
![Healthcare AI Assistant 1](https://cdn.hengnation.dev/lXb.png)
### KH
![Healthcare AI Assistant 2](https://cdn.hengnation.dev/9VJ.png)

## ✨ Features

- **🤖 AI-Powered Responses**: Uses Google Gemini 2.0 Flash for intelligent health consultations
- **🌐 Bilingual Support**: English and Khmer language support
- **🩺 Dual Modes**: 
  - General Health Information
  - Symptom Analysis & Checker
- **🎨 Modern UI**: Clean, professional interface with dark/light theme support
- **💬 Chat Interface**: WhatsApp-style chat bubbles for easy conversation
- **⚡ Fast Responses**: Optimized prompts for quick, concise answers
- **🔒 Privacy-Focused**: Local desktop application with secure API integration

## 🛠️ Technologies Used

- **Programming Language**: Python 3.12+
- **GUI Framework**: PyQt6
- **AI Integration**: Google Generative AI (Gemini API)
- **Configuration**: JSON-based config files
- **Environment Management**: python-dotenv
- **Text Processing**: Markdown to HTML conversion
- **Architecture**: Modular configuration system

## 📋 Requirements

### System Requirements
- Python 3.12 or higher
- Windows, macOS, or Linux
- Internet connection for AI responses

### Python Dependencies
Install the required packages using pip:

```bash
pip install PyQt6 google-generativeai python-dotenv
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
git clone https://github.com/HenGPlayZ/Healthcare-AI-Assistant
```

### 2. Install Dependencies
```bash
pip install PyQt6 google-generativeai python-dotenv
```

### 3. Set Up API Key

#### Get Google Gemini API Key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

#### Configure Environment Variables:
1. Navigate to the `config` folder
2. Copy `config/.env.example` to `config/.env`
3. Edit `config/.env` and add your API key:

```env
# Healthcare Assistant Configuration
GEMINI_API_KEY=your_actual_api_key_here
```

### 4. Run the Application
```bash
python main.py
```

## 📁 Project Structure

```
HealthCare/
│
├── main.py              # Main application file
├── README.md               # This file
├── requirements.txt        # Python dependencies
│
├── assets/                 # Static files
│   ├── icon.png           # Application icon
│   └── Dangrek-Regular.ttf # Custom font for Khmer text
│
└── config/                 # Configuration files
    ├── __init__.py        # Package initializer
    ├── prompts.py         # AI prompt templates
    ├── ui_text.py         # Interface text (EN/KM)
    ├── styles.py          # Application styling
    ├── .env.example       # Environment template
    └── .env               # Your API keys (create this)
```

## 🔧 Configuration

### Environment Variables (.env file)
Create a `.env` file in the `config` folder with:

```env
# Required: Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Optional: Add other configuration here
```

### Customization
- **Prompts**: Edit `config/prompts.py` to modify AI response behavior
- **UI Text**: Edit `config/ui_text.py` to change interface text or add new languages
- **Styling**: Edit `config/styles.py` to customize the appearance
- **Themes**: Default is dark mode, can be changed in `main.py`

## 🎯 Usage

1. **Launch the application**: Run `python main.py`
2. **Choose a mode**: 
   - 🩺 General Health: For health information and advice
   - 🔍 Symptom Checker: For symptom analysis
3. **Select language**: Click 🌐 to switch between English and Khmer
4. **Toggle theme**: Click ☀️/🌙 to switch between light and dark modes
5. **Ask questions**: Type your health-related questions and get AI-powered responses

## 🔍 Troubleshooting

### Common Issues

**❌ "Gemini API not available" error**
- Install the Google AI library: `pip install google-generativeai`

**❌ API key not working**
- Check your `.env` file is in the `config` folder
- Verify your API key is correct and active
- Ensure no extra spaces in the API key

**❌ Font not loading**
- Ensure `assets/Dangrek-Regular.ttf` exists
- Check file permissions
- The app will fall back to system fonts if custom font fails

**❌ Application won't start**
- Verify Python 3.12+ is installed
- Install PyQt6: `pip install PyQt6`
- Check all dependencies are installed

### Getting Help
If you encounter issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Ensure your API key is properly configured
4. Make sure all files in the `assets` and `config` folders are present

## 🚀 Development

### Adding New Features
1. **New Languages**: Add translations to `config/ui_text.py`
2. **Custom Prompts**: Modify `config/prompts.py`
3. **Styling Changes**: Edit `config/styles.py`
4. **New Modes**: Extend the mode system in `main.py`

### Architecture
The application uses a modular architecture:
- **Separation of Concerns**: UI, logic, and configuration are separated
- **Easy Maintenance**: All text, prompts, and styles are in config files
- **Extensible**: Easy to add new languages, themes, or features

## 📝 License

This project is provided as-is for educational and personal use.

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve the application.

---

**Note**: This application provides general health information only and should not replace professional medical advice. Always consult qualified healthcare professionals for medical concerns.
