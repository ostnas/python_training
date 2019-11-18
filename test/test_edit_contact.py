# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "Test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="2Johny", lastname="White", home="41243", address2="Another address")
    app.contact.edit_contact_by_id(random_contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = random_contact.id
    old_contacts.remove(random_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(Contact.clean, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

