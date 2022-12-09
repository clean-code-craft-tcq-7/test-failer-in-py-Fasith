from tshirts import get_size

cms_to_size_test_data = [
    (0,'S'), (1, 'S'), (37, 'S'), (38, 'S'),
    (39, 'M'), (40, 'M'), (41, 'M'), (42, 'L'),
    (43, 'L'), (100, 'L')
]

def test_get_size():
    for (cms, size) in cms_to_size_test_data:
        try:
            output = get_size(cms)
            assert(output == size)
        except AssertionError as e:
            e.args = (
                "Input: ", {cms},
                "Expected output: ", {size},
                "Actual output: ", {output}
                )
            raise
            

if __name__ == "__main__":
    test_get_size()