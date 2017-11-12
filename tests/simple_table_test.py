import unittest
from simple_table import SimpleTable


table_text_ascii = '''| Name | Age | City |
| Tom  | 12  | AAA  |
| Kate | 13  | BBB  |
'''

table_text_non_ascii = '''| Title                   | Price |
| JavaScript 高级程序设计 | 99    |
| Html Cookbook           | 100   |
| 计算机程序设计的艺术    | 128   |
'''


class TestSimpleTable(unittest.TestCase):
    def test_render_ascii(self):
        table = SimpleTable()
        table.set_headers(['Name', 'Age', 'City'])
        table.add_row(['Tom', '12', 'AAA'])
        table.add_rows([['Kate', '13', 'BBB']])

        self.assertEqual(table_text_ascii, str(table))

    def test_render_non_ascii(self):
        table = SimpleTable()
        table.set_headers(['Title', 'Price'])
        table.add_row(['JavaScript 高级程序设计', '99'])
        table.add_row(['Html Cookbook', '100'])
        table.add_row(['计算机程序设计的艺术', '128'])

        self.assertEqual(table_text_non_ascii, str(table))


if __name__ == '__main__':
    unittest.main()
