import allure

from pages.sbis.home_page import HomePage as SbisHome
from pages.sbis.contacts_page import ContactsPage as SbisContact
from pages.sbis.download_page import DownloadPage as SbisDownload
from pages.tensor.home_page import HomePage as TensorHome
from pages.tensor.about_page import AboutPage as TensorAboutPage

from utils.dowload_check import check_size_matching


@allure.title("Verify Navigation Between SBIS and Tensor Websites and Image Resolution")
@allure.feature("Regression tests")
@allure.description(
    """
    **Test Scenario:**

    This test verifies the navigation flow between the SBIS and Tensor websites, along with 
    specific element checks and image resolution validation on the Tensor site.

    **Test Steps:**
        1. Navigate to the SBIS website (https://sbis.ru/) and open the "Contacts" section.
        2. Locate the Tensor banner on the contacts page and click it.
        3. Navigate to the Tensor website (https://tensor.ru/) which will open in a new tab.
        4. On the Tensor homepage, verify that the "Strength in people" block is displayed.
        5. Within the "Strength in people" block, click on the "More Details" button and verify that
           the navigation leads to https://tensor.ru/about
        6. On the Tensor "About" page, locate the "Работаем" section.
        7. Check that all images within the chronology section in "Работаем" have the same height and width.

    **Expected Result:**
        - The navigation between SBIS and Tensor websites is successful.
        - The "Strength in people" block is correctly displayed on the Tensor homepage.
        - The "More Details" button in the "Strength in people" block correctly navigates to the "About" page.
        - All images in the chronology section on the "About" page have the same height and width.
    """
)
def test_script_one(browser):
    with allure.step("Open Sbis main page"):
        sbis_home = SbisHome(browser)
        sbis_home.go_to_site()

    with allure.step("Click on contacts button"):
        sbis_home.click_on_the_contacts()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="contacts_page_after_button",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Click on the contacts link"):
        sbis_home.click_on_the_link()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="contacts_page_after_link",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Click on tensor banner"):
        sbis_contact = SbisContact(browser)
        sbis_contact.click_on_the_tensor_banner()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="tensor_banner_after_click",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Open tensor main page"):
        tensor_home = TensorHome(browser)
        tensor_home.change_window()
        allure.attach(
            browser.get_screenshot_as_png(),
            name="tensor_home_page",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Check a strength in people block"):
        assert tensor_home.check_strength_in_people() == 1
        allure.attach(
            browser.get_screenshot_as_png(),
            name="strength_in_people_block",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Click on more details button"):
        tensor_home.click_more_details()

        assert tensor_home.get_current_url() == "https://tensor.ru/about"
        allure.attach(
            browser.get_screenshot_as_png(),
            name="tensor_home_after_more_details",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Assert same resolution of images"):

        tensor_about_page = TensorAboutPage(browser)
        assert tensor_about_page.check_same_resolution() == 1
        allure.attach(
            browser.get_screenshot_as_png(),
            name="about_page_with_images",
            attachment_type=allure.attachment_type.PNG,
        )


@allure.title("Verify Region and Partner List on SBIS Contacts Page")
@allure.feature("Regression tests")
@allure.description(
    """
    **Test Scenario:**

    This test verifies the functionality of the SBIS contacts page, focusing on region detection
    and the subsequent update of information after a region change.

    **Test Steps:**
        1. Navigate to the SBIS "Contacts" page.
        2. Verify that the correct initial region is detected (e.g., "Тюменская обл." when using VPN).
           Also, verify that the list of partners is displayed.
        3. Change the region to "Камчатский край".
        4. Verify that the selected region is correctly displayed, the list of partners has changed, 
           and the URL and title contain information about the new selected region. 
           Additionally, check that at least the first partner on the list contains information of the selected region (e.g. contains "Камчатка")

    **Expected Result:**
        - The initial region is correctly detected, and the list of partners is displayed.
        - After changing the region, the updated region, partner list, URL, and title
          reflect the newly selected region ("Камчатский край").
    """
)
def test_script_two(browser):
    with allure.step("Verify initial region and partner list"):
        sbis_contacts = SbisContact(browser)
        sbis_contacts.go_to_site()
        assert sbis_contacts.get_region() == "Тюменская обл."
        assert sbis_contacts.check_list_of_partners() == 1
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Contacts region check",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Checking info region update"):
        sbis_contacts.change_region()
        allure.description(
            "Check that the selected region has been .\
                substituted, the list of partners has changed, url and .\
                title contains information of the selected region"
        )

        assert ("41-kamchatskij-kraj" in browser.current_url) == 1
        assert sbis_contacts.get_region() == "Камчатский край"
        assert ("Камчатский край" in sbis_contacts.get_title()) == 1
        assert ("Камчатка" in sbis_contacts.get_first_partner_text()) == 1

        allure.attach(
            browser.get_screenshot_as_png(),
            name="Change region",
            attachment_type=allure.attachment_type.PNG,
        )


@allure.title("Verify the Size of Downloaded SBIS Plugin Web Installe")
@allure.feature("Regression tests")
@allure.description(
    """
    **Test Scenario:**.

    This test checks the download functionality of the SBIS Plugin for Windows web installer
    and verifies that the size of the downloaded file matches the size specified on the website.

    **Test steps:**
        1. Open the home page of the SBIS Web site (https://sbis.ru/).
        2. In the footer, find the “Download Local Versions” link and navigate to it.
        3. Download the SBIS Plugin for Windows web installer to the directory where this test is located.
        4. Verify that the plugin has successfully downloaded.
        5. Compare the size of the downloaded file in megabytes (MB) to the size specified on the website (e.g., 3.64 MB).

    **Expected Result:**.
        - The SBIS Plugin web installer has been successfully downloaded.
        - The size of the downloaded file in MB matches the size specified on the download page.
        - Test passed if all checks are successful.

    **Notes:**
        - If the size of the uploaded file does not match the size on the site, the test will fail.
    """
)
def test_script_three(browser):
    with allure.step("Open the main page of the SBIS website"):
        sbis_home = SbisHome(browser)
        sbis_home.go_to_site()

    with allure.step("Navigate to the 'Download local versions' link in the footer"):
        sbis_home.click_on_download_local_vers()

    with allure.step("Download the SBIS Plugin web installer for Windows"):
        sbis_download = SbisDownload(browser)
        sbis_download.click_on_the_download_web_installer_Win()

    with allure.step("Retrieve the text containing the file size information"):
        text_installer = sbis_download.get_text_web_installer_win()

    with allure.step("Verify that the downloaded file size matches the expected size"):
        file_path = "/home/ton1ps/Downloads/"  # Your path
        file_name = "sbisplugin-setup-web.exe"
        assert check_size_matching(text_installer, file_path, file_name) == 1
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Screenshot after size verification",
            attachment_type=allure.attachment_type.PNG,
        )
