from selene import command, by
from selene.core.entity import Element
from selene.support.shared.jquery_style import s


class Dropdown:
    def __init__(self, state: Element, city: Element):
        self.state = state
        self.city = city

    def select(self, state_data: str):
        self.state.perform(command.js.scroll_into_view).click()
        s(by.text(state_data)).click()

    def autocomplete(self, city_data: str):
        self.city.s('#react-select-4-input').type(city_data).press_tab()

