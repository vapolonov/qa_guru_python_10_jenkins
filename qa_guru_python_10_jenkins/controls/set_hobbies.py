from selene import have
from selene.support.shared.jquery_style import s, ss


def set_hobby(hobby: str):
    ss('.custom-checkbox').element_by(have.text(hobby)).click()
