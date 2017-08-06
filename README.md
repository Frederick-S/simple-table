# simple-table [![Build Status](https://travis-ci.org/Frederick-S/simple-table.svg?branch=master)](https://travis-ci.org/Frederick-S/simple-table) [![Build status](https://ci.appveyor.com/api/projects/status/pckdlfb6o7w9canp?svg=true)](https://ci.appveyor.com/project/Frederick-S/simple-table) [![codecov](https://codecov.io/gh/Frederick-S/simple-table/branch/master/graph/badge.svg)](https://codecov.io/gh/Frederick-S/simple-table)  [![Code Health](https://landscape.io/github/Frederick-S/simple-table/master/landscape.svg?style=flat)](https://landscape.io/github/Frederick-S/simple-table/master) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/8d2496221fe44df5bf0b80891dd8bbf2)](https://www.codacy.com/app/Frederick-S/simple-table?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Frederick-S/simple-table&amp;utm_campaign=Badge_Grade)
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
