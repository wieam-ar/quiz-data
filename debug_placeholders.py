import json
from pathlib import Path
import re

def is_placeholder(question_text):
    """Determine if a question is a placeholder or fake."""
    placeholder_patterns = [
        r'\w+\s*question\s*\d+',
        r'^test\s*\d*$',
        r'^lorem ipsum',
        r'^q\d+$',
        r'^placeholder',
        r'^\d+ ?\. ?$',
        r'^write your question',
        r'^[A-D]$',
        r'^true.*false',
        r'^image',
        r'^fake',
        r'^unknown',
        r'^X$|^Y$|^Z$|^W$',
    ]
    
    text_lower = question_text.lower().strip()
    for pattern in placeholder_patterns:
        if re.search(pattern, text_lower):
            return True
    if len(question_text.strip()) < 15:
        return True
    return False

# Check fonds_pelerinage/hard.json specifically
file_path = Path('questions/fonds_pelerinage/hard.json')
with open(file_path, 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}")
print(f"\nChecking for placeholders...")

placeholder_count = 0
for i, q in enumerate(questions):
    if is_placeholder(q.get('question', '')):
        placeholder_count += 1
        print(f"  Question {i+1} (id: {q['id']}): PLACEHOLDER - '{q['question']}'")

print(f"\nTotal placeholders found: {placeholder_count}")
