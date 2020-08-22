class Participant:

    """
        This class represent a participant of the event
 """
    def __init__(self, name: str, query_answers: dict):
        self._username = name    # as shown in app
        self._query_answers = query_answers
        self._investment = float()   # how much spent so far

    def set_answers(self, answers: dict):
        self._query_answers.update(answers)

    def increase_investment(self, sum_to_add: float):
        self._investment = self._investment + sum_to_add

    def get_answer(self, question: str):
        return self._query_answers.get(question)

    def set_answer(self, question: str, answer: bool):
        self._query_answers.question = answer

    def get_username(self):
        return self._username
