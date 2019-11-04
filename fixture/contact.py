from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_to_home_page()
        self.contact_cache = None

    """return to home page by link in msgbox"""
    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete first contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select and edit first contact
        self.app.open_home_page()
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

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

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastName = cells[1].text
                firstName = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(id=id, firstname=firstName, lastname=lastName))
        return list(self.contact_cache)