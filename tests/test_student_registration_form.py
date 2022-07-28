import allure
from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_python_10_jenkins.controls import set_hobbies
from qa_guru_python_10_jenkins.controls.datepicker import Datepicker
from qa_guru_python_10_jenkins.controls.dropdown import Dropdown
from qa_guru_python_10_jenkins.controls.table import Table
from qa_guru_python_10_jenkins.controls.tags_input import TagsInput
from utils import attach
from utils.helpers import Student, Subjects, Hobbies
from utils.utils import resource, arrange_student_registration_form_opened


def test_submit_automation_practice_form(setup_browser):
    browser = setup_browser

    with allure.step('Preconditions and open page for test'):
        arrange_student_registration_form_opened()

    with allure.step('Check page title'):
        browser.should(have.title('ToolsQA'))

    with allure.step('Check page header'):
        s('.main-header').should(have.exact_text('Practice Form'))

    with allure.step('Enter student name'):
        s('#firstName').type(Student.first_name)
    with allure.step('Enter student last name'):
        s('#lastName').type(Student.last_name)
    with allure.step('Enter student email'):
        s('#userEmail').type(Student.email)
    with allure.step('Enter student mobile number'):
        mobile_number = s('#userNumber')
        mobile_number.type(Student.mobile)

    with allure.step('Select student gender'):
        gender_group = s('#genterWrapper')
        gender_group.all('.custom-radio').element_by(have.exact_text(Student.gender)).click()

    with allure.step('Select student date of birth'):
        date_of_birth = Datepicker(s('#dateOfBirthInput'))
        date_of_birth.set_date_of_birth(year=Student.year_of_birth,
                                        month=Student.month_of_birth,
                                        day=Student.day_of_birth)
    with allure.step('Set Subjects'):
        subject = TagsInput(s('#subjectsInput'))
        subject.add(Subjects.maths)
        # subject.add(Subjects.maths).add(Subjects.english).add(Subjects.physics)
        subject.autocomplete(from_='Eng', to_=Subjects.english)
        subject.add_or_auto('Phys')

    with allure.step('Set hobbies'):
        set_hobbies.set_hobby(Hobbies.sports)
        set_hobbies.set_hobby(Hobbies.music)

    with allure.step('Load a file'):
        s('#uploadPicture').send_keys(resource('picture.png'))

    with allure.step('Enter the address'):
        s('#currentAddress').type(Student.address)

    with allure.step('Select state and city'):
        set_state_city = Dropdown(s('#state'), s('#city'))
        set_state_city.select(state_data=Student.state)
        set_state_city.autocomplete(city_data=Student.city)

    with allure.step('Send the form'):
        s('#submit').perform(command.js.click)

    with allure.step('Check student data'):
        results = Table(s('.modal-content .table'))
        results.cell(1, 1).should(have.text(f'{Student.first_name} {Student.last_name}'))
        results.cell(2, 1).should(have.text(Student.email))
        results.cell(3, 1).should(have.text(Student.gender))
        results.cell(4, 1).should(have.text(Student.mobile))
        results.cell(5, 1).should(have.text(Student.date_of_birth))
        results.cell(6, 1).should(have.text(f'{Subjects.maths}, {Subjects.english}, {Subjects.physics}'))
        results.cell(7, 1).should(have.text(f'{Hobbies.sports}, {Hobbies.music}'))
        results.cell(8, 1).should(have.text('picture.png'))
        results.cell(9, 1).should(have.text(Student.address))
        results.cell(10, 1).should(have.text(f'{Student.state} {Student.city}'))
