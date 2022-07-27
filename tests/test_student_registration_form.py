
from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from qa_guru_python_10_jenkins.controls import set_hobbies
from qa_guru_python_10_jenkins.controls.datepicker import Datepicker
from qa_guru_python_10_jenkins.controls.dropdown import Dropdown
from qa_guru_python_10_jenkins.controls.table import Table
from qa_guru_python_10_jenkins.controls.tags_input import TagsInput
from qa_guru_python_10_jenkins.utils import resource, arrange_student_registration_form_opened


class Subjects:
    maths = 'Maths'
    english = 'English'
    physics = 'Physics'


class Hobbies:
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Student:
    first_name = 'Vasily'
    last_name = 'Apolonov'
    email = 'test@mail.com'
    mobile = '9101112233'
    gender = 'Male'
    year_of_birth = '1974'
    month_of_birth = 8
    day_of_birth = '09'
    date_of_birth = '09 September,1974'
    address = 'Russia, Nizhny Novgorod'
    state = 'Uttar Pradesh'
    city = 'Lucknow'


def test_submit_automation_practice_form():
    arrange_student_registration_form_opened()

    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Practice Form'))

    # Filling the form
    s('#firstName').type(Student.first_name)
    s('#lastName').type(Student.last_name)
    s('#userEmail').type(Student.email)

    mobile_number = s('#userNumber')
    mobile_number.type(Student.mobile)

    # Select Gender (radio-button)
    gender_group = s('#genterWrapper')
    gender_group.all('.custom-radio').element_by(have.exact_text(Student.gender)).click()

    # Select Date of Birth
    date_of_birth = Datepicker(s('#dateOfBirthInput'))
    date_of_birth.set_date_of_birth(year=Student.year_of_birth,
                                    month=Student.month_of_birth,
                                    day=Student.day_of_birth)

    # Set Subjects
    subject = TagsInput(s('#subjectsInput'))
    subject.add(Subjects.maths)
    # subject.add(Subjects.maths).add(Subjects.english).add(Subjects.physics)
    subject.autocomplete(from_='Eng', to_=Subjects.english)
    subject.add_or_auto('Phys')

    # Set hobbies - checkbox
    set_hobbies.set_hobby(Hobbies.sports)
    set_hobbies.set_hobby(Hobbies.music)

    # Load a file
    s('#uploadPicture').send_keys(resource('picture.png'))

    # Filling the address
    s('#currentAddress').type(Student.address)

    set_state_city = Dropdown(s('#state'), s('#city'))
    set_state_city.select(state_data=Student.state)
    set_state_city.autocomplete(city_data=Student.city)

    s('#submit').perform(command.js.click)

    # Assert
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
