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


class ConfigParser(object):
    """
    Class that parses camera config files
    """

    @staticmethod
    def parse_camera_config():
        """
        Parses a configuration file to load the user's configured cameras
        
        :return: a list of configs
        """
        config_file = os.path.join(os.path.expanduser("~"), ".hikvision-client", "cam_config")

        with open(config_file, 'r') as config:
            content = config.read().split("\n")

            cameras = []

            for line in content:
                if line:
                    cam_name, cam_link = line.split("#####")
                    cameras.append((cam_name, cam_link))

        return cameras
