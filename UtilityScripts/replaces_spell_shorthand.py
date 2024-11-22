import json
import os

# This script is used to go through the files I make and replace the shorthand of what I write
# mainly so I don't write each school of magic a million times

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

def format_duration(duration):
    if duration.lower() == "instant" or duration.lower() == "instant":
        return "Instantaneous"
    return duration

# Process all JSON files in EmptySpells directory
directory = 'Grimoire'
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Read the JSON file
        with open(file_path, 'r') as file:
            spells = json.load(file)

        # Update each spell's school and duration
        for spell in spells:
            spell['school'] = format_school(spell['school'])
            spell['duration'] = format_duration(spell['duration'])

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(spells, file, indent=4)
