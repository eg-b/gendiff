[![Maintainability](https://api.codeclimate.com/v1/badges/f2371655977d1a500b73/maintainability)](https://codeclimate.com/github/eg-b/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/f2371655977d1a500b73/test_coverage)](https://codeclimate.com/github/eg-b/python-project-lvl2/test_coverage)
[![Build Status](https://travis-ci.com/eg-b/python-project-lvl2.svg?branch=master)](https://travis-ci.com/eg-b/python-project-lvl2)

### Сommand line tool that helps you find the difference between two files. Works with json and yaml.

### Usage
```sh
gendiff [-h] [-f FORMAT] first_file second_file

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set output format: "jsontxt", "plain", "json"
```

### Installation

```sh
$ python3 -m pip install --user -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ eg-b-gendiff
```

[![asciicast](https://asciinema.org/a/g2sWU1Tc52NyT47X7Pp2Fnl4U.svg)](https://asciinema.org/a/g2sWU1Tc52NyT47X7Pp2Fnl4U)

### jsontxt gendiff

[![asciicast](https://asciinema.org/a/1eTcs9fW7SMawCBtO5uWwN30T.svg)](https://asciinema.org/a/1eTcs9fW7SMawCBtO5uWwN30T)

### yaml gendiff

[![asciicast](https://asciinema.org/a/pBc59xrM2LviG556BPvuqoDRw.svg)](https://asciinema.org/a/pBc59xrM2LviG556BPvuqoDRw)

### recursive diff

[![asciicast](https://asciinema.org/a/2Gwo37yJRwvUsRyzosmNk22AY.svg)](https://asciinema.org/a/2Gwo37yJRwvUsRyzosmNk22AY)

### plain format diff

[![asciicast](https://asciinema.org/a/jPwnvVQ5UL42GxAqLtuyUWcfx.svg)](https://asciinema.org/a/jPwnvVQ5UL42GxAqLtuyUWcfx)

### json format diff

[![asciicast](https://asciinema.org/a/PFrML5oqd8ldw6JUAui3iYOlD.svg)](https://asciinema.org/a/PFrML5oqd8ldw6JUAui3iYOlD)
