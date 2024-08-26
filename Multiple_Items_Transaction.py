from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome Driver path
chrome_driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 15)  # Increase timeout if needed

def test_transaction_with_multiple_items():
    print("Starting test case for transaction with multiple items...")
    
    # Navigate to the website
    driver.get("https://www.saucedemo.com/")
    
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Logged in successfully.")
    
    # Add multiple items to cart
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
    print("Multiple items added to cart.")
    
    # Navigate to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    print("Navigating to cart.")
    
    # Proceed to checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    print("Proceeding to checkout.")
    
    # Fill out checkout information
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    print("Checkout information entered.")
    
    # Complete the purchase
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
    print("Completing the purchase.")
    
    # Check if the transaction is completed
    try:
        time.sleep(5)  # Additional sleep to ensure the page has fully loaded
        
        # Verify URL to ensure we are on the completion page
        current_url = driver.current_url
        assert current_url == "https://www.saucedemo.com/checkout-complete.html", f"Not on the checkout complete page, current URL: {current_url}"
        
        # Check for the presence of confirmation message
        confirmation_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))).text
        print(f"Confirmation message found: {confirmation_message}")
        assert "THANK YOU FOR YOUR ORDER" in confirmation_message.upper(), "Transaction was not completed successfully"
        print("Transaction with multiple items completed successfully.")
        
    except AssertionError as e:
        print(f"Failed to complete transaction: {e}")
        driver.save_screenshot("multiple_items_transaction_screenshot.png")  # Save screenshot for debugging
        print("Screenshot saved as 'multiple_items_transaction_screenshot.png'.")
        raise  # Reraise exception to mark test as failed

# Run the test
try:
    test_transaction_with_multiple_items()
    print("Test Case 5: Transaction with Multiple Items - Passed")
except AssertionError as e:
    print(f"Test Case 5: Transaction with Multiple Items - Failed: {e}")
finally:
    # Closing the browser
    driver.quit()