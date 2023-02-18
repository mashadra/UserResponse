import UserResponseView
from UserResponseModel import UserResponseModel
from UserResponseView import UserResponseView


class UserResponseController:

    def __init__(self, view: UserResponseView):
        self.view = view

    def oneBlock(self) -> list[str]:
        model = UserResponseModel();
        self.view.showDirection(model.responseDescription)

        while (not model.outOfQuestions()):
            nextQuestion = model.getNextQuestion()
            userInput = self.view.getNumericalResponse(nextQuestion)
            while (not model.validInput(userInput)):
                self.view.showDirection("Please input a valid answer")
                userInput = self.view.getNumericalResponse(nextQuestion)
            model.saveResponse(userInput)

        return model.responses

    def fullExperiment(self):
        allResponses = []

        for i in range(0, 6):
            allResponses.append(self.oneBlock())

    def runGUI(self):
        self.view.runApp()