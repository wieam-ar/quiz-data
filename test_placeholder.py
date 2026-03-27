import re

def is_placeholder(question_text):
    """Determine if a question is a placeholder or fake."""
    # Check for placeholder patterns
    placeholder_patterns = [
        r'\w+\s*question\s*\d+',     # "category question 93", "Fonds_pelerinage question 7"
        r'^test\s*\d*$',             # "test", "test 1"
        r'^lorem ipsum',             # Lorem ipsum
        r'^q\d+$',                    # Q1, Q2
        r'^placeholder',              # placeholder
        r'^\d+ ?\. ?$',              # Just numbers
        r'^write your question',     # Instructions left behind
        r'^[A-D]$',                  # Just single letters
        r'^true.*false',             # True/False instruction
        r'^image',                   # image placeholder
        r'^fake',                    # fake question
        r'^unknown',                 # unknown
        r'^X$|^Y$|^Z$|^W$',          # Single placeholder letters
    ]
    
    text_lower = question_text.lower().strip()
    
    for pattern in placeholder_patterns:
        if re.search(pattern, text_lower):
            return True
    
    # Check if too short (less than 15 characters is suspicious for a real question)
    if len(question_text.strip()) < 15:
        return True
    
    return False

# Test cases
test_questions = [
    "Fonds_pelerinage question 93",
    "Fonds_pelerinage question 94",
    "Le modèle de financement du fonds repose sur:",
    "Lesquels sont des défis du fonds de pèlerinage?",
    "réponse",
    "1",
    "X",
]

for q in test_questions:
    result = is_placeholder(q)
    print(f"'{q}' -> PLACEHOLDER: {result}")
