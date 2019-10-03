# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="2Johny", lastname="White", home="41243", address2="Another address"))
    app.session.logout()