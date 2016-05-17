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


import os
import collections

"""
Class that parses camera config files
"""
class ConfigParser(object):

    """
    Constructor
    """
    def __init__(self):
        self.configs = []

    """
    Starts the parsing
    @:return a list of configs
    """
    def parse(self):
        configDir = os.getenv("HOME") + "/.cams/config"
        for config in os.listdir(configDir):
            camDictionary = collections.OrderedDict()
            camDictionary["name"] = config
            configFile = configDir + "/" + config
            file = open(configFile)
            for line in file:
                camname = line.split(":")[0]
                camlink = line.split(":", 1)[1]
                camDictionary[camname] = camlink
            self.configs.append(camDictionary)
        return self.configs