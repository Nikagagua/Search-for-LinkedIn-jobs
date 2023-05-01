import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv('.env')
ACCOUNT_EMAIL = os.getenv('USERNAME')
ACCOUNT_PASSWORD = os.getenv('PASSWORD')
PHONE = os.getenv("PHONE_NUMBER")
JOB_SEARCH_URL = os.getenv("jobs_search_url")

chrome_driver_path = os.getenv('CHROME_DRIVER_PATH')
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(JOB_SEARCH_URL)
time.sleep(2)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(5)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(By.CLASS_NAME, 'fb-single-line-text__input')
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, 'footer button')
        if submit_button.get_attribute('data-control-name') == 'continue_unify':
            close_button = driver.find_element(By.CSS_SELECTOR, 'artdeco-model__dismiss')
            close_button.click()
            time.sleep(2)

            discard_button = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
            close_button.click()
    except NoSuchElementException as e:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
