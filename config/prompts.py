
HEALTH_QUERY_PROMPT_EN = """As a healthcare assistant, provide brief health information about: {message}

Give me ONLY:
- 1-2 key facts (max 2 sentences)
- 1 simple recommendation
- When to see doctor (1 sentence)

Keep response under 100 words. Be concise."""

HEALTH_QUERY_PROMPT_KM = """ជាជំនួយការសុខភាព សូមផ្តល់ព័ត៌មានសុខភាពខ្លីអំពី: {message}

ផ្តល់ឱ្យខ្ញុំតែ៖
- ការពិតសំខាន់ 1-2 (អតិបរមា 2 ប្រយោគ)
- ការណែនាំសាមញ្ញ 1
- ពេលណាត្រូវជួបគ្រូពេទ្យ (1 ប្រយោគ)

រក្សាចម្លើយឱ្យក្រោម 100 ពាក្យ។ សង្ខេប។"""

# Symptom analysis prompt templates
SYMPTOM_PROMPT_EN = """Analyze these symptoms briefly: {message}

Provide:
- 2-3 possible causes with brief explanations
- 2 simple self-care tips
- Clear guidance on when to see a doctor

Keep under 150 words. Be helpful but direct."""

SYMPTOM_PROMPT_KM = """វិភាគរោគសញ្ញាទាំងនេះ៖ {message}

ផ្តល់៖
- មូលហេតុអាចមាន 2-3 ជាមួយការពន្យល់ខ្លី
- គន្លឹះថែទាំខ្លួនឯង 2
- ការណែនាំច្បាស់លាស់ពេលណាត្រូវជួបគ្រូពេទ្យ

រក្សាក្រោម 150 ពាក្យ។ ជួយប្រយោជន៍ប៉ុន្តែត្រង់ចំណុច។"""

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
