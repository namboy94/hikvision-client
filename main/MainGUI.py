import tkinter
import easygui
import os

"""
Class that models the GUI
@author Hermann Krumrey<hermann@krumreyh.com>
"""
class MainGUI(object):

    """
    Constructor, which asks the user for a username and password, and which group of cameras to use
    Afterwards, a selection of cameras is shown that can be accessed
    @:param camConfigs - the camera configurations
    """
    def __init__(self, camsConfigs):

        self.user = easygui.enterbox("User")
        self.passwd = easygui.passwordbox("Password")
        self.camGroup = "'"

        self.selectorGUI = tkinter.Tk()
        for config in camsConfigs:
            name = config["name"]
            button = tkinter.Button(self.selectorGUI, text=name, command=lambda name=name:self.__setCamGroup__(name))
            button.pack(fill=tkinter.X)
        self.selectorGUI.mainloop()

        for config in camsConfigs:
            if config["name"] == self.camGroup:
                self.cams = config
                break

        self.gui = tkinter.Tk()
        self.buttons = []
        for cam in self.cams:
            if cam == "name": continue
            button = tkinter.Button(self.gui, text=cam, command=lambda cam=cam:self.__startCam__(cam))
            self.buttons.append(button)
            button.pack(fill=tkinter.X)
        self.gui.mainloop()

    """
    Starts a camera
    """
    def __startCam__(self, cam):
        os.system("vlc rtsp://" + self.user + ":" + self.passwd + "@" + self.cams[cam])

    """
    Sets the camera group
    """
    def __setCamGroup__(self, name):
        self.camGroup = name
        self.selectorGUI.destroy()