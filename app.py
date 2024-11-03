import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image, ImageTk
import numpy as np
import writer

class SpellApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Spell Generator")

        # Load attributes
        self.ranges = self.load_attributes("attributes/range.txt")
        self.levels = self.load_attributes("attributes/levels.txt")
        self.areas = self.load_attributes("attributes/area_types.txt")
        self.dtypes = self.load_attributes("attributes/damage_types.txt")
        self.schools = self.load_attributes("attributes/school.txt")

        # Create dropdowns
        self.create_dropdowns()

        # Button to generate spell
        self.generate_button = tk.Button(master, text="Generate Glyph", command=self.generate_spell)
        self.generate_button.pack()

        # Label to display the image
        self.image_label = tk.Label(master)
        self.image_label.pack()

    def create_dropdowns(self):
        self.level_var = tk.StringVar()
        self.range_var = tk.StringVar()
        self.area_var = tk.StringVar()
        self.dtype_var = tk.StringVar()
        self.school_var = tk.StringVar()

        # Level dropdown
        ttk.Label(self.master, text="Select Level:").pack()
        level_dropdown = ttk.Combobox(self.master, textvariable=self.level_var, values=self.levels)
        level_dropdown.pack()

        # School dropdown
        ttk.Label(self.master, text="Select School:").pack()
        school_dropdown = ttk.Combobox(self.master, textvariable=self.school_var, values=self.schools)
        school_dropdown.pack()

        # Damage Type dropdown
        ttk.Label(self.master, text="Select Damage Type:").pack()
        dtype_dropdown = ttk.Combobox(self.master, textvariable=self.dtype_var, values=self.dtypes)
        dtype_dropdown.pack()

        # Area dropdown
        ttk.Label(self.master, text="Select Area Type:").pack()
        area_dropdown = ttk.Combobox(self.master, textvariable=self.area_var, values=self.areas)
        area_dropdown.pack()

        # Range dropdown
        ttk.Label(self.master, text="Select Range:").pack()
        range_dropdown = ttk.Combobox(self.master, textvariable=self.range_var, values=self.ranges)
        range_dropdown.pack()
        

    def load_attributes(self, filename):
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]

    def generate_spell(self):
        level = self.level_var.get()
        rang = self.range_var.get()
        area = self.area_var.get()
        dtype = self.dtype_var.get()
        school = self.school_var.get()

        # Generate the spell image
        image = self.create_spell_image(level, rang, area, dtype, school)
        
        # Display the image
        self.display_image(image)

    def create_spell_image(self, level, rang, area, dtype, school):
        buf = BytesIO()
        writer.draw_spell(level, rang, area, dtype, school, savename=buf)
        buf.seek(0)
        return buf

    def display_image(self, buf):
        image = Image.open(buf)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = SpellApp(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)  # Add this line
    root.mainloop()
