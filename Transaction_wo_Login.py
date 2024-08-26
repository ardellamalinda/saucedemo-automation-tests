from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome Driver path
chrome_driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10)  # Wait time for elements to load

# Negative Test Case - Transaction without Login
def test_transaction_without_login():
    print("Starting test case for transaction without login...")
    
    try:
        # Try to add item to the cart without logging in
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_to_cart_button.click()
        print("Item added to cart without login.")

        # Navigate to cart page
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        print("Navigated to cart page.")

        # Try to proceed to checkout without login
        wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()
        print("Attempting to checkout without login.")
        
        # Check if redirected to login page
        wait.until(EC.url_contains("login"))
        current_url = driver.current_url
        assert "login" in current_url, f"Expected to be on login page, but got {current_url}"

        print("Transaction not allowed without login - redirected to login page.")
    except Exception as e:
        print(f"Failed during test case: {str(e)}")
        driver.save_screenshot("screenshot_negative_test.png")
        print("Screenshot saved as 'screenshot_negative_test.png'.")

# Run the test
try:
    test_transaction_without_login()
    print("Test Case 5: Transaction without Login - Passed")
except AssertionError as e:
    print(f"Test Case 5: Transaction without Login - Failed: {e}")

# Closing the browser
driver.quit()