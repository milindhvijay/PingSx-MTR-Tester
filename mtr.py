import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    # Read server IDs and probe names from the CSV file
    with open("server_name.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        servers = list(reader)

    # Get the IP address to trace
    target_ip = input("Enter the IP address to trace: ")

    # Set up Chrome options and driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)

    for server in servers:
        # Get the server ID and probe name
        server_id = server['server_id']
        probe_name = server['probe_name']

        # Construct the URL for the MTR
        url = f"https://ping.sx/mtr?t={target_ip}&p={server_id}"

        # Load the MTR in the browser
        driver.get(url)

        # Wait for the target input field to be interactable before pressing Enter
        target_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'target')))
        target_input.send_keys(Keys.RETURN)

        # Wait for 15 seconds to let the page load completely
        time.sleep(15)

        # Get the current date and time in 24h format
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Take a screenshot of the full page and save it with a unique name
        file_name = f"{probe_name}_{target_ip}_{now}.png"
        file_path = f"path/to/{file_name}"
        driver.save_screenshot(file_path)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()
