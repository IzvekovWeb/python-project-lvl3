### Hexlet tests and linter status:
[![Actions Status](https://github.com/IzvekovWeb/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/IzvekovWeb/python-project-lvl3/actions)
[![Linter and Tests](https://github.com/IzvekovWeb/python-project-lvl3/actions/workflows/Tests-check.yml/badge.svg)](https://github.com/IzvekovWeb/python-project-lvl3/actions/workflows/Tests-check.yml)

[![Maintainability](https://api.codeclimate.com/v1/badges/b112df8f4f46a3aaee2b/maintainability)](https://codeclimate.com/github/IzvekovWeb/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/b112df8f4f46a3aaee2b/test_coverage)](https://codeclimate.com/github/IzvekovWeb/python-project-lvl3/test_coverage)

![python](https://img.shields.io/badge/python-%3E%3D3.8-brightgreen)
![pip](https://img.shields.io/badge/pip-%3E%3D20-blue)
![License](https://img.shields.io/github/license/IzvekovWeb/python-project-lvl2) 

# Page loader
## Description

This app is designed to load web pages and files related to them: html, css, js.
The application is available as a library or as a console utility.

## Installation

This program is not posted on pypi.org, to install it you need to clone the repository or download the zip archive of the project and build it.

    git clone git@github.com:IzvekovWeb/python-project-lvl3.git

    cd python-project-lvl3

    make build
    
After that you can install the package

    make package-install

The page-loader library is now installed in your environment.

---

## Download page

    page-loader [--output <path>] <url>



### Example

[![asciicast](https://asciinema.org/a/5wxRuAZoxqMEP0au9RmDfqwYY.svg)](https://asciinema.org/a/5wxRuAZoxqMEP0au9RmDfqwYY)