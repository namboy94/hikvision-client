"""
Main script that starts the program
@author Hermann Krumrey<hermann@krumreyh.com>
"""

import ConfigParser
import MainGUI

cams = ConfigParser.ConfigParser().parse()
MainGUI.MainGUI(cams)