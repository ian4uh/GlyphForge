import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image, ImageTk
import numpy as np
import writer
import bases
import line_shapes

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
        self.durations = [line.strip() for line in self.load_attributes("attributes/duration.txt")]


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
        self.duration_var = tk.StringVar()
        self.concentration_var = tk.StringVar()
        self.ritual_var = tk.StringVar()
        self.shape_var = tk.StringVar()
        self.lineType_var = tk.StringVar()

        # Create frames for organizing dropdowns
        top_frame = ttk.Frame(self.master)
        top_frame.pack()
        bottom_frame = ttk.Frame(self.master)
        bottom_frame.pack()

        # Level dropdown
        ttk.Label(top_frame, text="Select Level:").grid(row=0, column=0)
        level_dropdown = ttk.Combobox(top_frame, textvariable=self.level_var, values=self.levels)
        level_dropdown.grid(row=1, column=0, padx=5)

        # School dropdown
        ttk.Label(top_frame, text="Select School:").grid(row=0, column=1)
        school_dropdown = ttk.Combobox(top_frame, textvariable=self.school_var, values=self.schools)
        school_dropdown.grid(row=1, column=1, padx=5)

        # Damage Type dropdown
        ttk.Label(top_frame, text="Select Damage Type:").grid(row=0, column=2)
        dtype_dropdown = ttk.Combobox(top_frame, textvariable=self.dtype_var, values=self.dtypes)
        dtype_dropdown.grid(row=1, column=2, padx=5)

        # Area dropdown
        ttk.Label(top_frame, text="Select Area Type:").grid(row=0, column=3)
        area_dropdown = ttk.Combobox(top_frame, textvariable=self.area_var, values=self.areas)
        area_dropdown.grid(row=1, column=3, padx=5)

        # Range dropdown
        ttk.Label(top_frame, text="Select Range:").grid(row=0, column=4)
        range_dropdown = ttk.Combobox(top_frame, textvariable=self.range_var, values=self.ranges)
        range_dropdown.grid(row=1, column=4, padx=5)

        # Duration dropdown
        ttk.Label(top_frame, text="Select Duration:").grid(row=0, column=5)
        duration_dropdown = ttk.Combobox(top_frame, textvariable=self.duration_var, values=self.durations)
        duration_dropdown.grid(row=1, column=5, padx=5)

        # Concentration dropdown
        ttk.Label(bottom_frame, text="Concentration:").grid(row=0, column=0)
        concentration_dropdown = ttk.Combobox(bottom_frame, textvariable=self.concentration_var, values=["Yes", "No"])
        concentration_dropdown.grid(row=1, column=0, padx=5)

        # Ritual dropdown
        ttk.Label(bottom_frame, text="Ritual:").grid(row=0, column=1)
        ritual_dropdown = ttk.Combobox(bottom_frame, textvariable=self.ritual_var, values=["Yes", "No"])
        ritual_dropdown.grid(row=1, column=1, padx=5)

        # Shape Dropdown
        ttk.Label(bottom_frame, text="Select Shape:").grid(row=0, column=2)
        shape_dropdown = ttk.Combobox(bottom_frame, textvariable=self.shape_var, values=["Polygon", "Line", "Quadratic", "Circle", "Cubic", "Golden"])
        shape_dropdown.grid(row=1, column=2, padx=5)

        # Line Type Dropdown
        ttk.Label(bottom_frame, text="Select Line Type:").grid(row=0, column=3)
        lineType_dropdown = ttk.Combobox(bottom_frame, textvariable=self.lineType_var, values=["Centre Circle", "Non-Centre Circle", "Straight"])
        lineType_dropdown.grid(row=1, column=3, padx=5)
        
    def load_attributes(self, filename):
        with open(filename, "r") as f:
            return [line.strip() for line in f.readlines()]

    def generate_spell(self):
        level = self.level_var.get()
        rang = self.range_var.get()
        area = self.area_var.get()
        dtype = self.dtype_var.get()
        school = self.school_var.get()
        duration = self.duration_var.get()
        concentration = self.concentration_var.get()
        ritual = self.ritual_var.get()
        shape = self.shape_var.get()
        lineType = self.lineType_var.get()

        # Set default inputs - had to do it this way cause the results get passed in anyway
        if level == '':
            level = "None"
        if rang == '':
            rang = "None"
        if area == '':
            area = "None"
        if dtype == '':
            dtype = "None"
        if school == '':
            school = "None"
        if duration == '':
            duration = "Instant"
        if concentration == '':
            concentration = "No"
        if ritual == '':
            ritual = "No"

        match shape:
            case "Polygon":
                shape = bases.polygon
            case "Line":
                shape = bases.line
            case "Quadratic":
                shape = bases.quadratic
            case "Circle":
                shape = bases.circle
            case "Cubic":
                shape = bases.cubic
            case "Golden":
                shape = bases.golden
            case _:
                shape = bases.polygon

        match lineType:
            case "Centre Circle":
                lineType = line_shapes.centre_circle
            case "Non-Centre Circle":
                lineType = line_shapes.non_centre_circle
            case "Straight":
                lineType = line_shapes.straight
            case _:
                lineType = line_shapes.straight


        # Convert the level to lowercase in case of "None"
        level = level.lower()

        # Convert the concentration and ritual values to booleans
        if concentration=="Yes":
            concentration = True
        else:
            concentration = False

        if ritual=="Yes":
                ritual = True
        else:
            ritual = False

        # Generate the spell image
        image = self.create_spell_image(level, rang, area, dtype, school,duration,concentration, ritual, shape, lineType)
        
        # Display the image
        self.display_image(image)

    def create_spell_image(self, level, rang, area, dtype, school, duration, concentration,ritual, shape, lineType):
        buf = BytesIO()
        writer.draw_spell(level, rang, area, dtype, school, duration, concentration, ritual, shape, lineType, savename=buf)
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
