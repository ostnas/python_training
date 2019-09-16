# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_contact(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/edit.php")
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("John")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("Smith")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("Black")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("black_johny")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Title")
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("The Greatest Company")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("Somewhere, 123/2, 8214499")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("2")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("17263")
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("22341")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("17263234242323432434234")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("82133728342")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("23@mail.com")
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys("hello")
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys("www.google.com")
        Select(driver.find_element_by_name("bday")).select_by_visible_text("4")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[6]").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("September")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[43]").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1990")
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("Secondary address")
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("2")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("No notes")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        driver.find_element_by_link_text("home page").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
