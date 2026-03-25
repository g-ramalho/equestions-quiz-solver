from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver


def get_any_available_browser() -> WebDriver:
    browsers: list[tuple[str, WebDriver]] = [  # pyright: ignore[reportAssignmentType]
        ("Chrome", webdriver.Chrome),
        ("Edge", webdriver.Edge),
        ("Firefox", webdriver.Firefox),
    ]

    for name, driver_class in browsers:
        try:
            print(f"Attempting to launch {name}...")
            # Selenium 4.6+ will automatically handle driver downloads
            driver = driver_class()  # pyright: ignore[reportCallIssue]
            print(f"Success! Using {name}.")
            return driver
        except WebDriverException:
            print(f"{name} not found or failed to launch.")
            continue

    raise RuntimeError(
        "No supported browsers (Chrome, Edge, Firefox) found on this system."
    )
