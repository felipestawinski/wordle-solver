from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from question_to_ai import QuestionToAI

import re
import sys
from time import sleep

try: 
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--reduce-security-for-testing')
    options.set_capability("acceptInsecureCerts", True)

    service = Service()
    service.creation_flags = 0x08000000  # Prevents command window from appearing

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(60)
    driver.get("https://www.nytimes.com/games/wordle/index.html")

    print(f"Title: {driver.title}")

    sleep(2)

    elem = driver.find_element(By.CLASS_NAME, "fides-accept-all-button")
    elem.click()
    sleep(1)
    elem = driver.find_element(By.CLASS_NAME, "purr-blocker-card__button")
    elem.click()
    sleep(1)
    elem = driver.find_element(By.XPATH, f'//button[@data-testid="Play"]')
    elem.click()
    sleep(1)
    elem = driver.find_element(By.CLASS_NAME, "game-icon")
    elem.click()
    sleep(1)
    # Locate the "Row 1" element

    actions = ActionChains(driver)
    actions.send_keys("STONE").perform()
    actions.send_keys(Keys.ENTER).perform()

    ai_client = QuestionToAI()


    #for i in range(5):

    # Keep the browser open until user presses Enter 
    input("Press Enter to close the browser...")

except WebDriverException as e:
    print(f"Error: {e}")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    sys.exit(1)