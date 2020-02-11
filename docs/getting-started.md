# Getting Started

## Installation
Package spa2num is hosted on PyPi, so...

```bash
$ pip install spa2num
```

## Usage

```code
>>> from spa2num.converter import to_number
>>> to_number("ciento veintitrés millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve")
123456789
>>> to_number("novecientos ochenta y siete millones seiscientos cincuenta y cuatro mil trescientos veintiuno")
987654321
```

## Testing

A testing setup has been prepared. To run it locally, issue...

```bash
$ make test
...
___________________________________ summary ____________________________________
  py27: commands succeeded
  congratulations :)
```

## Generate Documentation

```bash
$ make docs
```

This wil generate a HTML version of your `docs/` and open it in a browser.
