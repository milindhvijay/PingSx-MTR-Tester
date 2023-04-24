import time
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor

def run_mtr(server_id, probe_name, target_ip):
    # Construct the URL for the MTR
    url = f"https://ping.sx/mtr?t={target_ip}&p={server_id}"

    # Set up Chrome options and driver
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(executable_path="path/to/chromedriver", options=chrome_options)

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

def main():
    # Read server IDs and probe names from the CSV file
    with open("server_name.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        servers = list(reader)

    # Get the IP address to trace
    target_ip = input("Enter the IP address to trace: ")

     # Get the number of windows to run MTR tests
    num_windows = int(input("Enter the number of windows to run MTR tests simultaneously: "))

    # Split the servers into batches of num_windows
    batches = [servers[i:i+num_windows] for i in range(0, len(servers), num_windows)]

    for batch in batches:
        # Launch num_windows threads to run the MTR for each server in the batch
        with ThreadPoolExecutor(max_workers=num_windows) as executor:
            for server in batch:
                server_id = server['server_id']
                probe_name = server['probe_name']
                executor.submit(run_mtr, server_id, probe_name, target_ip)

    print("MTR tests complete")

if __name__ == "__main__":
    main()