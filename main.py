from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome browser
driver = webdriver.Chrome()  # Add `executable_path='your/path'` if needed

try:
    # Step 1: Open the login page
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)

    # Step 2: Enter credentials
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # Step 3: Submit login form
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Step 4: Capture login success message
    flash = driver.find_element(By.ID, "flash").text
    print("Login message:", flash)

finally:
    driver.quit()
