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

import sys
from hikvision_client.config.ConfigParser import ConfigParser


def main(graphics_framework: str = ""):
    """
    The main method of the program
    It parses the local config file for cameras

    :return: None
    """
    if len(sys.argv) < 2:
        sys.argv.append("tk")
    if graphics_framework:
        sys.argv[1] = graphics_framework

    print(sys.argv)

    from hikvision_client.userinterface.LoginGui import LoginGui

    cams = ConfigParser.parse_camera_config()
    LoginGui(cams).start()


if __name__ == '__main__':
    main("gtk3")
