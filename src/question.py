class Question:
    correct_alternative: int = -1
    tried_alternatives: list[int] = []

    def __init__(self, tried_alternative, correct_alternative: int = -1) -> None:
        self.tried_alternatives.append(tried_alternative)
        self.correct_alternative = correct_alternative
