# Hikvision Client


This is a graphical client for use with Hikvision DVR systems which support RTSP.

The Program reads a config file from ~/.hikvision-client/cam_config, which defines which cameras the program can access.

Afterwards, the user is prompted for a username and password, which is then used to authenticate the connection to 
the Hikvision DVR

The program has been tested with the Hikvision DS-8016HFI-ST, it should however be able to connect to other
RTSP-enabled DVRs as well. Or any RTSP feed in general.


## Installation

To install the program, either download the source and run

    python setup.py install
    
or, if you have pip installed, run

    pip install hikvision_client
    
This should also install all python dependencies required by the program
Use the ```--user``` flag to install it only for the current user (or if you don't have
root/admin privileges)
    
The program makes use of the VLC Media Player, and as such it is required for VLC to be installed for this program
to function correctly.

## Writing the Config File

The program requires a configuration file located at ~/.hikvision-client/cam_config. It is a plain text file. To add a
camera, add a new line in the following format:

Camera_Name\#\#\#\#\#Camera_Link

The camera link is formatted like this:

    <domain>/h264/chX/main/av_stream  (analog)
    <domain>/Streaming/Channels/X01   (digital)

whereas 'X' is the channel number of the camera.


## Contributing

This project is automatically mirrored to [github](https://github.com/namboy94/hikvision-client), however all development
is conducted at a privately hosted [Gitlab instance](http://gitlab.namibsun.net/namboy94/hikvision-client). Issues
on both services are taken unto consideration.

## Documentation

Sphinx Documentation can be found [here](http://krumreyh.eu/hikvision-client/documentation/html/index.html).
A [PDF version](http://krumreyh.eu/hikvision-client/documentation/documentation.pdf) is also available

## Statistics

Automatically generated git statistics can be found [here](http://krumreyh.eu/hikvision-client/git_stats/index.html)