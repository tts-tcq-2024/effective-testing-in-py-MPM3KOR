
def create_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = {}
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            key = i * len(minor_colors) + j
            color_map[key] = (major, minor)
    return color_map

def print_color_map(color_map):
    for key, colors in color_map.items():
        print(f"{key+1 } | {colors[0]} | {colors[1]}")

color_map = create_color_map()
print_color_map(color_map)

