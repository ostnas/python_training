import re
from model.contact import Contact
from random import randrange

def test_contact_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", middlename="Smith", lastname="Black", nickname="black_johny",
                               title="Title", company="The Greatest Company", address="Somewhere, 123/2, 8214499",
                               home="22341", mobile="17263234242323432434234", work="82133728342", email="23@mail.com",
                               email2="hello", homepage="www.google.com", bday="4", bmonth="September", byear="1990",
                               address2="Secondary address", phone2="2", notes="No notes"))

    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_from_home_page = contact_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work,
                                                            contact.phone2]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))