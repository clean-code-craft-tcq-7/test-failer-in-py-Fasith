from color_coder_constants import major_colors, minor_colors
from misaligned import *

def test_get_all_combinations():
    combinations = get_all_combinations(major_colors, minor_colors)
    assert(len(combinations) == 25)

    combinations = get_all_combinations(["A","B"], ["C","D"])    
    expected_output = [
        ("1","A","C"), ("2","A","D"),
        ("3","B","C"), ("4","B","D")
        ]
    assert(len(combinations) == 4)
    assert(combinations == expected_output)


def test_get_formatted_strings_from_combinations():
    test_combinations = [
        ("1","A","C"), ("2","AA","C"),
        ("11","A","C"), ("11","AA","C")
    ]
    expected_output = [
        "1  | A  | C",
        "2  | AA | C",
        "11 | A  | C",
        "11 | AA | C"
    ]
    formatted_strings = get_formatted_strings_from_combinations(test_combinations)
    assert(formatted_strings == expected_output)


# def test_get_color_map_from_formatted_strings():
#     test_formatted_string = [
#         "1  | A  | C",
#         "2  | AA | C",
#         "11 | A  | C",
#         "11 | AA | C"
#     ]

#     expected_output = """\
#                     1  | A  | C
#                     2  | AA | C
#                     11 | A  | C
#                     11 | AA | C
#                     """

#     expected_output = "".join[
#         "1  | A  | C",
#         "2  | AA | C",
#         "11 | A  | C",
#         ""
#     ]

#     formatted_color_map_string = get_color_map_from_formatted_strings(test_formatted_string)
#     assert(formatted_color_map_string == expected_output)
