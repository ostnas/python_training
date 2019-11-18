from model.contact import Contact
import re

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

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        self.select_contact_by_index(index)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        # select contact
        self.select_contact_by_id(id)
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()

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
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastName = cells[1].text
                firstName = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, firstname=firstName, lastname=lastName, address=address,
                                                  all_email_from_home_page=all_email, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        wd = self.app.wd
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        middlename = wd.find_element_by_name("middlename").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        nickname = wd.find_element_by_name("nickname").get_attribute("value")
        title = wd.find_element_by_name("title").get_attribute("value")
        company = wd.find_element_by_name("company").get_attribute("value")
        address = wd.find_element_by_name("address").text
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        address2 = wd.find_element_by_name("address2").text
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        notes = wd.find_element_by_name("notes").text
        return Contact(id=id, firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname,
                       title=title, company=company, address=address, home=home,
                       mobile=mobile, work=work, email=email, email2=email2, email3=email3,
                       homepage=homepage,phone2=phone2, address2=address2, notes=notes)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    def select_group_to_add_contact(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[2]" % group_id).click()

    def select_group_to_delete_contact(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("(//option[@value='%s'])[1]" % group_id).click()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_to_add_contact(group_id)
        wd.find_element_by_name("add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_group_to_delete_contact(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.app.open_home_page()
        self.contact_cache = None

