from selenium.webdriver.common.by import By

class LogInPageLocators:
    """Contains the locators of Log in page
    """
    email = (By.ID, 'login-username')
    pwd = (By.ID, 'login-password')
    forgot_pwd = (By.ID, 'reset-password-link')
    login_btn = (By.ID, 'login-button')
    remember = (By.ID, 'login-remember')

    # Socail Logins
    fb = (By.XPATH, "//*[text()='Continue with Facebook']//ancestor::button")
    apple = (By.XPATH, "//*[text()='Continue with Apple']//ancestor::button")
    google = (By.XPATH, "//*[text()='Continue with Google']//ancestor::button")
    phone = (By.XPATH, "//*[text()='Continue with phone number']//ancestor::button")

    # Error message
    error = (By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")