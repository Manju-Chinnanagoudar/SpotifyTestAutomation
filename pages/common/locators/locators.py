from selenium.webdriver.common.by import By

class HeaderLocators:
    """Locators of the header elements which will be common for all screens
    """
    premium_btn = (By.XPATH, "//button[contains(text(),'Premium')]")
    support_btn = (By.XPATH, "//button[contains(text(),'Support')]")
    download_btn = (By.XPATH, "//button[contains(text(),'Download')]")

    signup_btn = (By.XPATH, "//button[contains(text(),'Sign up')]")
    login_btn = (By.XPATH, "//span[contains(text(),'Log in')]")

    profile_drpdn = (By.XPATH, "//header/button[1]")
    profile_name = (By.XPATH, "//header/button[1]/span")
    upgrade_btn = (By.XPATH, "//button[@title='Upgrade to Premium']")