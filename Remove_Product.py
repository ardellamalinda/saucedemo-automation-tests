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

# Test Case - Remove Product from Cart
def test_remove_product_from_cart():
    print("Starting test case for removing product from cart...")
    
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
        
        # Remove item from cart
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart_button"))).click()
        print("Item removed from cart.")
        
        # Verify that the cart is empty by checking if no items are present
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == 0, "Cart is not empty after removing the product."
        print("Product removal from cart verified successfully.")
    
    except Exception as e:
        print(f"Test Case 9: Remove Product from Cart - Failed: {e}")
        driver.save_screenshot("remove_product_screenshot.png")
        print("Screenshot saved as 'remove_product_screenshot.png'.")
        raise
    
# Run the test
try:
    test_remove_product_from_cart()
    print("Test Case 9: Remove Product from Cart - Passed")
except Exception as e:
    print(f"Test Case 9: Remove Product from Cart - Failed: {e}")
finally:
    driver.quit()