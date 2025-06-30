from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.sign_in_button = (By.ID, "signin")
        self.username_text = (By.CLASS_NAME, "username")

    def click_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(self.sign_in_button)).click()

    def login_success(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "username")))
        username = self.driver.find_element(By.CLASS_NAME, "username").text
        assert username == "demouser"
        print("Login Successful")