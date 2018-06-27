# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Reservar(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_reservar(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("id_username").clear()
        time.sleep(2)
        driver.find_element_by_id("id_username").send_keys("manuelzg")
        time.sleep(2)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("1234qwer")
        time.sleep(2)
        driver.find_element_by_id("id_password").send_keys(Keys.ENTER)
        driver.find_element_by_id("palabra").click()
        driver.find_element_by_id("palabra").clear()
        time.sleep(2)
        driver.find_element_by_id("palabra").send_keys("elec")
        time.sleep(2)
        driver.find_element_by_id("palabra").send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='main']/div/section/div/table/tbody/tr/td[4]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@id='main']/div/div[2]/div/table/tbody/tr/td[3]/a[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_link_text("Mi Perfil").click()
        time.sleep(2)
        driver.find_element_by_link_text("Ver Reservas").click()
        time.sleep(3)
    
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
