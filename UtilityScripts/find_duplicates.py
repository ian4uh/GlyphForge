import json

def find_duplicate_spells():
    # Dictionary to map json files to their section headers
    level_map = {
        'wizard_cantrips.json': '# Level 0',
        'wizard_1.json': '# Level 1',
        'wizard_2.json': '# Level 2',
        'wizard_3.json': '# Level 3',
        'wizard_4.json': '# Level 4',
        'wizard_5.json': '# Level 5',
        'wizard_6.json': '# Level 6',
        'wizard_7.json': '# Level 7',
        'wizard_8.json': '# Level 8',
        'wizard_9.json': '# Level 9'
    }
    
    # Read existing content from duplicates.md
    with open('duplicates.md', 'r') as file:
        content = file.read()
    
    # Process each spell level file
    for json_file, header in level_map.items():
        try:
            with open(f'Grimoire/{json_file}', 'r') as file:
                spells = json.load(file)
                
            # Dictionary to store spells with same attributes
            spell_groups = {}
            
            for spell in spells:
                key = (
                    spell['school'],
                    spell['duration'],
                    spell['range'],
                    spell['area_type'],
                    spell['dtype'],
                    spell['concentration'],
                    spell['ritual']
                )
                
                if key in spell_groups:
                    spell_groups[key].append(spell['name'])
                else:
                    spell_groups[key] = [spell['name']]
            
            # Generate duplicate information for this level
            duplicate_info = []
            for key, names in spell_groups.items():
                if len(names) > 1:
                    duplicate_info.append(f"\nSpells with attributes:")
                    duplicate_info.append(f"School: {key[0]}")
                    duplicate_info.append(f"Duration: {key[1]}")
                    duplicate_info.append(f"Range: {key[2]}")
                    duplicate_info.append(f"Area Type: {key[3]}")
                    duplicate_info.append(f"Damage Type: {key[4]}")
                    duplicate_info.append(f"Concentration: {key[5]}")
                    duplicate_info.append(f"Ritual: {key[6]}")
                    duplicate_info.append(f"Matching spells: {', '.join(names)}")
                    duplicate_info.append("-" * 50)
            
            # Replace content between current header and next header
            if duplicate_info:
                start_idx = content.find(header)
                next_header_idx = content.find('#', start_idx + 1)
                if next_header_idx == -1:
                    next_header_idx = len(content)
                    
                content = (content[:start_idx] + header + '\n' + 
                          '\n'.join(duplicate_info) + '\n\n' +
                          content[next_header_idx:])
                
        except FileNotFoundError:
            continue
    
    # Write updated content back to duplicates.md
    with open('duplicates.md', 'w') as file:
        file.write(content)

if __name__ == "__main__":
    find_duplicate_spells()
