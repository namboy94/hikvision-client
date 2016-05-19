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
import sys
from typing import Tuple, List
from subprocess import Popen, PIPE
from gfworks.templates.generators.GridTemplateGenerator import GridTemplateGenerator
templates = GridTemplateGenerator.get_grid_templates()
try:
    used_template = templates[sys.argv[1]]
except KeyError:
    used_template = templates["tk"]


# noinspection PyUnresolvedReferences,PyAbstractClass
class MainGui(used_template):
    """
    Class that models the GUI
    """

    username = ""
    """
    The user's username
    """

    password = ""
    """
    The user's password
    """

    cameras = []
    """
    The list of cameras read while parsing the config
    """

    camera_buttons = []
    """
    The list of camera buttons
    """

    def __init__(self, credentials: Tuple[str, str], cameras: List[Tuple[str, str]], login_window: used_template):
        """
        Constructor, which asks the user for a username and password, and which group of cameras to use
        Afterwards, a selection of cameras is shown that can be accessed

        :param credentials: Tuple of username and password
        :param cameras: The list of cameras to which the user can connect to
        :param login_window: The login window calling this window
        """
        self.username, self.password = credentials
        self.cameras = cameras
        super().__init__("Hikvision Client", parent=login_window, hide_parent=True)

    def lay_out(self) -> None:
        """
        Handles the layout of the GUI

        :return: None
        """

        for camera in self.cameras:
            camera_name, camera_link = camera

            self.camera_buttons.append(self.generate_button(camera_name, self.start_stream, camera_link))

        row = 0
        column = 0
        for camera in self.camera_buttons:
            self.position_absolute(camera, column, row, 2, 1)
            column += 2

            if column % 6 == 0:
                row += 1
                column = 0

    def start_stream(self, widget: object, this_camera_link: str) -> None:
        """
        Starts the video feed for a camera

        :param widget: the button calling this method
        :param this_camera_link: the camera link used
        :return: None
        """
        str(widget)
        args = ["vlc",
                "-vvv",
                "--live",
                "--no-drop-late-frames",
                "--no-skip-frames",
                "--rtsp-tcp",
                ("rtsp://" + self.username + ":" + self.password + "@" + this_camera_link).rstrip()]
        Popen(args, stderr=PIPE).wait()

    def stop(self) -> None:
        """
        Overrides the stop() method to close the program if this window is closed

        :return: None
        """
        sys.exit(0)
