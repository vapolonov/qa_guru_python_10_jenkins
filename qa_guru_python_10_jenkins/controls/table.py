from selene.core.entity import Element


class Table:
    def __init__(self, element: Element):
        self.element = element

    def cell(self, row_index: int, column_index: int):
        return self.element.all('tr')[row_index].all('td')[column_index]
