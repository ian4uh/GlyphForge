# GlyphForge
Generate the glyphs based off [Gorilla of Denstiny](https://github.com/GorillaOfDestiny)'s science of magic system

# Usage
1. Run the `app.py` file
2. Fill in the dropdown boxes with desired values
3. Click the `Generate Glyph` button.

OR

1. Run the `app.py` file
2. Click the `Random Spell` button to generate a random glyph.

# Requirements

```bash
pip install -r requirements.txt
```

## Current Development
I have the app where conditions exist - however I think this might not be needed if this is restricted to just wizard spells which I am testing.

But first I have to catalog all the currently available spells which is draining my soul

## CONTRIBUTING
Feel free to use the `spell_entry.py` tool to help fill out the Grimoire. 

The `find_duplicates.py` file is to be used once all the spells have been entered to find all the duplicates so that further modifications can be made to the spell entries.

### Spell Fields
#### Unchanging
The following fields should not be modified in the json for organizational purposes and for the sake of contributing to the originators project.

- **id** - This is the id of the spell for database purposes.
- **name** - This is the normal string name of the spell.
- **level** - This is the level of the spell.
- **srd** - This boolean dictates if a spell is part of the SRD for D&D 5e. This is used for scripts and identifying what may be published and sold according to WotC guidelines.

#### Unfilled Fields
- **school** - This marks the school that the spell belongs to.
  - When filling out the json, you may type the shorthand (first letter of the school with the exceptions of `ev` for `Evocation` and `en` for `Enchantment` and then run the `replaces_spell_shorthands.py` utility to automatically translate them to their proper name. 
- **duration** - This is how long a spell effect will last
- **range** - This is how far a spell may be cast from
- **area_type** - This shows the area of effect of a spell (if it has one)
- **dtype** - This is the value for the damage type(s) of a spell (if it has one)
- **condition** - This shows any condition(s) a spell inflicts (if it inflicts any)
- **ritual** - This determines if a spell requires ritual casting
- **concentration** - This determines if a spell requires concentration


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

### Contains Duplicates:
- [X] Level 0 (Cantrips) 
    - [ ] SRD
- [X] Level 1
    - [ ] SRD
- [X] Level 2
    - [X] SRD
- [X] Level 3
    - [ ] SRD
- [ ] Level 4
    - [ ] SRD
- [ ] Level 5 - **FREE OF DUPLICATES**
- [ ] Level 6 - **FREE OF DUPLICATES**
- [ ] Level 7 - **FREE OF DUPLICATES**
- [ ] Level 8 - **FREE OF DUPLICATES**
- [ ] Level 9 - **FREE OF DUPLICATES**

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

## Secondary Tasks
- [ ] Make a catalog of all spells and their attributes
    - [X] Cantrips
    - [X] 1st Level
    - [X] 2nd Level
    - [X] 3rd Level
    - [ ] 4th Level
    - [ ] 5th Level
    - [X] 6th Level
    - [X] 7th Level
    - [X] 8th Level
    - [X] 9th Level
- [ ] Allow users to search for spell and return glyph
- [X] Have generated glyph return spell

## Tertiary Tasks
- [ ] Be able to change random spell values after generation
- [ ] Allow users to select colors
    - [ ] Whole glyph
    - [ ] Individual attributes

# DISCLAIMER
I did not create any of the algorithms used in the backend of this program. I exclusively made the GUI and assembled the JSONs used in the spell lookup. Aside from slight modifications, I have done nothing to the `bases.py` and `line_shapes.py`. I have made a number of changes to `writer.py`, but the majority is still the original code.
