from pages.page_control import BasePage
from selenium.webdriver.common.by import By


class DownloadPageLocators:
    LOCATOR_DOWNLOAD_WEB_INSTALLER_WIN = (
        By.XPATH,
        "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
    )


class DownloadPage(BasePage):
    def __init__(self, driver):
        url = "https://sbis.ru/download"
        self.base_url = url
        super().__init__(driver, url)

    def click_on_the_download_web_installer_Win(self) -> None:
        self.find_element(
            DownloadPageLocators.LOCATOR_DOWNLOAD_WEB_INSTALLER_WIN
        ).click()

    def get_text_web_installer_win(self) -> str:
        return self.find_element(
            DownloadPageLocators.LOCATOR_DOWNLOAD_WEB_INSTALLER_WIN
        ).text
