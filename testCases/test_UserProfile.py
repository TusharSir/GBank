import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By

from Utilities.Logger import Log_Class
from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.SignUp_Page import SignUp_Class

@pytest.mark.usefixtures("driver_setup")
class Test_UserProfile:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()
    Log = Log_Class.log_generator()
    driver = None
    @pytest.mark.sanity
    @pytest.mark.group1
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.title("BankApp url testing 01")
    def test_BankApp_Url_001(self):
        """self.Log.debug("This is debug")
        self.Log.info("This is info")
        self.Log.warning("This is warning")
        self.Log.error("This is error")
        self.Log.critical("This is critical")"""

        self.Log.info("Testcase test_BankApp_Url_001 is started")
        self.Log.info("Opening browser")
        self.driver.get("https://apps.credence.in/")
        self.Log.info("Checking page title")
        if self.driver.title == "Bank Application":
            self.Log.info("Testcase test_BankApp_Url_001 is passed")
            self.Log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_BankApp_Url_001_pass", attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\Screeshots\\test_BankApp_Url_001_pass.png")
            self.Log.info("Testcase test_BankApp_Url_001 is completed\n")
            assert True
        else:
            self.Log.info("Testcase test_BankApp_Url_001 is fail")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_BankApp_Url_001_fail.png")
            self.Log.info("Testcase test_BankApp_Url_001 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group1
    def test_Signup_002(self, faker):
        self.Log.info("Testcase test_Signup_002 is started")
        self.Log.info("Opening browser")
        #self.driver.get("https://apps.credence.in/user.html")
        self.su = SignUp_Class(self.driver)
        self.su.Click_Signup()
        self.Log.info(faker.name())
        self.su.Enter_Username(faker.email())
        self.Log.info("Entering the Password")
        self.su.Enter_Password("Demo555@")
        self.Log.info(faker.email())
        self.su.Enter_Email(faker.email())
        self.Log.info(faker.phone_number())
        self.su.Enter_Phone(faker.phone_number())
        self.Log.info("Click on Create user button")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.su.Click_CreateUser_Button()
        self.Log.info("Checking user creation")
        time.sleep(1)
        if self.su.Validate_User_Creation() == "User created successfully":
            self.Log.info("Testcase test_Signup_002 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Signup_002_pass.png")
            self.Log.info("Testcase test_Signup_002 is completed\n")
            assert True
        else:
            self.Log.info("Testcase test_Signup_002 is fail")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Signup_002_fail.png")
            self.Log.info("Testcase test_Signup_002 is completed\n")
            assert False

    @pytest.mark.sanity
    @pytest.mark.group2
    def test_Login_003(self):
        self.Log.info("Testcase test_Login_003 is started")
        self.Log.info("Opening browser")
        self.driver.get("https://apps.credence.in/login.html")
        self.lp = Login_Class(self.driver)
        self.Log.info("Click on Login link")
        #self.lp.Click_Login_Link()
        self.Log.info("Entering the username")
        self.lp.Enter_Username(self.Username)
        self.Log.info("Entering the password")
        self.lp.Enter_Password(self.Password)
        self.Log.info("Click on login button")
        self.lp.Click_Login_Button()
        self.Log.info("Checking the page title")
        if self.driver.title == "Dashboard":
            self.Log.info("Testcase test_Login_003 is passed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Login_003_pass.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, " //a[normalize-space()='User Management']").click()
            # time.sleep(2)
            # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
            # time.sleep(2)

            assert True

        else:
            self.Log.info("Testcase test_Login_003 is failed")
            self.Log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screeshots\\test_Login_003_fail.png")
            self.Log.info("Testcase test_Login_003 is completed\n")
            assert False


import random
import string
import time


def generate_random_username(length=6):
    return 'User' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_random_email(domain="gmail.com"):
    return generate_random_username() + "@" + domain


def generate_random_phone_number():
    return ''.join(random.choices(string.digits, k=10))

# Allure report image attach
# Full page screenshot
# Allure decorators
# Random username, email, phone number for signup write python program for this and give the data to signup testcase


# pytest -v -n=4 -m "sanity and group1" --html=HTMLReport/myreport_chrome.html --browser chrome --alluredir="Allure-results" -p no:warnings
#pytest -v -n auto --html=HTMLReport/myreport_chrome.html --browser chrome --alluredir="Allure-results" -reruns 1 --rerun-delay 1