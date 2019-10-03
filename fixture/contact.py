class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()

    """return to home page by link in msgbox"""
    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select and edit first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[2]").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        self.app.fill_text_field("firstname", contact.firstname)
        self.app.fill_text_field("middlename", contact.middlename)
        self.app.fill_text_field("lastname", contact.lastname)
        self.app.fill_text_field("nickname", contact.nickname)
        self.app.fill_text_field("title", contact.title)
        self.app.fill_text_field("company", contact.company)
        self.app.fill_text_field("address", contact.address)
        self.app.fill_text_field("home", contact.home)
        self.app.fill_text_field("mobile", contact.mobile)
        self.app.fill_text_field("work", contact.work)
        self.app.fill_text_field("email", contact.email)
        self.app.fill_text_field("email2", contact.email2)
        self.app.fill_text_field("homepage", contact.homepage)
        self.app.select_date("bday", contact.bday)
        self.app.select_date("bmonth", contact.bmonth)
        self.app.fill_text_field("byear", contact.byear)
        self.app.fill_text_field("address2", contact.address2)
        self.app.fill_text_field("phone2", contact.phone2)
        self.app.fill_text_field("notes", contact.notes)