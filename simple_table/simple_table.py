class SimpleTable():
    def __init__(self, headers=[], rows=[]):
        self.headers = headers
        self.rows = rows

    def set_headers(self, headers):
        self.headers = headers

    def add_row(self, row):
        self.rows.append(row)

    def add_rows(self, rows):
        self.rows = self.rows + rows

    def get_column_width(self):
        column_widths = [0] * len(self.headers)

        for i, header in enumerate(self.headers):
            column_widths[i] = max([len(header)] +
                                   [len(row[i]) for row in self.rows])

        return column_widths

    def __str__(self):
        table_text = ''
        contents = [self.headers] + self.rows
        column_widths = self.get_column_width()

        for i, row in enumerate(contents):
            for j, cell in enumerate(row):
                pad_right_width = column_widths[j] - len(cell) + 1
                table_text += '| ' + cell + ' ' * pad_right_width

            table_text += '|\n'

        return table_text
