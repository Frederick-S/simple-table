import unittest
from simple_table.simple_table import SimpleTable


table_text = '''| Name | Age | City |
| Tom  | 12  | AAA  |
| Kate | 13  | BBB  |
'''


class TestSimpleTable(unittest.TestCase):
    def test_render(self):
        table = SimpleTable()
        table.set_headers(['Name', 'Age', 'City'])
        table.add_row(['Tom', '12', 'AAA'])
        table.add_row(['Kate', '13', 'BBB'])

        self.assertEqual(table_text, str(table))
