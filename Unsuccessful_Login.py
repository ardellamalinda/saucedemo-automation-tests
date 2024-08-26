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

# Negative Test Case - Unsuccessful Login with Invalid Credentials
def test_unsuccessful_login_invalid_credentials():
    driver.find_element(By.ID, "user-name").send_keys("invalid_user")  # Input invalid username
    driver.find_element(By.ID, "password").send_keys("secret_sauce")  # Input valid password
    driver.find_element(By.ID, "login-button").click()  # Click login button
    time.sleep(2)
    
    # Check for error message
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message, "Error message not displayed for invalid credentials"

# Run the test
try:
    test_unsuccessful_login_invalid_credentials()
    print("Test Case 2: Unsuccessful Login with Invalid Credentials - Passed")
except AssertionError as e:
    print(f"Test Case 2: Unsuccessful Login with Invalid Credentials - Failed: {e}")

# Closing the browser
driver.quit()