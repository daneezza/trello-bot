# import libraries
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Load environment variables from a .env file into the environment
load_dotenv()
url = os.getenv("BASE_URL")
email = os.getenv("EMAIL")
pwd = os.getenv("PASSWORD")

# Instantiate webdriver and open a Chrome browser
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

# maximize browser window
driver.maximize_window()

# Load the web page
driver.get(url)

# define a wait
wait = WebDriverWait(driver, 15)

# reusable wait wrapper
def wait_for_clickable(xpath):
    return wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

def wait_for_presence(xpath):
    return wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


try:
    # Enter login email
    login_email = wait_for_clickable('//*[@id="username"]')
    login_email.send_keys(email)
    sleep(2)

    # Click "Remember me"
    remember_me = wait_for_presence('//*[@id="form-login"]/div[1]/div[3]/div/label/input')
    remember_me.click()
    sleep(2)

    # Click "Continue" button
    continue_button = wait_for_clickable('//*[@id="login-submit"]')
    continue_button.click()
    sleep(2)

    # Enter password
    password = wait_for_clickable('//*[@id="password"]')
    password.send_keys(pwd)
    sleep(2)

    # Click final "Login" button
    login_button = wait_for_clickable('//*[@id="login-submit"]')
    login_button.click()
    sleep(10)

    # Wait until the board is present and scroll into view
    navigate_to_board = wait_for_presence('(//a[@title="Trello-Bot"])[1]')
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", navigate_to_board)
    sleep(3)

    # Click the desired board
    board_click = wait_for_clickable('(//a[@title="Trello-Bot"])[1]')
    board_click.click()
    sleep(10)

    # Click "Add a card" button
    click_add_card = wait_for_clickable('//*[@id="board"]/li[1]/div/div[3]/button[1]')
    click_add_card.click()
    sleep(3)

    # Enter card title
    add_card = wait_for_clickable('//textarea[@placeholder="Enter a title or paste a link"]')
    add_card.send_keys("This trello bot was made by daneezza")
    sleep(3)

    # Click "Add card" submit button
    submit_add_card = wait_for_clickable('//button[normalize-space()="Add card"]')
    submit_add_card.click()
    sleep(3)

    # Close the card input form
    close_button = wait_for_clickable('//button[@aria-label="Cancel"]')
    close_button.click()
    sleep(3)

except Exception as e:
    print(f"An Error Occurred: {e}")

finally:
    print("Trello Bot executed successfully!")
    print("Created by Daneesha Hansaka.")
    driver.quit()

