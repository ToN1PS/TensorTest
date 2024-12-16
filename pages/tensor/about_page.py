from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.page_control import BasePage

from typing import Tuple, Optional


class AboutPageLocators:
    LOCATOR_ABOUT_BLOCK_3_1 = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img',
    )
    LOCATOR_ABOUT_BLOCK_3_2 = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img',
    )
    LOCATOR_ABOUT_BLOCK_3_3 = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img',
    )
    LOCATOR_ABOUT_BLOCK_3_4 = (
        By.XPATH,
        '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img',
    )


class AboutPage(BasePage):
    def __init__(self, driver):
        url = "https://tensor.ru/about"
        self.base_url = url
        super().__init__(driver, url)

    def check_same_resolution(self):
        img_1 = self.find_element(AboutPageLocators.LOCATOR_ABOUT_BLOCK_3_1)
        img_2 = self.find_element(AboutPageLocators.LOCATOR_ABOUT_BLOCK_3_2, time=2)
        img_3 = self.find_element(AboutPageLocators.LOCATOR_ABOUT_BLOCK_3_3, time=2)
        img_4 = self.find_element(AboutPageLocators.LOCATOR_ABOUT_BLOCK_3_4, time=2)

        res_img_1 = self._get_image_resolution(img_1)
        res_img_2 = self._get_image_resolution(img_2)
        res_img_3 = self._get_image_resolution(img_3)
        res_img_4 = self._get_image_resolution(img_4)

        return res_img_1 == res_img_2 == res_img_3 == res_img_4

    def _get_image_resolution(
        self, image: WebElement
    ) -> Tuple[Optional[str], Optional[str]]:

        width = image.get_attribute("width")
        height = image.get_attribute("height")

        return width, height
