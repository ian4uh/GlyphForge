import json
from typing import Dict

# USAGE: Note that you will need to go manually fill each concentration and ritual field as 
# it's easier there, this tool doesn't fill it out

def get_input_with_default(prompt: str, current_value: str) -> str:
    user_input = input(f"{prompt} [{current_value}]: ")
    return user_input if user_input.strip() else current_value

def spell_entry_wizard(file):
    with open(file, "r") as f:
        spells = json.load(f)
    
    # Show available spell IDs
    print("Available spell IDs:")
    for spell in spells:
        print(f"- {spell['id']}")
    
    # Get starting point
    start_id = input("\nEnter spell ID to start from (press Enter to start from beginning): ").strip()
    
    # Find starting index
    start_index = 0
    if start_id:
        for i, spell in enumerate(spells):
            if spell['id'] == start_id:
                start_index = i
                break
    
    for spell in spells[start_index:]:
        print(f"\n=== Editing Spell: {spell['name']} ===")
        print(f"Current values:")
        print(f"ID: {spell['id']}")
        print(f"Level: {spell['level']}")
        print(f"School: {spell['school']}")
        print(f"Duration: {spell['duration']}")
        print(f"Range: {spell['range']}")
        print(f"Area Type: {spell['area_type']}")
        print(f"Damage Type: {spell['dtype']}")
        print(f"Condition: {spell['condition']}")
        print("-" * 40)

        spell["school"] = get_input_with_default("School (a/ev/t/n/en/i/d/c)", spell["school"])
        spell["duration"] = get_input_with_default("Duration", spell["duration"])
        spell["range"] = get_input_with_default("Range", spell["range"])
        spell["area_type"] = get_input_with_default("Area Type", spell["area_type"])
        spell["dtype"] = get_input_with_default("Damage Type", spell["dtype"])
        spell["condition"] = get_input_with_default("Condition", spell["condition"])

        # Save after each spell update
        with open(file, "w") as f:
            json.dump(spells, f, indent=4)

        if input("\nContinue to next spell? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    file = "Grimoire/wizard_2.json"
    spell_entry_wizard(file)
