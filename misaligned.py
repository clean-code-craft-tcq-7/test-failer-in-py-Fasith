from typing import List, Tuple
from color_coder_constants import major_colors, minor_colors

def get_all_combinations(major_colors: List[str], minor_colors: List[str]) -> List[Tuple[str,str,str]]:
    combinations = []
    index = 0
    for major_color in major_colors:
        for minor_color in minor_colors:
            index += 1
            combination = (str(index), major_color, minor_color)
            combinations.append(combination)
    return combinations


def get_formatted_strings_from_combinations(combinations: List[Tuple[str,str,str]]) -> List[str]:
    formatted_strings = []

    maximum_length_of_index = max(len(combination[0]) for combination in combinations)
    maximum_length_of_major_color = max(len(combination[1]) for combination in combinations)

    for (index, major_color, minor_color) in combinations:
        spacing_after_index = ' '*(maximum_length_of_index - len(index))
        spacing_after_major_color = ' '*(maximum_length_of_major_color - len(major_color))
        formatted_string = f"{index}{spacing_after_index} | {major_color}{spacing_after_major_color} | {minor_color}"
        formatted_strings.append(formatted_string)
    return formatted_strings
    

def get_color_map_from_formatted_strings(formatted_strings: List[str]):
    formatted_color_map_string = ''
    for formatted_string in formatted_strings:
        formatted_color_map_string += formatted_string
        formatted_color_map_string += '\n'
    return formatted_color_map_string
    

def get_color_map(major_colors:List[str], minor_colors:List[str]) -> str:
    color_code_combinations = get_all_combinations(major_colors, minor_colors)
    formatted_color_code_strings = get_formatted_strings_from_combinations(color_code_combinations)
    formatted_color_map = get_color_map_from_formatted_strings(formatted_color_code_strings)
    return formatted_color_map


def print_color_map():
    colour_map = get_color_map(major_colors, minor_colors)
    print(colour_map)



if __name__ == "__main__":
    print_color_map()