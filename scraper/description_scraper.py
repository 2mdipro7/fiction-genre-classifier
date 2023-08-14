import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import requests
from PIL import Image
import io
from sklearn.cluster import KMeans
import numpy as np
from tqdm import tqdm

# Function to perform K-means clustering for color analysis
def perform_kmeans_clustering(image, num_colors=5):
    # Convert image to RGB mode (if not already)
    if image.mode != "RGB":
        image = image.convert("RGB")
    
    # Convert image to NumPy array
    image_array = np.array(image)
    height, width, _ = image_array.shape

    # Reshape the array to a list of RGB pixels
    pixel_data = image_array.reshape(-1, 3)

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)  # Set n_init explicitly
    kmeans.fit(pixel_data)

    # Get the cluster centers (representative colors)
    cluster_centers = kmeans.cluster_centers_.astype(int)

    # Convert cluster centers to hexadecimal color strings
    color_info = ['#%02x%02x%02x' % tuple(color) for color in cluster_centers]

    return color_info

# Function to extract tags, descriptions, and cover image URL from a given URL
def get_tags_description_and_cover_url(url, driver):
    tags = []
    description = ""
    cover_url = ""
    color_info = []

    driver.get(url)

    try:

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='showTags']")))
        button = driver.find_element(By.CSS_SELECTOR, "label[for='showTags']")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='showTags']"))).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tags")))
        tags_element = driver.find_element(By.CLASS_NAME, "tags")
        tags = [tag.text for tag in tags_element.find_elements(By.TAG_NAME, "a")]

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "description")))
        description_element = driver.find_element(By.CLASS_NAME, "description")
        description = description_element.text.strip()

        cover_element = driver.find_element(By.XPATH, "//img[@data-type='cover']")
        cover_url = cover_element.get_attribute("src")

        # Download the cover image
        response = requests.get(cover_url)
        image_data = io.BytesIO(response.content)
        image = Image.open(image_data)

        # Perform color analysis using K-means clustering
        color_info = perform_kmeans_clustering(image, num_colors=5)

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Error occurred while fetching data for {url}: {e}")

    return tags, description, cover_url, color_info

def main():
    try:
        webdriver_path = r"C:\Users\mmdip\Downloads\Compressed\chromedriver_win32\new2\chromedriver.exe"
        
        # Load the previous CSV file with URLs, titles, and other data (if any) from the previous scraping
        df_previous = pd.read_csv("fiction_data.csv")
        urls = df_previous["URL"]
        titles = df_previous["Title"]

        # Initialize the webdriver
        service = webdriver.chrome.service.Service(webdriver_path)
        service.start()
        driver = webdriver.Chrome(executable_path=service.service_url)

        all_tags = []
        all_descriptions = []
        all_cover_urls = []
        all_color_info = []  # List to store color information

        
         # Read the last scraped record number from the "last_scraped_record.txt" file
        try:
            with open("tracker/last_scraped_record.txt", "r") as file:
                last_scraped_record = int(file.read())
        except FileNotFoundError:
            last_scraped_record = 0

        for id, url in tqdm(enumerate(urls[last_scraped_record:]), total=len(urls) - last_scraped_record, desc="Scraping Progress"):
            # Increment the index by last_scraped_record to get the actual index in the original list
            actual_index = id + last_scraped_record

            tags, description, cover_url, color_info = get_tags_description_and_cover_url(url, driver)
            all_tags.append(tags)
            all_descriptions.append(description)
            all_cover_urls.append(cover_url)
            all_color_info.append(color_info)  # Append color information
            time.sleep(2)  # Adding a short delay to avoid overwhelming the website

            # Print the progress, title, tags, and description
            print(f"Processed {actual_index + 1} of {len(urls)} URLs. Title: {titles[actual_index]}")
            print(f"Tags: {tags}")
            print(f"Description: {description}")
            print(f"Cover URL: {cover_url}")
            print(f"Color Info: {color_info}")  # Print color information
            print("-" * 30)

    except Exception as e:
        print(f"An error occurred during scraping: {e}")

    finally:
        # Close the webdriver
        driver.quit()

        # Create a new DataFrame to store the data
        data = {
            "Title": [],
            "Tags": [],
            "Description": [],
            "Cover_URL": [],
            "Color Info": []
        }

        for i, title in enumerate(titles):
            if i < len(all_tags) and i < len(all_descriptions) and i < len(all_cover_urls) and i < len(all_color_info):
                data["Title"].append(title)
                data["Tags"].append(all_tags[i])
                data["Description"].append(all_descriptions[i])
                data["Cover_URL"].append(all_cover_urls[i])
                data["Color Info"].append(all_color_info[i])

        df_new = pd.DataFrame(data)

        # Save the updated DataFrame to a new CSV file
        df_new.to_csv("fiction_data_with_tags_and_cover_url2.csv", index=False)

        # Save the last scraped record number to a txt file
        with open("tracker/last_scraped_record.txt", "w") as file:
            file.write(str(id + 1))

if __name__ == "__main__":
    main()
