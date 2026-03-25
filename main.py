from src.browser_finder import get_any_available_browser
from src.solver import Solver


def main():
    driver = get_any_available_browser()
    Solver(driver).run()


if __name__ == "__main__":
    main()
