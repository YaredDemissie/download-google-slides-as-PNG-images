from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv
import os
import time

# Loads environmental variables
load_dotenv(find_dotenv())

# Initialize Chrome options
opts = Options()
opts.add_experimental_option("debuggerAddress", "localhost:9250")

# Chrome Driver setup
driver = webdriver.Chrome(os.getenv('CHROME_DRIVER_PATH'), options=opts)

# Open Google Slides link
driver.get(os.getenv('GOOGLE_SLIDES_URL'))

# create action chain object
action = ActionChains(driver)

def download_PNG_image():
    # Open the File menu (Alt + Shift + f)
    time.sleep(5)
    action.key_down(Keys.ALT).key_down(Keys.SHIFT).key_down('f').key_up(Keys.ALT).key_up(Keys.SHIFT).key_up('f').perform()

    # In the File menu, move the selector to Download
    time.sleep(5)
    for i in range(7):
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        
    # Move right to select the options in Download
    time.sleep(5)
    action.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()

    # In the Download menu, move the selector to PNG image
    time.sleep(5)
    for i in range(5):
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()

    # Select PNG image
    time.sleep(5)
    action.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

# Variable to save the previous URL because moving to the next slide 
# changes the current URL. If placeholder_url is equal to current_url,
# it means the program has reached the last slide
placeholder_url = "placeholder"

# Convert slide to PNG and keep moving to the next slide until 
# reaching the last slide (placeholder_url == driver.current_url)
while placeholder_url != driver.current_url:
    placeholder_url = driver.current_url
    time.sleep(5)
    download_PNG_image()
    time.sleep(5)
    action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()

driver.quit()