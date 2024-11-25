import json
import os

def add_srd_field():
    directory = 'Grimoire'
    
    # Process each JSON file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            
            # Read the JSON file
            with open(file_path, 'r') as file:
                spells = json.load(file)

            # Add given field to each spell
            for spell in spells:
                spell['srd'] = False

            # Write the updated data back to the file
            with open(file_path, 'w') as file:
                json.dump(spells, file, indent=4)

if __name__ == "__main__":
    add_srd_field()
