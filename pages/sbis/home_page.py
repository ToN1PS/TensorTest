from pages.page_control import BasePage
from selenium.webdriver.common.by import By
from utils.decorators import redirect_timer


class HomePageLocators:
    LOCATOR_CONTACTS_MENU = (
        By.XPATH,
        '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]',
    )
    LOCATOR_SBISRU_LINKS = (
        By.XPATH,
        '//*[@id="wasaby-content"]/div/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]',
    )

    LOCATOR_SBISRU_DOWNLOAD_LOCAL_VERSIONS = (
        By.XPATH,
        '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[9]/a',
    )


class HomePage(BasePage):
    def __init__(self, driver):
        url = "https://sbis.ru"
        self.base_url = url
        super().__init__(driver, url)

    def click_on_the_contacts(self) -> None:
        self.find_element(HomePageLocators.LOCATOR_CONTACTS_MENU).click()

    def click_on_the_link(self) -> None:
        self.find_element(HomePageLocators.LOCATOR_SBISRU_LINKS).click()

    @redirect_timer
    def click_on_download_local_vers(self) -> None:
        self.find_element(
            HomePageLocators.LOCATOR_SBISRU_DOWNLOAD_LOCAL_VERSIONS
        ).click()
