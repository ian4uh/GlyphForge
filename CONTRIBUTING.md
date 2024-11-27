# CONTRIBUTING
Feel free to use the `spell_entry.py` tool to help fill out the Grimoire. 

The `find_duplicates.py` file is to be used once all the spells have been entered to find all the duplicates so that further modifications can be made to the spell entries.

## Spell Fields
### Unchanging
The following fields should not be modified in the json for organizational purposes and for the sake of contributing to the originators project.

- **id** - This is the id of the spell for database purposes.
- **name** - This is the normal string name of the spell.
- **level** - This is the level of the spell.
- **srd** - This boolean dictates if a spell is part of the SRD for D&D 5e. This is used for scripts and identifying what may be published and sold according to WotC guidelines.

### Unfilled Fields
- **school** - This marks the school that the spell belongs to.
  - When filling out the json, you may type the shorthand (first letter of the school with the exceptions of `ev` for `Evocation` and `en` for `Enchantment` and then run the `replaces_spell_shorthands.py` utility to automatically translate them to their proper name. 
- **duration** - This is how long a spell effect will last
- **range** - This is how far a spell may be cast from
- **area_type** - This shows the area of effect of a spell (if it has one)
- **dtype** - This is the value for the damage type(s) of a spell (if it has one)
- **condition** - This shows any condition(s) a spell inflicts (if it inflicts any)
- **ritual** - This determines if a spell requires ritual casting
- **concentration** - This determines if a spell requires concentration
