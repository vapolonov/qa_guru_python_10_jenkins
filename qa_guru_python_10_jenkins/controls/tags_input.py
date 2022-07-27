from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, option: str):
        self.element.set_value(option).press_enter()
        return self

    def autocomplete(self, /, *, from_: str, to_: str = None):
        self.element.type(from_)
        ss('.subjects-auto-complete__option').element_by(have.text(to_)).click()

    def add_or_auto(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        ss(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
