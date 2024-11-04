import bases
import line_shapes
import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm.auto import tqdm

cmap = plt.get_cmap('viridis')

#---------Functions for creating unique binary numbers------
def cycle_list(l, loops=1):
    n = len(l)
    for t in range(loops):
        l = [l[(i + 1) % n] for i in range(n)]
    return l

def generate_unique_combinations(L):
    combinations = generate_binary_strings(L)
    non_repeating = [combinations[0]]
    for i in tqdm(range(len(combinations)), desc="Generating Unique Binary Numbers"):
        ref = list(combinations[i])
        N = len(ref)
        test = 0
        for j in range(len(non_repeating)):
            for n in range(N):
                if cycle_list(list(non_repeating[j]), loops=n + 1) == ref:
                    test += 1
        if test == 0:
            non_repeating.append(combinations[i])
            
    for i in range(len(non_repeating)):
        non_repeating[i] = [int(s) for s in list(non_repeating[i])]
    return non_repeating

def generate_binary_strings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')

    genbin(bit_count)
    return binary_strings

#-------Functions for drawing runes
def decode_shape(in_array, k=1, point_color='k', on_color='darkred', off_color="grey",
                 label=None, base_fn=bases.polygon, base_kwargs=[],
                 shape_fn=line_shapes.straight, shape_kwargs=[], plot_base=False):
    n = len(in_array)
    x, y = base_fn(n, *base_kwargs)
    if plot_base:
        plt.scatter(x[1:], y[1:], s=70, facecolors='none', edgecolors=point_color)
        plt.scatter(x[0], y[0], s=70, facecolors=point_color, edgecolors=point_color)
        plt.axis('off')
        plt.axis('scaled')
    for i, elem in enumerate(in_array):
        P = [x[i], y[i]]
        Q = [x[(i + k) % n], y[(i + k) % n]]
        X, Y = shape_fn(P, Q, *shape_kwargs)
        if elem == 0:
            plt.plot(X, Y, color=off_color, ls="--", linewidth=0.25)
        elif elem == 1:
            plt.plot(X, Y, color=on_color, ls="-", label=label if i == np.where(in_array == 1)[0][0] else None,
                     linewidth=2)
        else:
            print(f'elem {elem} at index {i} is not valid, input being skipped')

def draw_multiple_inputs(in_array,
                         base_fn=bases.polygon, base_kwargs=[],
                         shape_fn=line_shapes.straight, shape_kwargs=[],
                         point_color='k', labels=[], legend=False, colors=[],
                         legend_loc="upper left"):
    
    if isinstance(colors, list) and len(colors) == 0:
        colors = [point_color] * in_array.shape[0]
    elif isinstance(colors, str):
        colors = [colors] * in_array.shape[0]
    n = in_array.shape[1]
    x, y = base_fn(n, *base_kwargs)
    plt.scatter(x[1:], y[1:], s=70, facecolors='none', edgecolors=point_color)
    plt.scatter(x[0], y[0], s=70, facecolors=point_color, edgecolors=point_color)
    
    if len(labels) != in_array.shape[0]:
        labels = [None] * in_array.shape[0]

    for i, k in enumerate(range(in_array.shape[0])):
        decode_shape(in_array[i], k=k + 1, base_fn=base_fn, base_kwargs=base_kwargs,
                     shape_fn=shape_fn, shape_kwargs=shape_kwargs, label=labels[i], on_color=colors[i])

    if labels[0] is not None and legend:
        plt.legend(loc=legend_loc, fontsize=10)
    plt.axis('off')
    plt.axis('scaled')

def load_attribute(fname):
    with open(fname, "r") as f:
        data = f.readlines()
    data = [d.strip().lower() for d in data]
    return data

def draw_spell(level, rang, area, dtype, school,
               savename="output.png", legend=False,
               base_fn=bases.polygon, base_kwargs=[],
               shape_fn=line_shapes.straight, shape_kwargs=[],
               colors=[], legend_loc="upper left", breakdown=True):
    
    ranges = load_attribute("attributes/range.txt")
    levels = load_attribute("attributes/levels.txt")
    area_types = load_attribute("attributes/area_types.txt")
    dtypes = load_attribute("attributes/damage_types.txt")
    schools = load_attribute("attributes/school.txt")
    i_range = ranges.index(rang)
    i_levels = levels.index(str(level))
    i_area = area_types.index(area)
    i_dtype = dtypes.index(dtype)
    i_school = schools.index(school)
    attributes = [i_levels, i_school, i_dtype, i_area, i_range]
    labels = [f"level: {level}",
              f"school: {school}",
              f"damage type: {dtype}",
              f"range: {rang}",
              f"area type: {area}"]
    N = 2 * len(attributes) + 1
    
    if len(colors) == 0 and breakdown:
        colors = [cmap(i / len(attributes)) for i in range(len(attributes))]
    
    if not os.path.isdir("Uniques/"):
        os.makedirs("Uniques/")
    
    if os.path.isfile(f'Uniques/{N}.npy'):
        non_repeating = np.load(f'Uniques/{N}.npy')
    else:
        non_repeating = generate_unique_combinations(N)
        non_repeating = np.array(non_repeating)
        np.save(f"Uniques/{N}.npy", non_repeating)

    input_array = np.array([non_repeating[i] for i in attributes])
    
    draw_multiple_inputs(input_array, labels=labels, legend=legend,
                         base_fn=base_fn, base_kwargs=base_kwargs,
                         shape_fn=shape_fn, shape_kwargs=shape_kwargs,
                         colors=colors, legend_loc=legend_loc)
    
    
    if savename is not None:
        plt.savefig(savename, transparent=False, bbox_inches='tight')
        plt.clf()
    else:
        plt.show()
