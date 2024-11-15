import json

def format_spell_name(spell_id):
    # Split the id by hyphens and convert to list of words
    words = spell_id.split('-')
    
    # Process each word according to rules
    formatted_words = []
    for word in words:
        if word.lower() in ['of', 'the']:
            formatted_words.append(word.lower())
        else:
            formatted_words.append(word.capitalize())
    
    # Join words with spaces
    return ' '.join(formatted_words)

# Read the JSON file
with open('wizard_spells.json', 'r') as file:
    spells = json.load(file)

# Update each spell's name
for spell in spells:
    spell['name'] = format_spell_name(spell['id'])

# Write the updated data back to the file
with open('wizard_spells.json', 'w') as file:
    json.dump(spells, file, indent=4)
