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

"""
The metadata is stored here. It can be used by any other module in this project this way, most
notably by the setup.py file
"""

project_name = "hikvision_client"
"""
The name of the project
"""

project_description = "A graphical client software for Hikvision (and other RTSP-enabled) IP cameras"
"""
A short description of the project
"""

version_number = "0.5"
"""
The current version of the program.
"""

development_status = "Development Status :: 3 - Alpha"
"""
The current development status of the program
"""

audience = "Intended Audience :: End Users/Desktop"
"""
The intended audience of this software
"""

environment = "Environment :: Other Environment"
"""
The intended environment in which the program will be used
"""

programming_language = 'Programming Language :: Python :: 3'
"""
The programming language used in this project
"""

topic = "Topic :: Multimedia :: Video :: Display"
"""
The broad subject/topic of the project
"""

language = "Natural Language :: English"
"""
The (default) language of this project
"""

compatible_os = "Operating System :: OS Independent"
"""
Th eOperating Systems on which the program can run
"""

project_url = "http://namibsun.net/namboy94/hikvision-client"
"""
A URL linking to the home page of the project, in this case a
self-hosted Gitlab page
"""

download_url = "http://gitlab.namibsun.net/namboy94/hikvision-client/repository/archive.zip?ref=master"
"""
A URL linking to the current source zip file.
"""

author_name = "Hermann Krumrey"
"""
The name(s) of the project author(s)
"""

author_email = "hermann@krumreyh.com"
"""
The email address(es) of the project author(s)
"""

license_type = "GNU GPL3"
"""
The project's license type
"""

license_identifier = "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
"""
The license used for this project
"""

pypi_requirements = ["gfworks"]
"""
List of requirements available on pypi.
"""

other_requirements = ["VLC"]
"""
List of requirements not available on pypi
"""

scripts = ["bin/hikvision-client-gtk", "bin/hikvision-client-tk"]
"""
List of script files to be installed during installation
"""
