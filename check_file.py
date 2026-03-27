import json

with open('questions/fonds_pelerinage/hard.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total questions: {len(data)}')
print(f'First question: {data[0]["question"]}')
print(f'Last 3 questions:')
for q in data[-3:]:
    print(f'  - {q["question"]}')
