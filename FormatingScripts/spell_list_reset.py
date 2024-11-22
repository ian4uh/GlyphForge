import json
import os

directory = 'EmptySpells'

# Process each JSON file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Read the original JSON file
        with open(file_path, 'r') as file:
            spells = json.load(file)

        # Rearrange each spell according to new format
        rearranged_spells = []
        for spell in spells:
            rearranged_spell = {
                "id": spell["id"],
                "name": spell["name"],
                "level": spell["level"],
                "school": "None",
                "duration": "None",
                "range": "None",
                "area_type": "None",
                "dtype": "None",
                "condition": "None",
                "ritual": False,
                "concentration": False
            }
            rearranged_spells.append(rearranged_spell)

        # Write to the same JSON file
        with open(file_path, 'w') as file:
            json.dump(rearranged_spells, file, indent=4)
