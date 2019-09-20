# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="John", middlename="Smith", lastname="Black", nickname="black_johny",
                   title="Title", company="The Greatest Company", address="Somewhere, 123/2, 8214499",
                   home="22341", mobile="17263234242323432434234", work="82133728342", email="23@mail.com",
                   email2="hello", homepage="www.google.com", bday="4", bmonth="September", byear="1990",
                   address2="Secondary address", phone2="2", notes="No notes"))
    app.session.logout()
