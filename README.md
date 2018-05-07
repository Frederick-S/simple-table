# simple-table [![Build Status](https://travis-ci.org/Frederick-S/simple-table.svg?branch=master)](https://travis-ci.org/Frederick-S/simple-table) [![Build status](https://ci.appveyor.com/api/projects/status/pckdlfb6o7w9canp?svg=true)](https://ci.appveyor.com/project/Frederick-S/simple-table) [![codecov](https://codecov.io/gh/Frederick-S/simple-table/branch/master/graph/badge.svg)](https://codecov.io/gh/Frederick-S/simple-table) [![Maintainability](https://api.codeclimate.com/v1/badges/88f184b459b2061c1831/maintainability)](https://codeclimate.com/github/Frederick-S/simple-table/maintainability)
A very very very basic terminal table.

## Installation
```
pip3 install --upgrade simple_table
```

## Usage
```py
from simple_table import SimpleTable

table = SimpleTable()
table.set_headers(['Name', 'Age', 'City'])
table.add_row(['Tom', '12', 'AAA'])
table.add_rows([['Kate', '13', 'BBB']])

print(table)
```
