from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/index.php")

    def fill_text_field(self, fieldname, value):
        wd = self.wd
        if value is not None:
            wd.find_element_by_name(fieldname).click()
            wd.find_element_by_name(fieldname).clear()
            wd.find_element_by_name(fieldname).send_keys(value)

    def select_date(self, fieldname, value):
        wd = self.wd
        if value is not None:
            Select(wd.find_element_by_name(fieldname)).select_by_visible_text(value)

    def destroy(self):
        self.wd.quit()