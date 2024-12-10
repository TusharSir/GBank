import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture(scope="class")
def driver_setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("launching chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("launching firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("launching edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("chrome headless browser started")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible browser windows)
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("chrome headless browser started")
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no visible browser windows)
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://apps.credence.in/")
    driver.maximize_window()
    driver.implicitly_wait(15) # Wait for 5 seconds for element to load before proceeding with next operation

    # attaching driver to class
    request.cls.driver = driver
    yield driver # driver is return to the test cases or method
    driver.quit()
    print("Browser closed")


def pytest_metadata(metadata):
    metadata["Class"] = "Credence_Test#20"
    metadata["Description"] = "Test to verify the Credence homepage and search functionality"
    metadata["Test Type"] = "Functional"
    metadata["Author"] = "Credence : Test Automation Team"
    metadata["URL"] = "https://automation.credence.in/" # to add url key in report
    metadata.pop("Platform", None) # to remove the platform key
    # metadata.pop("Plugins", None)
    # How to edit summary in html report is your task




@pytest.fixture(params=[

    ("Admin", "pass"),
    ("Tushar", "pass"),
    ("Admin420", "fail"),
    ("demo2", "pass")
])
def getDataForSearchUser(request):
    return request.param
