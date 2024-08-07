
# def print_color_map():
#     major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
#     minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
#     for i, major in enumerate(major_colors):
#         for j, minor in enumerate(minor_colors):
#             print(f'{i * 5 + j} | {major} | {minor}')
#     return len(major_colors) * len(minor_colors)



# result = print_color_map()
# assert(result == 25)
# print("All is well (maybe!)\n")




import logging

def create_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = {}
    for MajorColors, major in enumerate(major_colors):
        for MinorColors, minor in enumerate(minor_colors):
            index = MajorColors * len(minor_colors) + MinorColors
            index+=1
            color_map[index] = (major, minor)
            result_length = (len(major_colors) * len(minor_colors))
    return color_map, result_length



def log_color_map(color_map):
    for index, colors in color_map.items():
        logging.info(f"{index } | {colors[0]} | {colors[1]}")
    


color_map,result_length = create_color_map()
result = log_color_map(color_map)  
assert(result_length == 24)
print("All is well (maybe!)\n") 
