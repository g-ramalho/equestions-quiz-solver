class Quiz:
    title: str
    questions: list[int] = []
    """
    represents the 0-indexed correct alternative for a question.
    `-1` means the correct answer has not been figured out yet.
    """
    is_finished: bool = False

    def __init__(self, title: str) -> None:
        self.title = title
