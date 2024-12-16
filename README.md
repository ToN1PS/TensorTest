# Automated UI Tests for SBIS and Tensor Websites

This project implements automated UI tests for the SBIS and Tensor websites as part of a test assignment for a Test Automation Engineer position.

## Project Overview

This project uses Python 3, Selenium WebDriver, and pytest to automate the testing of two mandatory scenarios and one optional scenario. The Page Object pattern has been implemented to organize test code and make it more maintainable. All code is available on GitHub/GitLab.

## Requirements

*   **Python 3.13**
*   **Selenium WebDriver**
*   **pytest**
*   **Allure Framework**
    * `allure-pytest==2.13.5`
    * `allure-python-commons==2.13.5`
*  **Other Libraries:**
   * `attrs==24.2.0`
   * `certifi==2024.12.14`
   * `h11==0.14.0`
   * `idna==3.10`
   * `iniconfig==2.0.0`
   * `outcome==1.3.0.post0`
   * `packaging==24.2`
   * `pluggy==1.5.0`
   * `PySocks==1.7.1`
   * `selenium==4.27.1`
   * `sniffio==1.3.1`
   * `sortedcontainers==2.4.0`
   * `trio==0.27.0`
   * `trio-websocket==0.11.1`
   * `typing_extensions==4.12.2`
   * `urllib3==2.2.3`
   * `websocket-client==1.8.0`
   * `wsproto==1.2.0`


## Getting Started

1. Clone the repository

Clone the project repository from GitHub/GitLab to your local machine.

   ```bash
   git clone <repository_url>
   ```

2. Install Dependencies

Install the required dependencies using pip.

```bash 
pip install -r requirements.txt
```

3. Run the tests

Run the tests using pytest.

```bash 
pytest test.py --alluredir=allure-results
```

5. View the test report

After run the tests you can view generated allure report with:

 ```bash 
allure serve allure-results
```

## Test Scenarios
This project automates the following scenarios:

Mandatory Scenarios:
#### Scenario 1: Navigation between SBIS and Tensor Websites
1. Navigate to the SBIS website (https://sbis.ru/) and open the “Contacts” section.
2. Locate the Tensor banner on the contacts page and click it.
3. Navigate to the Tensor website (https://tensor.ru/) which will open in a new tab.
4. On the Tensor homepage, verify that the “Strength in people” block is displayed.
5. Within the “Strength in people” block, click on the “More Details” button and verify that the navigation leads to https://tensor.ru/about.
6. On the Tensor “About” page, locate the “We work” section and check that all images within the chronology section in “We work” have the same height and width.

#### Scenario 2: SBIS Region and Partner List Verification
1. Navigate to the SBIS website (https://sbis.ru/) and open the “Contacts” section.
2. Verify that the correct initial region is detected and that a list of partners is displayed.
3. Change the region to “Камчатский край”.
4. Verify that the selected region is correctly displayed, the list of partners has changed, and the URL and title contain information about the new selected region.

#### Scenario 3: SBIS Plugin Download Verification
1. Navigate to the SBIS website (https://sbis.ru/).
2. In the footer, locate and navigate to the “Download local versions” link.
3. Download the SBIS Plugin web installer for Windows to the directory where the test is located.
4. Verify that the plugin has been downloaded successfully.
5. Compare the downloaded file size in megabytes (MB) with the size specified on the website (example 3.64 MB).