import time

import pytest

from Utilities.readProperties import ReadConfigFile
from pageObjects.Login_Page import Login_Class
from pageObjects.Search_User_Page import Search_User_Class

@pytest.mark.usefixtures("driver_setup")
class Test_Search_User_params:
    Username = ReadConfigFile.GetUsername()
    Password = ReadConfigFile.GetPassword()

    @pytest.mark.regression
    @pytest.mark.group2
    def test_search_user_params_005(self,getDataForSearchUser):
        self.lp = Login_Class(self.driver)
        self.driver.get("https://apps.credence.in/login.html")
        self.lp.Enter_Username(self.Username)
        self.lp.Enter_Password(self.Password)
        self.lp.Click_Login_Button()
        self.su = Search_User_Class(self.driver)
        self.su.Click_Link_User_Management()

        Search_Username = getDataForSearchUser[0]
        print(Search_Username)
        Expected_result = getDataForSearchUser[1]
        print(Expected_result)

        self.su.Enter_UserName(Search_Username)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        self.su.Click_Search_User_Button()
        if self.su.Validate_Search_User() == "pass" and Expected_result == "pass":
            assert True
        elif self.su.Validate_Search_User() == "pass" and Expected_result == "fail":
            assert False
        elif self.su.Validate_Search_User() == "fail" and Expected_result == "pass":
            assert False
        elif self.su.Validate_Search_User() == "fail" and Expected_result == "fail":
            assert True


