# Descatt

## About

Descatt is a Python script for casting your Linux desktop to a Chromecast. 

Audio casting is not supported and the framerate is very low.

## Requirements

* Python 3
* [Pyscreenshot](https://pypi.org/project/pyscreenshot/)
* [Cast All The Things](https://pypi.org/project/catt/)

## Installation

* `git clone https://github.com/tyea/descatt.git`
* `pip3 install pyscreenshot`
* `pip3 install catt`

## Example

```
foo@bar:~$ catt scan
Scanning Chromecasts...
192.168.0.1 - Tom's Chromecast - Google Inc. Chromecast Ultra
foo@bar:~$ python3 descatt.py
http://192.168.0.2:7425/index.html
foo@bar:~$ catt -d 192.168.0.1 cast_site http://192.168.0.2:7425/index.html
```

## Author

Written by Tom Yeadon in October 2019.
