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
from typing import List, Tuple
from hikvision_client.userinterface.MainGui import MainGui
from gfworks.templates.generators.GridTemplateGenerator import GridTemplateGenerator
templates = GridTemplateGenerator.get_grid_templates()
try:
    used_template = templates[sys.argv[1]]
except KeyError:
    used_template = templates["tk"]


# noinspection PyAbstractClass,PyUnresolvedReferences
class LoginGui(used_template):
    """
    A Login Screen for the program
    """

    cameras = []
    """
    The list of cameras read from the config file
    """

    login_button = None
    """
    The login button
    """

    username_label = None
    """
    A Label that displays the string "Username"
    """

    username_entry = None
    """
    An entry widget for the user to enter his/her username
    """

    password_label = None
    """
    A Label that displays the string "Password"
    """

    password_entry = None
    """
    A password entry widget for the user to enter his/her password
    """

    def __init__(self, cameras: List[Tuple[str, str]]) -> None:
        """
        Calls the constructor of the parent class with the window title "Login"

        :return: None
        """
        super().__init__("Login")
        self.cameras = cameras

    def lay_out(self) -> None:
        """
        Lays out the UI elements

        :return: None
        """
        self.login_button = self.generate_button("Log In", self.login)
        self.username_label = self.generate_label("Username")
        self.username_entry = self.generate_text_entry("")
        self.password_label = self.generate_label("Password")
        self.password_entry = self.generate_password_entry(self.login)

        self.position_absolute(self.username_label, 0, 0, 2, 1)
        self.position_absolute(self.password_label, 2, 0, 2, 1)
        self.position_absolute(self.username_entry, 0, 1, 2, 1)
        self.position_absolute(self.password_entry, 2, 1, 2, 1)
        self.position_absolute(self.login_button, 1, 3, 2, 1)

    def login(self, widget: object) -> None:
        """
        Tries to log in. Continues on to the Main Gui on success or shows an error dialog on failure

        :param widget: The button that called this method
        :return: None
        """
        str(widget)
        username = self.get_string_from_text_entry(self.username_entry)
        password = self.get_string_from_text_entry(self.password_entry)

        if username and password:
            MainGui((username, password), self.cameras, login_window=self).start()
        else:
            self.show_message_dialog("Error Logging In", "Please enter both a username and a password")
