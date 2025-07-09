from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import csv
import os
import time
import requests

# URL of the page to scrape
url = "https://www.myntra.com/earrings"

# Provide the correct path to GeckoDriver
service = Service("C:/Users/KIIT/Downloads/geckodriver-v0.36.0-win64/geckodriver.exe")

# Initialize the Firefox WebDriver
driver = webdriver.Firefox(service=service)

# Function to scrape earrings data
def scrape_earrings(url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Extract product details
    product_elements = driver.find_elements(By.CLASS_NAME, "product-base")
    
    product_titles = []
    product_prices = []
    product_images = []

    for product in product_elements:
        # Extract title
        try:
            title = product.find_element(By.CLASS_NAME, "product-brand").text
        except:
            title = "N/A"
        product_titles.append(title)

        # Extract price
        try:
            price = product.find_element(By.CLASS_NAME, "product-discountedPrice").text
        except:
            price = "N/A"
        product_prices.append(price)

        # Extract image URL
        try:
            image = product.find_element(By.TAG_NAME, "img").get_attribute("src")
        except:
            image = "N/A"
        product_images.append(image)

    # Save data to CSV
    save_to_csv(product_titles, product_prices, product_images)

    # Optionally download images
    download_images(product_images)

    print("Scraping completed!")

# Function to save data to CSV
def save_to_csv(titles, prices, images):
    with open('earrings_data_with_images.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Image URL"])
        for i in range(len(titles)):
            writer.writerow([titles[i], prices[i], images[i]])
    print("Data saved to earrings_data_with_images.csv")

# Function to download images
def download_images(image_urls):
    os.makedirs("earrings_images", exist_ok=True)
    for i, url in enumerate(image_urls):
        if url != "N/A":  # Skip invalid URLs
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(f"earrings_images/earring_{i + 1}.jpg", 'wb') as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    print(f"Downloaded image: earring_{i + 1}.jpg")
                else:
                    print(f"Failed to download image {i + 1}. Status code: {response.status_code}")
            except Exception as e:
                print(f"Error downloading image {i + 1}: {e}")

# Run the scraper
try:
    scrape_earrings(url)
finally:
    driver.quit()  # Ensure the browser closes after the script finishes
