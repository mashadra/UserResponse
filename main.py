from UserResponseController import UserResponseController
from UserResponseView import UserResponseViewCLI, UserResponseViewGUI

if __name__ == '__main__':
    # Working CLI version
    view = UserResponseViewCLI()
    controller = UserResponseController(view)
    controller.fullExperiment()

    # Not working GUI version
#    view = UserResponseViewGUI()
#    controller = UserResponseController(view)
#    controller.runGUI()
#    controller.fullExperiment()