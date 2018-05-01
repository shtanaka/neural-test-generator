from genlib import gen_ruleset, gen_test_file
from src.calculator_generated_test import func

TEST_RESULT_PATH = 'data/eq2/x1result.txt'


def main():
    gen_ruleset.map_data(TEST_RESULT_PATH)
    gen_test_file.generate_test_file(
        'src/', 'calculator_generated_test.py',
        ['from src.calculator import Calculator'],
        gen_ruleset.rules
    )
    print(func(3, 4, 1))
    print(func(1, -1, -1))
    print(func(5, 0, -4))


if __name__ == "__main__":
    main()
