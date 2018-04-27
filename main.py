from genlib import gen_ruleset
from src.calculator import Calculator

TEST_RESULT_PATH = 'data/eq2/testresult.txt'


def main():
    gen_ruleset.map_data(TEST_RESULT_PATH)
    gen_ruleset.print_clauses()


if __name__ == "__main__":
    main()
