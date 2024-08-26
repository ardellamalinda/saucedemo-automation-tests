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

# Positive Test Case - Logout Functionality
def test_logout_functionality():
    print("Starting test case for logout functionality...")
    
    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    print("Logged in successfully.")
    
    # Navigate to the menu and log out
    wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    print("Logging out...")
    
    # Check if logout is successful
    try:
        time.sleep(2)  # Ensure page has fully loaded
        assert "https://www.saucedemo.com/" in driver.current_url, "Failed to log out, not on login page"
        print("Logout successful, redirected to login page.")
    except AssertionError as e:
        print(f"Failed to log out: {e}")
        driver.save_screenshot("logout_screenshot.png")
        print("Screenshot saved as 'logout_screenshot.png'.")
        raise

# Run the test
try:
    test_logout_functionality()
    print("Test Case 6: Logout Functionality - Passed")
except AssertionError as e:
    print(f"Test Case 6: Logout Functionality - Failed: {e}")
finally:
    driver.quit()