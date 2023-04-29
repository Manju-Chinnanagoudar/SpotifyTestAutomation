from .common.base_page import BasePage
from .locators.locators import LogInPageLocators
from .common.exceptions import LoginScreenException

class LogInPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        """
        Retruns the title of the page
        :return: Page title (str)
        """
        return self.get_title()
    
    def login_with_email(self, username, password, remember_me=False):
        """Login with email and password

        Args:
            username (str): User name of the user
            password (str): Password of the user
            remember_me (bool, optional): _description_. Defaults to False.
        :return: bool, True if login successful, False otherwise
        :exception: Raise LoginScreenException, if some issue happens while login
        """
        self.send_keys(LogInPageLocators.email, username)
        self.send_keys(LogInPageLocators.pwd, password)
        if remember_me:
            self.click(LogInPageLocators.remember)
        self.click(LogInPageLocators.login_btn)
        if self.get_page_title()=='Spotify - Web Player: Music for everyone':
            self.logger.info(f'Login sucessful with username: {username} and password{password}')
            return True
        elif self.is_element_present(LogInPageLocators.error):
            self.logger.warn(f'Login unsucessful with username: {username} and password{password}')
            return False
        else:
            raise LoginScreenException('Error while logging in')
            self.logger.error('Error while logging in')
        