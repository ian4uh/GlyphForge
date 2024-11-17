# GlyphForge
Generate the glyphs based off [Gorilla of Denstiny](https://github.com/GorillaOfDestiny)'s science of magic system

# Usage
1. Run the `app.py` file
2. Fill in the dropdown boxes with desired values
3. Click the `Generate Glyph` button.

## Issues
Currently, I am running into an issue with each spell and how to list damage type. I added 2 options: buff and debuff but I feel this is not enough. This may be a matter where I have to suck it up and just add another attribute for status effects which creates issues. I am trying to keep the spells as realistic to the Spell Compendium that was released but I don't see how that's possible with everything.

# Primary Tasks
- [X] Update to work with draw_spell_2 from original project
- [X] Standardize the Attributes
- [X] Fix original code to allow for concentration and ritual attributes
- [X] Allow users to select base shape
- [X] Allow users to select line shape
- [X] Randomly generate glyphs

# Secondary Tasks
- [ ] Make a catalog of all spells and their attributes
- [ ] Allow users to search for spell and return glyph
- [ ] Have generated glyph return spell
    - [X] Cantrips
    - [ ] 1st Level
    - [ ] 2nd Level
    - [ ] 3rd Level
    - [ ] 4th Level
    - [ ] 5th Level
    - [ ] 6th Level
    - [ ] 7th Level
    - [ ] 8th Level
    - [ ] 9th Level


# DISCLAIMER
I did not create any of the algorithms used in the backend of this program. I exclusively made the GUI and assembled the JSONs used in the spell lookup. Aside from slight modifications, I have done nothing to the `bases.py`, `line_shapes.py`, and `writer.py` files.


