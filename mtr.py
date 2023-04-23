import time
from datetime import datetime
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
    driver.maximize_window()
    driver.get(url)

    # Wait for the target input field to be interactable before pressing Enter
    target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'target')))
    target_input.send_keys(Keys.RETURN)

    # Wait for 15 seconds to let the page load completely
    time.sleep(15)

    # Get the probe name from the webpage
    probe_name = driver.find_element(By.CSS_SELECTOR, 'h3.ml-2.mt-2.text-sm.leading-6.font-normal.text-gray-900').text

    # Get the current date and time in the desired format
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    # Rename the screenshot file with the probe name and current date and time
    file_name = f"{probe_name}_{target_ip}_{current_time}.png"

    # Take a screenshot of the full page and save it to the specified location
    driver.save_screenshot(f"path/to/save/{file_name}")

    driver.quit()

if __name__ == "__main__":
    main()
