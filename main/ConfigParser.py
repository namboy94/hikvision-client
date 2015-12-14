import os
import collections


class ConfigParser(object):

    def __init__(self):

        self.configs = []

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