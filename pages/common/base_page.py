from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException, ElementNotInteractableException

from .exceptions import DragAndDropException, NavigationException, ElementNotFoundException, ElementActionException, ActionFailedException
from utils.logger import Logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        #self.config = config
        self.logger = Logger()

    def navigate(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Navigated to URL: {url}")
        except Exception as e:
            self.logger.error(f"Error navigating to URL: {url}. Error message: {e}")
            raise NavigationException(f"Error navigating to URL: {url}. Error message: {e}")

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(*locator)
            )
            self.logger.info(f"Element {locator} found")
            return element
        except TimeoutException:
            error_message = f"Timed out waiting for element {locator}"
            self.logger.error(error_message)
            raise ElementNotFoundException(error_message)


    def get_element(self, locator):
        """Get a web element based on the locator provided.

        Args:
            locator (tuple): The locator of the element to find.

        Returns:
            WebElement: The web element found.

        Raises:
            ElementNotFoundException: If the element is not found.
        """
        try:
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException:
            self.logger.error(f"Could not find element {locator}")
            raise ElementNotFoundException(f"Could not find element {locator}")

    def get_elements(self, locator):
        """Get a list of web elements based on the locator provided.

        Args:
            locator (tuple): The locator of the elements to find.

        Returns:
            list: A list of web elements found.

        Raises:
            ElementNotFoundException: If no elements are found.
        """
        try:
            elements = self.driver.find_elements(*locator)
            return elements
        except NoSuchElementException:
            self.logger.error(f"Could not find elements {locator}")
            raise ElementNotFoundException(f"Could not find elements {locator}")

    def click(self, locator):
        """Click on a web element based on the locator provided.

        Args:
            locator (tuple): The locator of the element to click.

        Raises:
            ElementNotFoundException: If the element is not found.
            ElementNotInteractableException: If the element is not interactable.
        """
        try:
            element = self.get_element(locator)
            element.click()
            self.logger.info(f"Clicked element {locator}")
        except (NoSuchElementException, ElementNotInteractableException):
            self.logger.error(f"Could not click element {locator}")
            raise ElementActionException(f"Could not click element {locator}")

    def send_keys(self, locator, text):
        """Send keys to a web element based on the locator provided.

        Args:
            locator (tuple): The locator of the element to send keys to.
            text (str): The text to send to the element.

        Raises:
            ElementNotFoundException: If the element is not found.
            ElementNotInteractableException: If the element is not interactable.
        """
        try:
            element = self.get_element(locator)
            element.send_keys(text)
            self.logger.info(f"Sent keys '{text}' to element {locator}")
        except (NoSuchElementException, ElementNotInteractableException):
            self.logger.error(f"Could not send keys to element {locator}")
            raise ElementActionException(f"Could not send keys to element {locator}")

    def get_text(self, locator):
        """Get the text of a web element based on the locator provided.

        Args:
            locator (tuple): The locator of the element to get text from.

        Returns:
            str: The text of the web element.

        Raises:
            ElementNotFoundException: If the element is not found.
        """
        try:
            element = self.get_element(locator)
            text = element.text
            self.logger.info(f"Got text '{text}' from element {locator}")
            return text
        except NoSuchElementException:
            self.logger.error(f"Could not get text from element {locator}")
            raise ElementNotFoundException(f"Could not get text from element {locator}")

    def is_element_present(self, locator):
        """
        Check if the element is present in the page
        :param locator: tuple of (by, value) of the element
        :return: True if element is present, False otherwise
        """
        try:
            elements = self.get_elements(locator)
            if elements:
                self.logger.info(f"Element {locator} is present")
                return True
            else:
                self.logger.warn(f"Element {locator} is not present")
                return False
        except:
            self.logger.error(f"Error checking for element {locator}")
            raise ElementNotFoundException(f"Error checking for element {locator}")
        
    def get_current_url(self):
        """
        Gets the current URL of the web page
        :return: str - current URL of the web page
        :raises: Exception if the current URL cannot be retrieved
        """
        try:
            url = self.driver.current_url
            self.logger.info(f"Current URL is {url}")
            return url
        except Exception as e:
            self.logger.error("Error getting current URL")
            raise WebDriverException("Error getting current URL")


    def get_title(self):
        """
        Gets the title of the web page
        :return: str - title of the web page
        :raises: Exception if the title cannot be retrieved
        """
        try:
            title = self.driver.title
            self.logger.info(f"Page title is {title}")
            return title
        except Exception as e:
            self.logger.error("Error getting page title")
            raise WebDriverException("Error getting page title")


    def get_page_source(self):
        """
        Gets the source code of the web page
        :return: str - source code of the web page
        :raises: Exception if the source code cannot be retrieved
        """
        try:
            page_source = self.driver.page_source
            self.logger.info("Page source has been retrieved")
            return page_source
        except Exception as e:
            self.logger.error("Error getting page source")
            raise WebDriverException("Error getting page source")


    def hover_over_element(self, locator):
        """
        Moves the mouse pointer over the specified element
        :param locator: tuple of (by, value) of the element
        :raises: Exception if the element cannot be found or hovered over
        """
        try:
            element = self.get_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
            self.logger.info(f"Hovered over element {locator}")
        except Exception as e:
            self.logger.error(f"Error hovering over element {locator}", exc_info=True)
            raise WebDriverException(f"Error hovering over element {locator}")


    def right_click_element(self, locator):
        """
        Performs a right-click on the specified element
        :param locator: tuple of (by, value) of the element
        :raises: Exception if the element cannot be found or right-clicked
        """
        try:
            element = self.get_element(locator)
            ActionChains(self.driver).context_click(element).perform()
            self.logger.info(f"Performed right-click on element {locator}")
        except Exception as e:
            self.logger.error(f"Error performing right-click on element {locator}", exc_info=True)
            raise WebDriverException(f"Error performing right-click on element {locator}")


    def double_click_element(self, locator):
        """
        Double-clicks the element located by the given locator.

        :param locator: tuple of (by, value) of the element
        :return: None
        :raises ElementNotFoundException: If the element is not found on the page
        :raises ActionFailedException: If the double-click action fails
        """
        try:
            element = self.get_element(locator)
            ActionChains(self.driver).double_click(element).perform()
            self.logger.info(f"Double-clicked on element {locator}")
        except NoSuchElementException:
            self.logger.error(f"Element {locator} not found")
            raise ElementNotFoundException(f"Element {locator} not found")
        except:
            self.logger.exception(f"Could not double-click element {locator}")
            raise ActionFailedException(f"Could not double-click element {locator}")


    def drag_and_drop(self, source_locator, target_locator):
        """
        Performs drag and drop operation from source element to target element.

        :param source_locator: tuple containing locator strategy and value of source element
        :param target_locator: tuple containing locator strategy and value of target element
        :raises: DragAndDropException if unable to perform drag and drop operation
        """
        try:
            source_element = self.find_element(source_locator)
            target_element = self.find_element(target_locator)
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
            self.logger.info(f"Drag and drop successful from {source_locator} to {target_locator}")
        except NoSuchElementException:
            self.logger.error(f"Element not found while performing drag and drop from {source_locator} to {target_locator}")
            raise DragAndDropException("Unable to perform drag and drop operation: Element not found")
        except WebDriverException as e:
            self.logger.error(f"Unable to perform drag and drop from {source_locator} to {target_locator}: {e}")
            raise DragAndDropException("Unable to perform drag and drop operation")


