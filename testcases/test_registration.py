import time

from pageobjects.account_registration_page_object import *
from pageobjects.home_page_object import *
from utilities.random_string import *
from utilities.readproperties import *
import os

class TestRegistration:
    base_URL=get_config.get_application_url()

    def test_case1(self, setup):
        self.driver=setup
        self.driver.get(self.base_URL)
        self.driver.maximize_window()
        time.sleep(2)

        #home page
        self.hpage=homepagebject(self.driver)
        self.hpage.my_register_click()

        #account registration
        self.reg=account_registration_page_object(self.driver)
        self.reg.my_radio_button()
        self.reg.my_first_name("Srikanth")
        self.reg.my_last_name("Raju")
        self.email=random_string_generator()+"@gmail.com"
        self.reg.my_email(self.email)
        self.reg.my_company_details("password")
        self.reg.my_password("password")
        self.reg.my_confirm_pass("password")
        self.reg.my_submit_buttn()
        actual_text=self.reg.my_confirm_message()
        if actual_text=="Your registration completed":
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_case2.png")
            assert False


