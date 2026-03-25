from typing import Optional

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.question import Question
from src.quiz import Quiz


class Solver:
    driver: WebDriver
    quizzes: dict[str, Quiz] = {}

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def run(self, skip_finished_quizzes: bool = True):
        try:
            self.driver.get("https://www.equestions.com.br/escola/aluno/q-quiz.asp")

            questions_table = self.get_quiz_questions_table()

            for line in questions_table[1:]:
                quiz_status_cell = line.find_element(By.CLASS_NAME, "col6qi")

                quiz_link = quiz_status_cell.find_element(By.TAG_NAME, "a")

                if skip_finished_quizzes:
                    link_text = quiz_link.text.strip()
                    if link_text == "100,0%":
                        continue

                ActionChains(self.driver).click(quiz_link).perform()

                quiz_title = line.find_element(
                    By.CSS_SELECTOR, ".col5qi a"
                ).text.strip()

                current_quiz = self.quizzes[quiz_title]
                if not current_quiz:
                    current_quiz = Quiz(quiz_title)

                while not current_quiz.is_finished:
                    # - iterate quiz questions
                    # - check, at the end, which are correct
                    # - store questions, flag correct ones and retry until 100%

                    curr_alternative = 0

        finally:
            self.driver.quit()

    def get_quiz_questions_table(self):
        # Find the div with class "tabelaqi"
        tabelaqi_div = self.driver.find_element(By.CLASS_NAME, "tabelaqi")

        # Find all divs inside "tabelaqi" that start with the pattern "linha"
        return tabelaqi_div.find_elements(
            By.XPATH, ".//div[starts-with(@class, 'linha')]"
        )

    def get_quiz_answers(self, quiz: Quiz):
        """
        Finishes a quiz, marking which alternatives are correct and which are not
        """

    def answer_current_question(
        self, current_alternative: int, current_question: Question
    ) -> Question:
        alternatives_list = self.driver.find_element(By.CLASS_NAME, "respostas")
        visible_alternatives = alternatives_list.find_elements(
            By.XPATH, ".//li[not(@style='display:none')]"
        )

        num_visible_alternatives = len(visible_alternatives)

        if current_question.correct_alternative >= 0:
            current_alternative = current_question.correct_alternative
        else:
            current_alternative = min(current_alternative, num_visible_alternatives - 1)

        try:
            submit_btn = self.driver.find_element(By.ID, "botao")
            # Click the current_alternative-th visible <li>
            # and proceed to the next question
            ActionChains(self.driver).click(
                visible_alternatives[current_alternative]
            ).click(submit_btn).perform()

        except Exception as e:
            print(f"Failed to click current iteration's alternative: {e}")

        return Question(current_alternative)
