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
from gfworks.templates.generators.GridTemplateGenerator import GridTemplateGenerator
from gfworks.templates.gtk3.Gtk3GridTemplate import Gtk3GridTemplate

templates = GridTemplateGenerator.get_grid_templates()

try:
    used_template = templates["gtk3"]
except KeyError:
    used_template = templates["tk"]


class LoginGui(used_template):
    """
    A Login Screen for the program
    """

    login_button = None
    username_label = None
    username_entry = None
    password_label = None
    password_entry = None

    def __init__(self) -> None:
        """
        Calls the constructor of the parent class with the window title "Login"

        :return: None
        """
        super().__init__("Login")

    def lay_out(self) -> None:
        """
        Lays out the UI elements

        :return: None
        """
        self.login_button = self.generate_button("Log In")
        self.username_label = self.generate_label("Username")
        self.username_entry = self.generate_text_entry("")
        self.password_label = self.generate_label("Password")
        self.password_entry = self.generate_text_entry("")

        self.position_absolute(self.username_label, 0, 0, 2, 1)
        self.position_absolute(self.password_label, 2, 0, 2, 1)
        self.position_absolute(self.username_entry, 0, 1, 2, 1)
        self.position_absolute(self.password_entry, 2, 1, 2, 1)
        self.position_absolute(self.login_button, 1, 3, 2, 1)

