# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        #self.accept_next_alert = True
    def test_untitled_test_case(self):
        driver = self.driver
        self.driver.get("https://www.easyjet.com/en")
        self.driver.find_element(By.ID,"ensCloseBanner").click()
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.XPATH, "//div[contains(@class, 'input-wrapper ui-widget')]//*[@aria-label='From Airport']").click()
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'input-wrapper ui-widget')]//*[@aria-label='From Airport']").send_keys("Antalya (AYT)")
        self.driver.find_element(By.ID,"selected-autocomplete-item").click()
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'input-wrapper ui-widget')]//*[@aria-label='To Airport']").click()
        self.driver.find_element(By.XPATH,"//div[contains(@class, 'input-wrapper ui-widget')]//*[@aria-label='To Airport']").send_keys("Manchester (MAN)")
        self.driver.find_element(By.ID,"selected-autocomplete-item").click()
        self.driver.find_element(By.XPATH, "//div[@class='outbound-date-picker']//span[@class='chosen-date']").click()
        time.sleep(60)
        self.driver.find_element(By.ID,"routedatepicker-25681").click()
        self.driver.find_element(By.XPATH,"//div[@id='drawer-dialog']/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div/div/div[3]/div/div/div[16]/a/span[3]").click()
        self.driver.find_element(By.XPATH,"//div[@id='drawer-dialog']/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div/div[23]/a/span[3]").click()
        self.driver.find_element(By.XPATH,"//div[@id='pageWrapper']/main/div/div/section/div/div/div/ul/li/div/div/form/button").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Arr'])[1]/following::span[4]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Arr'])[5]/following::span[4]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='All flights selected?'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Continue with Standard fare'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='AYT to MAN, Sun 12th May'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Select seats'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='MAN to AYT, Mon 20th May'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='AYT to MAN, Sun 12th MayMAN to AYT, Mon 20th May'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "//div[@id='drawer-dialog']/div/div[2]/div/div/div[2]/div/div/div/div/div[3]/button").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)=concat('Tell us what you', \"'\", 'd like to bring with you')])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Lets find your perfect car'])[1]/following::button[1]").click()
        self.driver.find_element(By.ID,"signup-email").clear()
        self.driver.find_element(By.ID,"signup-email").send_keys("erdemsukrudemirtas@gmail.com")
        self.driver.find_element(By.ID,"signin-username").clear()
        self.driver.find_element(By.ID,"signin-username").send_keys("erdemsukrudemirtas@gmail.com")
        self.driver.find_element(By.ID,"signin-password").clear()
        self.driver.find_element(By.ID,"signin-password").send_keys("YhBxghZ6b8vB-uy")
        self.driver.find_element(By.ID,"signin-login").click()
        self.driver.find_element(By.ID,"reason-1-41f0cb66-845d-424e-8221-b22fedc3350f").click()
        self.driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Adult 1'])[1]/following::span[1]").click()
        self.driver.find_element(By.ID,"age-dropdown-adult-1").click()
        Select(driver.find_element(By.ID,"age-dropdown-adult-1")).select_by_visible_text("18+")
        self.driver.find_element(By.XPATH,"//option[@value='number:18']").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Choose cover now'])[1]/following::button[1]").click()
        self.driver.find_element(By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Terms & Conditions'])[1]/following::span[2]").click()
        self.driver.find_element(By.XPATH,
            u"(.//*[normalize-space(text()) and normalize-space(.)='€'])[2]/following::button[1]").click()
        self.driver.find_element(By.ID,"card-details-card-number").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
