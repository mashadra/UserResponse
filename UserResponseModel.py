class UserResponseModel:

    def __init__(self):
        self.questions = ["Compared to a handover with a human, the robot felt competent.",
                             "Compared to a handover with a human, the handover felt comfortable.",
                             "Compared to a handover with a human, the handover felt natural.",
                             "Compared to a handover with a human, the handover felt safe."]
        self.responseDescription = "Please rate the following statements on a scale from 1 to 7, " \
                                   "1 being strongly disagree, 7 being strongly agree, " \
                                   "4 being neither agree nor disagree."
        self.responseOptions = ["1", "2", "3", "4", "5", "6", "7"]
        self.responses = []
        self.counter = 0

    def getNextQuestion(self) -> str:
        self.counter += 1
        return self.questions[self.counter - 1]

    def saveResponse(self, response: str):
        self.responses.append(response)

    def outOfQuestions(self) -> bool:
        return self.counter == len(self.questions)

    def validInput(self, inp: str):
        return inp in self.responseOptions