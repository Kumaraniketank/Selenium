# Selenium
automation and Validation
README file for the saucedemo_test project:-
This project automates various tasks on the SauceDemo website (https://www.saucedemo.com/). 
The tasks include logging in, adding/removing items to/from the cart, completing a checkout 
process, and logging out. This project is built using Python and Selenium WebDriver.
Prerequisites
1. Python 3.x
2. Selenium 4.x
3. WebDriver for your browser (e.g., ChromeDriver for Google Chrome)
Installation
1. Install Python
Make sure Python 3.x is installed. You can download it from 
[here](https://www.python.org/downloads/).
2. Install Selenium
Install the Selenium package using `pip`:
pip install selenium
Download WebDriver
For Chrome:
• Download ChromeDriver compatible with your version of Google Chrome.
• Add the chromedriver executable to your system's PATH or specify its path in the script.
For Firefox:
• Download geckodriver.
• Add geckodriver to your system's PATH or specify its path in the script.
Usage
1. Modify the WebDriver path (if needed): In the script saucedemo_test.py, update the 
WebDriver initialization if you're not using Chrome. For example, for Firefox, you can use:
 driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
 2.Run the script: Execute the Python script in your terminal or IDE
 python saucedemo_test.py
 3.Expected Outcomes:
• Successful login with valid credentials and redirection to the inventory page.
• Error message displayed for invalid credentials.
• Items are added and removed from the cart.
• Checkout process is completed, and the total amount is printed.
• After finishing the checkout, the success message "Thank you for your order!" is displayed.
• Logout is successful, and the page redirects to the login screen.
Tasks Automated
1. Login Validation:
o Valid Credentials: Successful login and redirection to /inventory.html.
o Invalid Credentials: Error message "Epic sadface: Username and password do not 
match any user in this service.".
2. Add Items to Cart from Inventory Page:
o Filter items by price (low to high).
o Add two items to the cart and verify the cart count.
3. Add Items to Cart from Inventory Item Page:
o Add an item from the product details page.
o Verify the cart count.
4. Remove Items from Cart:
o Remove an item priced between $8 and $10 and verify the cart count.
5. Checkout Workflow:
o Complete the checkout process, verify items, and print the total amount.
o Finish the purchase and verify the success message.
6. Logout Functionality:
o Click the menu icon and select "Logout."
o Verify redirection to the login page.
Assumptions
1. Credentials:
o The credentials provided in the task (standard_user and secret_sauce) are valid and 
working on the SauceDemo website.
o The invalid credentials (invalid_user and wrong_password) consistently trigger the 
specified error message.
2. Website Stability:
o The SauceDemo website structure (IDs, classes, URLs, etc.) remains consistent during 
automation testing.
o The internet connection is stable to avoid timeouts or failures due to slow page 
loading.
3. Item Names and Prices:
o Product names like "Sauce Labs Backpack" and "Sauce Labs Bike Light" exist and are 
correctly displayed on the inventory page.
o The item price ranges are accurate, particularly the one priced between $8 and $10.
4. Cart Behavior:
o Items added to the cart persist across page navigations unless explicitly removed.
o The cart icon updates correctly to reflect the number of items in the cart.
5. Checkout Process:
o The checkout form accepts any non-empty values for First Name, Last Name, and 
Postal Code.
o The total amount displayed at the checkout overview is correct and reflects the sum 
of the items and taxes.
6. Environment:
o The automation script runs on a machine with a compatible browser and WebDriver 
installed and configured correctly.
Observations
1. Dynamic Element Loading:
o Some elements, such as the cart count badge, load dynamically, requiring careful 
synchronization using time.sleep or WebDriverWait.
2. Error Handling:
o The error message for invalid login credentials ("Epic sadface: Username and 
password do not match any user in this service.") is clearly displayed and easy to 
validate.
3. Filter Functionality:
o The filter dropdown (Price (low to high)) updates the product list as expected, 
simplifying the selection process.
4. Cart Management:
o Adding and removing items from the cart updates the cart icon badge correctly.
o After removing an item, the remaining items persist in the cart without issues.
5. Product Details Navigation:
o Clicking on a product name navigates to its details page without unexpected 
behaviors.
o Adding items to the cart from the product details page works as expected.
6. Success Message:
o The checkout success message ("Thank you for your order!") is prominently 
displayed after completing a purchase.
7. Logout:
o The logout functionality reliably redirects to the login page.
8. Potential Flaky Behavior:
o If the internet connection or server response is slow, elements like the inventory 
page or checkout button may not load immediately, causing test failures.
Notes
• Ensure the WebDriver is properly configured for your browser.
• Adjust the time.sleep values if the script is not synchronized well on your machine. You can 
also use WebDriverWait for better synchronization
