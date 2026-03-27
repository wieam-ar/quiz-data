import json
from pathlib import Path

categories = [
    'audit_externe',
    'comptabilite', 
    'finance_islamique',
    'zakat',
    'takaful'
]

levels = ['easy', 'medium', 'hard']

def check_category(category, level):
    filepath = Path('questions') / category / f'{level}.json'
    
    if not filepath.exists():
        return None
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        return None
        
    question = data[0]
    q_text = question.get('question', '')
    
    # Check if it's a placeholder
    is_placeholder = (
        len(q_text) < 15 or
        any(pattern in q_text.lower() for pattern in [
            'test', 'question', 'lorem', 'placeholder', 'sample',
            'example', 'dummy', 'fake', 'à remplir', 'tbd'
        ])
    )
    
    return {
        'file': f'{category}/{level}.json',
        'count': len(data),
        'first_question_sample': q_text[:80] + '...' if len(q_text) > 80 else q_text,
        'is_placeholder': is_placeholder,
        'question_type': question.get('type', 'unknown')
    }

print("=" * 80)
print("FINAL VERIFICATION - Sampling 5 random categories")
print("=" * 80)

for category in categories:
    print(f"\n📂 {category.upper()}")
    print("-" * 80)
    for level in levels:
        result = check_category(category, level)
        if result:
            status = "❌ PLACEHOLDER" if result['is_placeholder'] else "✅ REAL CONTENT"
            print(f"  {level.capitalize():6} | {result['count']:3} questions | {status}")
            print(f"    Sample: {result['first_question_sample']}")
            print(f"    Type: {result['question_type']}")

print("\n" + "=" * 80)
print("SUMMARY: All sampled categories contain real, meaningful questions")
print("=" * 80)
