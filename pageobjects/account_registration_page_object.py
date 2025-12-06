
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#locators
class account_registration_page_object:

    rdio_male_xpath="//*[@id='gender']/span[1]/label"
    txt_first_name_xpath="//input[@id='FirstName']"
    txt_last_name_xpath="//input[@id='LastName']"
    txt_email_xpath="//input[@id='Email']"
    txt_company_xpath="//input[@id='Company']"
    txt_password_xpath="//input[@id='Password']"
    txt_confirm_password_xpath="//input[@id='ConfirmPassword']"
    btn_submit_xpath="//button[@id='register-button']"
    txt_confirm_message_xpath="//div[@class='result']"

#constuctor
    def __init__(self,driver):
        self.driver=driver

#action methods

    def my_radio_button(self):
        self.wait = WebDriverWait(self.driver, 15)
        self.radio_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.rdio_male_xpath))
        )
        self.radio_button.click()

    def my_first_name(self,fname):
        self.driver.find_element(By.XPATH, self.txt_first_name_xpath).send_keys(fname)

    def my_last_name(self,lname):
        self.driver.find_element(By.XPATH, self.txt_last_name_xpath).send_keys(lname)

    def my_email(self,email):
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def my_company_details(self,com):
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(com)

    def my_password(self,passw):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(passw)

    def my_confirm_pass(self,confirm):
        self.driver.find_element(By.XPATH, self.txt_confirm_password_xpath).send_keys(confirm)

    def my_submit_buttn(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def my_confirm_message(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_confirm_message_xpath).text
        except:
            None



