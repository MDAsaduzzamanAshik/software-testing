from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()  
driver.maximize_window()

try:
    # Open the website
    driver.get("https://thinking-tester-contact-list.herokuapp.com/addUser")

    # Wait for the elements to be present and interact with them
    wait = WebDriverWait(driver, 20)
    first_name = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
    first_name.send_keys("Asaduzzaman")

    last_name = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
    last_name.send_keys("Ashik")

    email = wait.until(EC.presence_of_element_located((By.ID, "email")))
    email.send_keys("ashik@example.com")

    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("password123")

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()

    # Wait for a few seconds to see the result
    time.sleep(5)

    # Print success message
    print("User added successfully!")

except Exception as e:
    print("An error occurred:", e)
    print("Page source for debugging:\n", driver.page_source)

finally:
    # Close the WebDriver
    driver.quit()
