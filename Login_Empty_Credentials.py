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

# Boundary Test Case - Login with Empty Credentials
def test_login_empty_credentials():
    # Clear any existing values and attempt login without entering credentials
    driver.find_element(By.ID, "user-name").send_keys("")  # Explicitly set username to empty
    driver.find_element(By.ID, "password").send_keys("")  # Explicitly set password to empty
    driver.find_element(By.ID, "login-button").click()  # Attempt login
    time.sleep(2)
    
    # Check for error message when both fields are empty
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username is required" in error_message, "Error message not displayed for empty username"

# Run the test
try:
    test_login_empty_credentials()
    print("Test Case 3: Login with Empty Credentials - Passed")
except AssertionError as e:
    print(f"Test Case 3: Login with Empty Credentials - Failed: {e}")

# Closing the browser
driver.quit()