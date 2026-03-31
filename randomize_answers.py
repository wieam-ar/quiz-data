import json
import random
from pathlib import Path

def randomize_json_answers(input_file, output_file=None):
    """
    Randomize the position of correct answers in quiz JSON files.
    
    For singleChoice and dropdown: shuffles options and updates correctIndex
    For multipleChoice: shuffles options and updates correctIndexes array
    For trueFalse and fillBlank: leaves as is
    """
    if output_file is None:
        output_file = input_file
    
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    randomized = []
    
    for question in questions:
        q_copy = question.copy()
        question_type = q_copy.get('type', '')
        
        if question_type in ['singleChoice', 'dropdown']:
            # Shuffle options for singleChoice and dropdown
            if 'options' in q_copy and 'correctIndex' in q_copy:
                options = q_copy['options']
                correct_index = q_copy['correctIndex']
                correct_answer = options[correct_index]
                
                # Create list of (index, option) pairs and shuffle
                indexed_options = list(enumerate(options))
                random.shuffle(indexed_options)
                
                # Map old positions to new positions
                new_index_map = {}
                for new_pos, (old_pos, option) in enumerate(indexed_options):
                    new_index_map[old_pos] = new_pos
                
                # Update question
                q_copy['options'] = [option for _, option in indexed_options]
                q_copy['correctIndex'] = new_index_map[correct_index]
        
        elif question_type == 'multipleChoice':
            # Shuffle options for multipleChoice
            if 'options' in q_copy and 'correctIndexes' in q_copy:
                options = q_copy['options']
                correct_indexes = q_copy['correctIndexes']
                correct_answers = {options[i] for i in correct_indexes}
                
                # Create list of (index, option) pairs and shuffle
                indexed_options = list(enumerate(options))
                random.shuffle(indexed_options)
                
                # Map old positions to new positions
                new_index_map = {}
                for new_pos, (old_pos, option) in enumerate(indexed_options):
                    new_index_map[old_pos] = new_pos
                
                # Update question
                q_copy['options'] = [option for _, option in indexed_options]
                q_copy['correctIndexes'] = sorted([new_index_map[i] for i in correct_indexes])
        
        # trueFalse and fillBlank are left unchanged
        randomized.append(q_copy)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(randomized, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Randomized: {output_file}")

def main():
    base_path = Path('questions')
    json_files = list(base_path.rglob('*.json'))
    
    print(f"Found {len(json_files)} JSON files to process\n")
    
    for json_file in sorted(json_files):
        try:
            randomize_json_answers(str(json_file))
        except Exception as e:
            print(f"✗ Error processing {json_file}: {e}")
    
    print(f"\n✓ All {len(json_files)} files processed successfully!")

if __name__ == '__main__':
    main()
