import re
import json
import os

# This was just a script to make all the jsons based off the spell IDs

def create_empty_spell_template():
    return {
        "id": "",
        "name": "",
        "level": "",
        "school": "",
        "range": "",
        "duration": "",
        "area_type": "",
        "dtype": "",
        "ritual": False,
        "concentration": False
    }

def format_spell_name(spell_id):
    # Words that should remain lowercase
    lowercase_words = {'of', 'the', 'to', 'and'}
    
    # Split the spell name and capitalize each word
    words = spell_id.replace('-', ' ').split()
    titled_words = []
    
    for i, word in enumerate(words):
        if i == 0 or word not in lowercase_words:
            titled_words.append(word.title())
        else:
            titled_words.append(word.lower())
            
    return ' '.join(titled_words)

def parse_spells_md():
    # Create EmptySpells directory if it doesn't exist
    os.makedirs('EmptySpells', exist_ok=True)

    with open('spells.md', 'r') as file:
        content = file.read()

    # Dictionary to store spells by level
    level_spells = {}
    
    # Find all sections between <details> tags
    sections = re.findall(r'<details><summary>(.*?)</details>', content, re.DOTALL)
    
    for section in sections:
        # Extract level from the section header
        level_match = re.search(r'Level (\d+):', section)
        if level_match:
            level = level_match.group(1)
            
            # Extract spell IDs (they're in list format with hyphens)
            spell_ids = re.findall(r'- ([\w-]+)', section)
            
            # Create list of spell templates for this level
            spells = []
            for spell_id in spell_ids:
                spell = create_empty_spell_template()
                spell['id'] = spell_id
                spell['name'] = format_spell_name(spell_id)
                spell['level'] = level
                spell['school'] = ""
                spell['range'] = ""
                spell['duration'] = ""
                spell['area_type'] = ""
                spell['dtype'] = ""
                spell['ritual'] = False
                spell['concentration'] = False
                spells.append(spell)
                
            level_spells[level] = spells

    # Write each level's spells to its own file in EmptySpells directory
    for level, spells in level_spells.items():
        filename = os.path.join('EmptySpells', f"wizard_{level}.json")
        with open(filename, 'w') as f:
            json.dump(spells, f, indent=4)

if __name__ == "__main__":
    parse_spells_md()
