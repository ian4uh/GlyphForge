# GlyphForge
Generate the glyphs based off [Gorilla of Denstiny](https://github.com/GorillaOfDestiny)'s science of magic system

# Usage
1. Run the `app.py` file
2. Fill in the dropdown boxes with desired values
3. Click the `Generate Glyph` button.

OR

1. Run the `app.py` file
2. Click the `Random Spell` button to generate a random glyph.

## Current Development
I have the app where conditions exist - however I think this might not be needed if this is restricted to just wizard spells which I am testing.

But first I have to catalog all the currently available spells which is draining my soul

## Issues
There are spells that are basically identical, even with conditions and casting time
```
Spells with attributes:
Level: 0
School: Evocation
Duration: Instantaneous
Range: 60 feet
Area Type: None
Damage Type: Cold
Concentration: False
Ritual: False
Matching spells: Frostbite, Ray of Frost
```
And so I have to find a way to add unique identifiers. I've only finished cantrips but I imagine this will be common considering that there are only 32 cantrips and other levels like Level 2 have 61. 

### Possible Solutions:
- Add conditions spells inflict 
    - Currently testing - unlikely to succeed
- Add damage of spells
    - Doesn't work with spells that don't have damage (`Elementalism`, `Mold Earth`, `Shape Water`)
- Add casting time of spells (unlikely)
    - Most casting spells take 1 action
- Add category of spell
    - Control, Communication, Detection, Deception, etc.
    - This might be the best solution and may be able to be implemented without adding a whole set of attributes
        - Possibly just modifying the image to have a characteristic depending on the category
            - Will likely be difficult if different line type or base shape is used because I am bad at algorithms

# Primary Tasks
- [X] Update to work with draw_spell_2 from original project
- [X] Standardize the Attributes
- [X] Fix original code to allow for concentration and ritual attributes
- [X] Allow users to select base shape
- [X] Allow users to select line shape
- [X] Randomly generate glyphs

# Secondary Tasks
- [ ] Make a catalog of all spells and their attributes
    - [X] Cantrips
    - [X] 1st Level
    - [X] 2nd Level
    - [X] 3rd Level
    - [ ] 4th Level
    - [ ] 5th Level
    - [ ] 6th Level
    - [ ] 7th Level
    - [ ] 8th Level
    - [ ] 9th Level
- [ ] Allow users to search for spell and return glyph
- [ ] Have generated glyph return spell (ONLY WORKS FOR CANTRIPS CURRENTLY)


## Contriubte
Feel free to use the `spell_entry.py` tool to help fill out the Grimoire. The `find_duplicates.py` file is to be used once all the spells have been entered to find all the duplicates so that further modifications can be made to the spell entries.
# DISCLAIMER
I did not create any of the algorithms used in the backend of this program. I exclusively made the GUI and assembled the JSONs used in the spell lookup. Aside from slight modifications, I have done nothing to the `bases.py` and `line_shapes.py`. I have made a number of changes to `writer.py`, but the majority is still the original code.



# Requirements

```bash
pip install -r requirements.txt
```
