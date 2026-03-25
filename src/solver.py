from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Solver:
    _driver: WebDriver

    def __init__(self, driver: WebDriver) -> None:
        _driver = driver.get("https://www.equestions.com.br/escola/aluno/q-quiz.asp")

    def run(self):
        try:
            self._driver.get("https://www.equestions.com.br/escola/aluno/q-quiz.asp")

            linha_divs = self.get_quiz_questions()

            for linha_div in linha_divs[1:]:
                # Access the div with class "col6qi"
                col6qi_div = linha_div.find_element(By.CLASS_NAME, "col6qi")

                # Access the <a> element inside "col6qi"
                link = col6qi_div.find_element(By.TAG_NAME, "a")

                # Check the internal text of the <a> element
                link_text = link.text.strip()
                if link_text == "100,0%":
                    continue  # Skip if the text is "100,0%"

                # Click the link if the text is not "100,0%"
                ActionChains(self._driver).move_to_element(link).click(link).perform()

        finally:
            # Close the browser
            self._driver.quit()

    def get_quiz_questions(self):
        # Find the div with class "tabelaqi"
        tabelaqi_div = self._driver.find_element(By.CLASS_NAME, "tabelaqi")

        # Find all divs inside "tabelaqi" that start with the pattern "linha"
        return tabelaqi_div.find_elements(
            By.XPATH, ".//div[starts-with(@class, 'linha')]"
        )
