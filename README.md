# product_scrapper
# Myntra Earrings Scraper

This Python script scrapes earring product data from [Myntra](https://www.myntra.com/earrings) using Selenium WebDriver and saves the results to a CSV file. Optionally, it can also download product images.

## Features
- Scrapes product titles, prices, and image URLs from Myntra's earrings page
- Saves the extracted data to a CSV file
- Downloads product images to your local machine

## Requirements
- Python 3.7 or higher
- [Selenium](https://pypi.org/project/selenium/)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) (for Firefox)
- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [requests](https://pypi.org/project/requests/)

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install selenium requests
   ```

2. **Download GeckoDriver:**
   - Download the latest GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases).
   - Extract the executable and place it in your desired folder (e.g., `C:/Users/KIIT/Downloads/geckodriver-v0.36.0-win64/`).

3. **Ensure Firefox is installed:**
   - Download and install Firefox if it is not already installed.

4. **Update the script:**
   - Make sure the `service = Service(...)` line in the script points to the correct GeckoDriver path.

## Usage

1. Place the script (`scrape (2).py`) in your working directory.
2. Open a terminal (PowerShell or CMD) and navigate to the script's directory.
3. Run the script:
   ```bash
   python "scrape (2).py"
   ```
4. The script will scrape the data and save it to a CSV file. Images (if enabled) will be downloaded to a folder.

## Notes
- The script uses Selenium WebDriver to automate Firefox. Ensure no other instances of Firefox are interfering.
- If you encounter errors related to GeckoDriver or Firefox, check the paths and compatibility.
- Website structure changes may break the scraper; update class names/selectors as needed.

## License
This project is for educational purposes only.
