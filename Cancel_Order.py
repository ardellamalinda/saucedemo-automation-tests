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

# Test Case - Cancel Order
def test_cancel_order():
    print("Starting test case for cancel order...")
    
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
    
    # Fill out checkout information
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("Ardella")
    driver.find_element(By.ID, "last-name").send_keys("Sarastri")
    driver.find_element(By.ID, "postal-code").send_keys("7890")
    driver.find_element(By.ID, "continue").click()
    print("Checkout information entered.")
    
    # Cancel the order
    wait.until(EC.element_to_be_clickable((By.ID, "cancel"))).click()
    print("Order cancelled.")
    
    # Verify that we are back on the products page
    current_url = driver.current_url
    assert "inventory.html" in current_url, f"Expected URL to be inventory page, but got {current_url}"
    print("Order cancellation verified successfully.")
    
# Run the test
try:
    test_cancel_order()
    print("Test Case 8: Cancel Order - Passed")
except Exception as e:
    print(f"Test Case 8: Cancel Order - Failed: {e}")
    driver.save_screenshot("cancel_order_screenshot.png")
    print("Screenshot saved as 'cancel_order_screenshot.png'.")
finally:
    driver.quit()