from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator: tuple[By, str], time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def go_to_site(self) -> WebDriver:
        return self.driver.get(self.base_url)

    def change_window(self) -> None:
        original_window = self.driver.current_window_handle
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.number_of_windows_to_be(2))

        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)

    def get_current_url(self) -> str:
        return self.driver.current_url
