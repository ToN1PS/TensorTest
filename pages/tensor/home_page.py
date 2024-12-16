from pages.page_control import BasePage

from selenium.webdriver.common.by import By


class HomePageLocators:
    LOCATOR_PEOPLE_POWER = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]')
    LOCATOR_PEOPLE_POWER_MORE_DETAILS = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a',
    )


class HomePage(BasePage):
    def __init__(self, driver):
        url = "https://tensor.ru/"
        self.base_url = url
        super().__init__(driver, url)

    def check_strength_in_people(self) -> bool:
        return self.find_element(HomePageLocators.LOCATOR_PEOPLE_POWER).is_enabled()

    def click_more_details(self) -> None:
        self.find_element(HomePageLocators.LOCATOR_PEOPLE_POWER_MORE_DETAILS).click()
