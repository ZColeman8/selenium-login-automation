from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignInPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_dropdown = (By.ID, "username")
        self.password_dropdown = (By.ID, "password")
        self.login_btn = (By.ID, "login-btn")

    def fill_username(self):
        self.wait.until(EC.element_to_be_clickable(self.username_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='demouser']"))).click()

    def fill_password(self):
        self.wait.until(EC.element_to_be_clickable(self.password_dropdown)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='testingisfun99']"))).click()

    def submit_form(self):
        self.wait.until(EC.element_to_be_clickable(self.login_btn)).click()