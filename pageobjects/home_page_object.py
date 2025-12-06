

from selenium.webdriver.common.by import By


#locators
class homepagebject:
    drp_txt_registor_xpath="//a[normalize-space()='Register']"
    drp_txt_login_xpath="//a[normalize-space()='Log in']"

#constuctor
    def __init__(self,driver):
        self.driver=driver

#action methods

    def my_register_click(self):
        self.driver.find_element(By.XPATH,self.drp_txt_registor_xpath).click()

    def my_login_click(self):
        self.driver.find_element(By.XPATH,self.drp_txt_login_xpath).click()






