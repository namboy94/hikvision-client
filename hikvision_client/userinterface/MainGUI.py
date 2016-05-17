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
from typing import Tuple, List
from gfworks.templates.generators.GridTemplateGenerator import GridTemplateGenerator
templates = GridTemplateGenerator.get_grid_templates()
try:
    used_template = templates["gtk3"]
except KeyError:
    used_template = templates["tk"]


class MainGUI(used_template):
    """
    Class that models the GUI
    """

    username = ""
    password = ""
    cameras = []
    camera_buttons = []

    def __init__(self, credentials: Tuple[str, str], cameras: List[Tuple[str, str]]):
        """
        Constructor, which asks the user for a username and password, and which group of cameras to use
        Afterwards, a selection of cameras is shown that can be accessed

        :param credentials: Tuple of username and password
        :param cameras: The list of cameras to which the user can connect to
        """
        self.username, self.password = credentials
        self.cameras = cameras
        super().__init__("Hikvision Client")

    def lay_out(self):

        print(self.cameras)
        for camera in self.cameras:
            camera_name, camera_link = camera

            def start_stream(widget):
                os.system("vlc -vvv --live --no-drop-late-frames --no-skip-frames --rtsp-tcp rtsp://" + self.username +
                          ":" + self.password + "@" + camera_link)

            self.camera_buttons.append(self.generate_button(camera_name, start_stream))

        print(self.camera_buttons)

        i = 0
        for camera in self.camera_buttons:
            self.position_absolute(camera, i, i, 1, 1)
            i += 1
