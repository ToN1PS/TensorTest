from pages.page_control import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class SbisContactsPageLocators:
    LOCATOR_SBIS_TENSOR_BANNER_LOGO = (
        By.XPATH,
        '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img',
    )
    LOCATOR_SBIS_REGION = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span',
    )
    LOCATOR_REGION_KAMCHATSKIY = (
        By.XPATH,
        '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span',
    )

    LOCATOR_LIST_OF_PARTNERS_FIRST_PARTNER = (
        By.XPATH,
        '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div',
    )
    LOCATOR_AFTER_REGION_CHANGE = (
        By.CSS_SELECTOR,
        "#container > div.sbis_ru-content_wrapper.ws-flexbox.ws-flex-column > div > div.sbis_ru-container.sbisru-Contacts__relative > div.s-Grid-container.s-Grid-container--space.s-Grid-container--alignEnd.s-Grid-container--noGutter.sbisru-Contacts__underline > div:nth-child(1) > div > div:nth-child(2) > span > span",
    )


class ContactsPage(BasePage):
    def __init__(self, driver):
        url = "https://sbis.ru/contacts/"
        self.base_url = url
        super().__init__(driver, url)

    def click_on_the_tensor_banner(self) -> None:
        self.find_element(
            SbisContactsPageLocators.LOCATOR_SBIS_TENSOR_BANNER_LOGO, time=2
        ).click()

    def get_region(self) -> str:
        return self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_REGION).text

    def change_region(self) -> None:
        self.find_element(SbisContactsPageLocators.LOCATOR_SBIS_REGION).click()
        self.find_element(SbisContactsPageLocators.LOCATOR_REGION_KAMCHATSKIY).click()

        time.sleep(2.0)

    def check_list_of_partners(self) -> bool:
        return self.find_element(
            SbisContactsPageLocators.LOCATOR_LIST_OF_PARTNERS_FIRST_PARTNER
        ).is_enabled()

    def get_first_partner_text(self) -> str:
        return self.find_element(
            SbisContactsPageLocators.LOCATOR_LIST_OF_PARTNERS_FIRST_PARTNER
        ).text

    def get_title(self) -> str:
        return self.driver.title
