import allure
from selenium import webdriver
import pytest
import Allure
@allure.severity(allure.severity_level.NORMAL)
class TestOrm:
    @allure.severity(allure.severity_level.MINOR)
    def test_home(self):
        self.drivers=webdriver.Chrome()
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        images=self.drivers.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if images == True:
            assert True
        else:
            assert False
        self.drivers.close()
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        self.drivers = webdriver.Chrome()
        self.drivers.get("https://opensource-demo.orangehrmlive.com/")
        self.drivers.find_element_by_id("txtUsername").send_keys("Admin")
        self.drivers.find_element_by_id("txtPassword").send_keys("admin123")
        self.drivers.find_element_by_xpath("//*[@id='btnLogin']").click()
        title=self.drivers.title
        if title == "OrangeHRM":
            self.drivers.get_screenshot_as_file(filename=r"C:\Users\Ram\Desktop\Selenium\Allure\A.png")
            self.drivers.close()
            assert True
        else:
            self.drivers.close()
            assert False


