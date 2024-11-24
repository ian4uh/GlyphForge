import json

def find_duplicate_spells():
    # Load the spells from JSON
    with open('Grimoire\wizard_cantrips.json', 'r') as file:
        spells = json.load(file)
    
    # Dictionary to store spells with same attributes
    spell_groups = {}
    
    for spell in spells:
        # Create a tuple of the attributes we want to check
        key = (
            spell['level'],
            spell['school'],
            spell['duration'],
            spell['range'],
            spell['area_type'],
            spell['dtype'],
            #spell['condition'],
            spell['concentration'],
            spell['ritual']
        )
        
        # Add spell to group with matching attributes
        if key in spell_groups:
            spell_groups[key].append(spell['name'])
        else:
            spell_groups[key] = [spell['name']]
    
    # Print groups that have more than one spell
    print("Duplicate Spell Groups:")
    for key, names in spell_groups.items():
        if len(names) > 1:
            print("\nSpells with attributes:")
            print(f"Level: {key[0]}")
            print(f"School: {key[1]}")
            print(f"Duration: {key[2]}")
            print(f"Range: {key[3]}")
            print(f"Area Type: {key[4]}")
            print(f"Damage Type: {key[5]}")
            #print(f"Condition: {key[6]}")
            print(f"Concentration: {key[6]}")
            print(f"Ritual: {key[7]}")
            print("Matching spells:", ", ".join(names))
            print("-" * 50)

if __name__ == "__main__":
    find_duplicate_spells()
