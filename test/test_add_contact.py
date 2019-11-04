# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="John", middlename="Smith", lastname="Black", nickname="black_johny",
                               title="Title", company="The Greatest Company", address="Somewhere, 123/2, 8214499",
                               home="22341", mobile="17263234242323432434234", work="82133728342", email="23@mail.com",
                               email2="hello", homepage="www.google.com", bday="4", bmonth="September", byear="1990",
                               address2="Secondary address", phone2="2", notes="No notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


