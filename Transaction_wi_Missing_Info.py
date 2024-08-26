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
wait = WebDriverWait(driver, 15)

# Navigate to the website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Test Case - Transaction with Missing Checkout Information
def test_transaction_missing_checkout_information():
    print("Starting test case for transaction with missing checkout information...")
    
    try:
        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        print("Logged in successfully.")
        
        # Add item to cart
        wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Item added to cart and navigating to cart.")
        
        # Proceed to checkout
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
        print("Proceeding to checkout.")
        
        # Fill out checkout information with one field left empty
        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ardella")
        driver.find_element(By.ID, "last-name").send_keys("")  # Leaving last name field empty
        driver.find_element(By.ID, "postal-code").send_keys("7890")
        driver.find_element(By.ID, "continue").click()
        print("Checkout information entered with one field left empty.")
        
        # Verify the error message for missing last name
        error_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container"))).text
        assert "Error: Last Name is required" in error_message, f"Expected error message not found: {error_message}"
        print("Error message displayed as expected.")
    
    except AssertionError as ae:
        print(f"Assertion error during test: {ae}")
        driver.save_screenshot("assertion_error_screenshot.png")
        print("Screenshot saved as 'assertion_error_screenshot.png'.")
        raise
    
    except Exception as e:
        print(f"Failed to handle missing checkout information: {e}")
        driver.save_screenshot("missing_info_screenshot.png")
        print("Screenshot saved as 'missing_info_screenshot.png'.")
        raise

# Run the test
try:
    test_transaction_missing_checkout_information()
    print("Test Case 7: Transaction with Missing Checkout Information - Passed")
except Exception as e:
    print(f"Test Case 7: Transaction with Missing Checkout Information - Failed: {e}")
finally:
    driver.quit()