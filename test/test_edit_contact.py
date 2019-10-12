# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname = "Test"))
    app.contact.edit_first_contact(Contact(firstname="2Johny", lastname="White", home="41243", address2="Another address"))