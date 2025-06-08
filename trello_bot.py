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
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# maximize browser window
driver.maximize_window()

# Load the web page
driver.get(url)

# define a wait
wait = WebDriverWait(driver, 15)

# enter login mail
login_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="username"]')))
login_email.send_keys(email)
sleep(2)

# remember me tick
remember_me = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="form-login"]/div[1]/div[3]/div/label/input')))
remember_me.click()
sleep(2)

# continue button
continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-submit"]')))
continue_button.click()
sleep(2)

# enter password
password = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
password.send_keys(pwd)
sleep(2)

# login button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-submit"]')))
login_button.click()
sleep(10)

# Wait until the board item is present
navigate_to_board = wait.until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]/a/div/div[1]/div'
)))

# Scroll it into view
driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", navigate_to_board)
sleep(3)  # optional slight delay after scroll

# Navigating to the desired board
navigate_to_board = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div/div/div/div/div/div[3]/div[1]/div[2]/div[1]')))
navigate_to_board.click()
sleep(10)

# click add card button
click_add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/div[3]/button[1]')))
click_add_card.click()
sleep(3)

# add a card
add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/ol/li[3]/form/textarea')))
add_card.send_keys("This trello bot was made by daneezza")
sleep(3)

# submit add card button
submit_add_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="board"]/li[1]/div/ol/li[3]/form/div/button[1]')))
submit_add_card.click()
sleep(3)

# close button
close_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="board"]/li[1]/div/ol/li[4]/form/div/button[2]/span/span')))
close_button.click()
sleep(3)

driver.quit()
