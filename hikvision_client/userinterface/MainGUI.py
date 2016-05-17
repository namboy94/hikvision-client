"""
Copyright 2015,2016 Hermann Krumrey

This file is part of hikvision-client.

    hikvision-client offers a graphical user interface to access Hikvision IP
    cameras over RTSP.

    hikvision-client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    hikvision-client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with hikvision-client.  If not, see <http://www.gnu.org/licenses/>.
"""

# imports
import os


class MainGUI(object):
    """
    Class that models the GUI
    """

    def __init__(self, camsConfigs):
        """
        Constructor, which asks the user for a username and password, and which group of cameras to use
        Afterwards, a selection of cameras is shown that can be accessed
        @:param camConfigs - the camera configurations
        """

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