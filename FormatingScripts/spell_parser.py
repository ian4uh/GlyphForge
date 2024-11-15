import re
import json
import os
from template import create_empty_spell_template

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
                spell['name'] = spell_id.replace('-', ' ').title()  # Convert id to title case name
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
