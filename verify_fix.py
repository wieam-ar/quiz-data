import json

data = json.load(open('questions/fonds_pelerinage/hard.json'))
print(f'Total: {len(data)} questions\n')

print('First 3 questions:')
for q in data[:3]:
    print(f'  {q["id"]}: {q["question"][:70]}...')

print('\nLast 3 questions:')
for q in data[-3:]:
    print(f'  {q["id"]}: {q["question"][:70]}...')
