from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Setup Chrome Driver path
chrome_driver_path = 'C:\\Users\\user\\Downloads\\chromedriver-win64\\chromedriver.exe'
service = Service(executable_path=chrome_driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Positive Test Case - Successful Login
def test_successful_login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    # Check if login is successful
    assert "inventory.html" in driver.current_url, "Failed to login with valid credentials"

# Run the test
try:
    test_successful_login()
    print("Test Case 1: Successful Login - Passed")
except AssertionError as e:
    print(f"Test Case 1: Successful Login - Failed: {e}")

# Closing the browser
driver.quit()