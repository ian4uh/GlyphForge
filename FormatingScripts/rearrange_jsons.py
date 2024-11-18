import json


file_name = 'EmptySpells//wizard_9.json'

# Read the original JSON file
with open(file_name, 'r') as file:
    cantrips = json.load(file)

# Rearrange each cantrip according to new format
rearranged_cantrips = []
for spell in cantrips:
    rearranged_spell = {
        "id": spell["id"],
        "name": spell["name"],
        "level": spell["level"],
        "school": spell["school"],
        "casting_time": "1 Action",
        "duration": spell["duration"],
        "range": spell["range"],
        "area_type": spell["area_type"],
        "dtype": spell["dtype"],
        "condition": "None",
        "ritual": spell["ritual"],
        "concentration": spell["concentration"]
    }
    rearranged_cantrips.append(rearranged_spell)

# Write to new JSON file
with open(file_name, 'w') as file:
    json.dump(rearranged_cantrips, file, indent=4)
