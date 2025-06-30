from src.pages.homepage import Homepage
from src.pages.sign_in_page import SignInPage

def test_login(driver):
    driver.get("https://www.bstackdemo.com/")

    homepage = Homepage(driver)
    homepage.click_sign_in()

    sign_in_page = SignInPage(driver)
    sign_in_page.fill_username()
    sign_in_page.fill_password()
    sign_in_page.submit_form()

    homepage.login_success()