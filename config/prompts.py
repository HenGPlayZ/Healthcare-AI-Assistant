
HEALTH_QUERY_PROMPT_EN = """As a healthcare assistant, provide helpful health information about: {message}

Please include:
- Key health facts
- Simple recommendations
- When to see a doctor

Keep your response concise and easy to understand. Always remind users to consult healthcare professionals for medical advice."""

HEALTH_QUERY_PROMPT_KM = """ជាជំនួយការសុខភាព សូមផ្តល់ព័ត៌មានសុខភាពមានប្រយោជន៍អំពី: {message}

សូមរួមបញ្ចូល៖
- ការពិតសុខភាពសំខាន់ៗ
- ការណែនាំសាមញ្ញ
- ពេលណាត្រូវជួបគ្រូពេទ្យ

រក្សាចម្លើយរបស់អ្នកឱ្យខ្លី និងងាយយល់។ តែងតែរំលឹកអ្នកប្រើប្រាស់ឱ្យពិគ្រោះជាមួយអ្នកជំនាញសុខភាពសម្រាប់ការប្រឹក្សាពេទ្យ។"""

# Symptom analysis prompt templates
SYMPTOM_PROMPT_EN = """As a healthcare assistant, analyze these symptoms: {message}

Please provide:
- What might cause these symptoms (2-3 possibilities)
- Simple self-care recommendations
- When to see a doctor

Keep it brief and clear. Remember: This is not a medical diagnosis - always consult healthcare professionals for proper evaluation."""

SYMPTOM_PROMPT_KM = """ជាជំនួយការសុខភាព សូមវិភាគរោគសញ្ញាទាំងនេះ៖ {message}

សូមផ្តល់៖
- អ្វីដែលអាចបណ្តាលឱ្យមានរោគសញ្ញាទាំងនេះ (ទំនាកទំនង ២-៣)
- ការណែនាំថែទាំខ្លួនឯងសាមញ្ញ
- ពេលណាត្រូវជួបគ្រូពេទ្យ

រក្សាឱ្យខ្លី និងច្បាស់លាស់។ ចំណាំ៖ នេះមិនមែនជាការធ្វើរោគវិនិច្ឆ័យវេជ្ជសាស្ត្រនោះទេ - តែងតែពិគ្រោះជាមួយអ្នកជំនាញសុខភាពសម្រាប់ការវាយតម្លៃត្រឹមត្រូវ។"""

def get_prompt(mode, language, message):
    if mode == 'health':
        if language == 'en':
            return HEALTH_QUERY_PROMPT_EN.format(message=message)
        else:  # km
            return HEALTH_QUERY_PROMPT_KM.format(message=message)
    else:  # symptom mode
        if language == 'en':
            return SYMPTOM_PROMPT_EN.format(message=message)
        else:  # km
            return SYMPTOM_PROMPT_KM.format(message=message)
