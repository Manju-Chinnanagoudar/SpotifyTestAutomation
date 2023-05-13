from .base_page import BasePage
from .locators.locators import HeaderLocators
from .exceptions import ElementNotFoundException

class HeaderSection(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_premium_btn(self):
        """Click the premium button in the header
        """
        try:
            self.click(HeaderLocators.premium_btn)
            self.logger.info('Clicked premium button in header')
        except:
            raise ElementNotFoundException('Failed to click on premium button in the header')
            self.logger.error('Failed to click on premium button in the header')

    def click_support_btn(self):
        """Click the support button in the header
        """
        try:
            self.click(HeaderLocators.support_btn)
            self.logger.info('Clicked support button in header')
        except:
            raise ElementNotFoundException('Failed to click on support button in the header')
            self.logger.error('Failed to click on support button in the header')

    def click_download_btn(self):
        """Click the download button in the header
        """
        try:
            self.click(HeaderLocators.download_btn)
            self.logger.info('Clicked download button in header')
        except:
            raise ElementNotFoundException('Failed to click on download button in the header')
            self.logger.error('Failed to click on download button in the header')        
    
    def click_signup_btn(self):
        """Click the signup button in the header
        """
        try:
            self.click(HeaderLocators.signup_btn)
            self.logger.info('Clicked pn sign up button in header')
        except:
            raise ElementNotFoundException('Failed to click on sign up button in the header')
            self.logger.error('Failed to click on sign up button in the header')

    def click_login_btn(self):
        """Click the Login button in the header
        """
        try:
            self.wait_for_element(HeaderLocators.login_btn)
            self.click(HeaderLocators.login_btn)
            self.logger.info('Clicked on login button in header')

        except:
            raise ElementNotFoundException('Failed to click on login button in the header')
            self.logger.error('Failed to click on login button in the header')
    
    def get_display_name(self):
        """Returns the text of the user name in the account dropdown
        """
        try:
            return self.get_text(HeaderLocators.profile_name)
        except:
            raise ElementNotFoundException('User Name unavailable')
            self.logger.error('User Name unavailable')
    
    def open_profile_drpdn(self):
        """Click the profile dropdown in the header
        """
        try:
            self.click(HeaderLocators.profile_drpdn)
            self.logger.info('Clicked on profile dropdown in header')
        except:
            raise ElementNotFoundException('Failed to click on profile dropdown in the header')
            self.logger.error('Failed to click on profile dropdown in the header')
    
    def is_logged_in(self):

        
        return not self.is_element_present(HeaderLocators.login_btn)