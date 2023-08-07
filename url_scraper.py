import requests
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import pandas as pd
import argparse
from tqdm import tqdm  # Import tqdm for the progress bar

columns = ["Title", "URL"]

def get_fiction_details(row, driver):
    contents = {}
    # Get the title of the fiction
    h2_element = row.find_element(By.TAG_NAME, "h2")
    title = h2_element.find_element(By.TAG_NAME, "a").text
    contents["Title"] = title
    # Get the URL of the fiction
    url = h2_element.find_element(By.TAG_NAME, "a").get_attribute("href")
    contents["URL"] = url
    print(f"URL: {url}")  # Add this print statement
    contents["URL"] = url

    return contents

def main():
    webdriver_path = r"C:\Users\mmdip\Downloads\Compressed\chromedriver_win32\new2\chromedriver.exe"
    fiction_data = []

    page_id = 2498
    count = 0

    last_page_number = 0  # Initialize last_page_number variable

    service = webdriver.chrome.service.Service(webdriver_path)
    service.start()
    driver = webdriver.Chrome(executable_path=service.service_url)

    try:
        while count < 57720:  # Limiting to 100 collections for now, you can adjust as needed
            url = f"https://www.royalroad.com/fictions/best-rated?page={page_id}"
            driver.get(url)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fiction-list")))
            item_id = driver.find_element(By.CLASS_NAME, "fiction-list")
            fictions = item_id.find_elements(By.CLASS_NAME, "fiction-list-item")

            for fiction in tqdm(fictions):  # Use tqdm to show the progress bar
                fiction_details = get_fiction_details(fiction, driver)
                fiction_data.append(fiction_details)
                count += 1
                print(f"Record {count}: {fiction_details['Title']}")

            last_page_number = page_id  # Update last_page_number to the current page_id
            page_id += 1
            time.sleep(2)  # Adding a short delay to avoid overwhelming the website

    except Exception as e:
        print(f"An error occurred during scraping: {e}")

    finally:
        # Close the webdriver
        driver.quit()

        # Create a Pandas DataFrame to store the scraped data
        df = pd.DataFrame(fiction_data, columns=columns)

        # Save the DataFrame to a CSV file along with the last page number
        df.to_csv("fiction_data_2498.csv", index=False)
        with open("last_page_number.txt", "w") as file:
            file.write(str(last_page_number))

if __name__ == "__main__":
    main()