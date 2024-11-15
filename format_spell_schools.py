import json

def format_school(school_code):
    school_mapping = {
        'a': 'Abjuration',
        'c': 'Conjuration',
        'd': 'Divination',
        'en': 'Enchantment',
        'ev': 'Evocation',
        'i': 'Illusion',
        'n': 'Necromancy',
        't': 'Transmutation'
    }
    return school_mapping.get(school_code.lower(), school_code)

# Read the JSON file
with open('wizard_spells.json', 'r') as file:
    spells = json.load(file)

# Update each spell's school
for spell in spells:
    spell['school'] = format_school(spell['school'])

# Write the updated data back to the file
with open('wizard_spells.json', 'w') as file:
    json.dump(spells, file, indent=4)
