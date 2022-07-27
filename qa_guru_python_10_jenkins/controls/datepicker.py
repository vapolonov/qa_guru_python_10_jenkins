from selene.core.entity import Element
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class Datepicker:

    def __init__(self, element: Element):
        self.element = element

    def set_date(self, option: str):
        self.element.with_(set_value_by_js=True).set_value(option).press_tab()

    def set_date_of_birth(self, year: str, month: int, day: str):
        self.element.click()
        s('.react-datepicker__year-select').s(f'[value="{year}"]').click()
        s('.react-datepicker__month-select').s(f'[value="{month}"]').click()
        s(f'.react-datepicker__day--0{day}').click()

    def set_value(self, option: str):
        self.element.click()
        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput").value = ''
            ''')
        self.element.set_value(option).click()

