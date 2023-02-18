class UserResponseView:

    def __init__(self):
        pass

    def getNumericalResponse(self, message) -> str:
        pass

    def getTypedResponse(self, message) -> str:
        pass

    def showDirection(self, message):
        pass

    def runApp(self):
        pass


class UserResponseViewCLI (UserResponseView):

    def __init__(self):
        pass

    def getNumericalResponse(self, message) -> str:
        return input(message + " ")

    def getTypedResponse(self, message) -> str:
        return input(message)

    def showDirection(self, message):
        print(message)

    def runApp(self):
        pass


from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QGridLayout, QPushButton, QRadioButton
from PyQt5.QtCore import Qt

class UserResponseViewGUI (UserResponseView):

    def __init__(self):
        # creating GUI components
        self.app = QApplication([])

        # defining a top-level widget to hold everything
        self.w = QWidget()
        self.w.setWindowTitle("User Response")

        # making labels
        self.label1 = QLabel("")
        self.label2 = QLabel("")

        # making submit button
        self.submitButton = QPushButton(self.w)
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.buttonClicked)

        # making bubbles for response options
        self.op1 = QRadioButton()
        self.op2 = QRadioButton()
        self.op3 = QRadioButton()
        self.op4 = QRadioButton()
        self.op5 = QRadioButton()
        self.op6 = QRadioButton()
        self.op7 = QRadioButton()
        self.buttons = [self.op1, self.op2, self.op3, self.op4, self.op5, self.op6, self.op7]


        # the value updated when a number is hit
        self.value = "?"

        # setting up layout
        self.layout = QGridLayout()
        self.w.setLayout(self.layout)

        # adding components to layout
        # parameters go in the order row, column, row span, column span
        self.layout.addWidget(self.label1, 0,  0, 1, 7, Qt.AlignCenter)
        self.layout.addWidget(self.label2, 1, 0, 1, 7, Qt.AlignCenter)
        self.layout.addWidget(self.op1, 2, 0, Qt.AlignCenter)
        self.layout.addWidget(self.op2, 2, 1, Qt.AlignCenter)
        self.layout.addWidget(self.op3, 2, 2, Qt.AlignCenter)
        self.layout.addWidget(self.op4, 2, 3, Qt.AlignCenter)
        self.layout.addWidget(self.op5, 2, 4, Qt.AlignCenter)
        self.layout.addWidget(self.op6, 2, 5, Qt.AlignCenter)
        self.layout.addWidget(self.op7, 2, 6, Qt.AlignCenter)
        self.layout.addWidget(self.submitButton, 3, 0, 1, 7, Qt.AlignCenter)

        self.w.show()


    def getNumericalResponse(self, message) -> str:
        self.label2.setText(message)
        if self.submitButton:
            for i in range(0, 7):
                if self.buttons[i].isChecked():
                    self.value = str(i + 1)
            return str(self.value)

    def getTypedResponse(self, message) -> str:
        pass

    def showDirection(self, message):
        self.label1.setText(message)

    def buttonClicked(self):
        self.submitButton = True

    def runApp(self):
        self.app.exec_()