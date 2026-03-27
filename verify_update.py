import json
from pathlib import Path

# Sample verification of a few key files
test_files = [
    Path('questions/audit_externe/easy.json'),
    Path('questions/audit_externe/medium.json'),
    Path('questions/audit_externe/hard.json'),
    Path('questions/comptabilite/easy.json'),
    Path('questions/zakat/easy.json'),
]

print("File Verification Report")
print("="*60)

all_good = True
for file_path in test_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        count = len(data)
        first_id = data[0]['id']
        last_id = data[-1]['id']
        
        # Extract numeric IDs
        last_num = int(last_id.split('_')[-1])
        
        print(f"\n{file_path.relative_to('.')}")
        print(f"  Total questions: {count}")
        print(f"  IDs: {first_id} ... {last_id}")
        print(f"  Status: {'✓ OK' if (count == 100 and last_num == 100) else '✗ ISSUE'}")
        
        if count != 100:
            all_good = False
            
    except Exception as e:
        print(f"\n{file_path.relative_to('.')}: ERROR - {e}")
        all_good = False

print("\n" + "="*60)
print(f"Overall Status: {'✓ All files updated successfully' if all_good else '✗ Some issues found'}")

# Now count all updated files
print("\nCounting all updated files...")
total = 0
total_questions = 0
for json_file in sorted(Path('questions').rglob('*.json')):
    if json_file.name in ['easy.json', 'medium.json', 'hard.json']:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if len(data) >= 5:
                total += 1
                total_questions += len(data)
        except:
            pass

print(f"Total category files (easy/medium/hard): {total}")
print(f"Expected: 57 (19 categories × 3 levels)")
print(f"\nTotal questions across all files: {total_questions}")
print(f"Expected: 57 × 100 = 5,700 questions (5 original + 95 new per file)")
