import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    target_ip = input("Enter the IP address to trace: ")
    server_id = input("Enter the server ID: ")
    url = f"https://ping.sx/mtr?t={target_ip}&p={server_id}"

    chrome_options = Options()
    driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)
    driver.get(url)

    # Wait for the target input field to be interactable before pressing Enter
    target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'target')))
    target_input.send_keys(Keys.RETURN)

    # Keep the browser open for 30 seconds
    time.sleep(30)

    driver.quit()

if __name__ == "__main__":
    main()
