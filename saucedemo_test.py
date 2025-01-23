from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  #browser's WebDriver
driver.maximize_window() #full screen view
driver.implicitly_wait(5)  # Implicit wait for elements to be available
def wait_for_element(selector, by=By.CSS_SELECTOR):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, selector)))


#Task-1

def login(username, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password + Keys.RETURN)
    
    try:
        if username == "standard_user":
            WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
            print("Login successful: Redirected to inventory page.")
        else:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container")))
            error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
            assert error_message == "Epic sadface: Username and password do not match any user in this service."
            print("Login failed as expected.")
    except Exception as e:
        print(f"Error during login validation: {e}")


#Task-2

def add_items_to_cart():
    driver.find_element(By.CLASS_NAME, "product_sort_container").click()
    driver.find_element(By.XPATH, "//option[text()='Price (low to high)']").click()
    
    items = driver.find_elements(By.CLASS_NAME, "btn_primary")
    items[1].click()  # Add "Sauce Labs Bike Light"
    items[4].click()  # Add "Sauce Labs Backpack"
    
    
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "2"
    print("Two items added to cart successfully.")



#Task-3

def add_item_from_detail_page():
    driver.find_element(By.LINK_TEXT, "Sauce Labs Onesie").click()
    driver.find_element(By.CLASS_NAME, "btn_primary").click()
    
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_count == "3"
    print("Added Sauce Labs Onesie from detail page.")


#Task-4

def remove_item_from_cart():
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()  # Go to cart page
    wait_for_element(".cart_item")
    
    # Remove item with price between $8 and $10
    item_price = float(driver.find_element(By.CSS_SELECTOR, ".cart_item .inventory_item_price").text[1:])
    if 8 <= item_price <= 10:
        driver.find_element(By.CSS_SELECTOR, ".cart_button").click()  # Click remove button
    
    # Verify cart count
    wait_for_element(".shopping_cart_badge")
    cart_count = int(driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text)
    assert cart_count == 2, f"Expected 2 items in cart, found {cart_count}"


#Task-5

def checkout():
    driver.find_element(By.CSS_SELECTOR, ".checkout_button").click()  # Click checkout
    wait_for_element("input[name='firstName']")
    
    # Fill out checkout form
    driver.find_element(By.NAME, "firstName").send_keys("Kumar")
    driver.find_element(By.NAME, "lastName").send_keys("Aniket")
    driver.find_element(By.NAME, "postalCode").send_keys("463231")
    driver.find_element(By.CSS_SELECTOR, ".cart_button").click()  # Click continue
    
    # Verify checkout overview
    wait_for_element(".cart_item")
    total_amount = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    print("Total amount:", total_amount)
    
    # Complete the purchase
    driver.find_element(By.CSS_SELECTOR, ".cart_button").click()  # Finish button
    
    # Verify success message
    wait_for_element(".complete-header")
    success_message = driver.find_element(By.CSS_SELECTOR, ".complete-header").text
    assert success_message == "Thank you for your order!", f"Expected success message, but found {success_message}"


#Task-6

def logout():
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    driver.find_element(By.ID, "logout_sidebar_link").click()
    current_url = driver.current_url
    assert current_url == "https://www.saucedemo.com/"
    print("Logout successful: Redirected to login page.")


# Execute all tasks

try:
    login("standard_user", "secret_sauce")
    add_items_to_cart()
    add_item_from_detail_page()
    remove_item_from_cart()
    checkout()
    logout()
    
finally:
    time.sleep(3) #sleep for 3 sec
    driver.quit()  # Close the browser