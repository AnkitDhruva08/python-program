from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Initialize the web driver
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# Uncomment the next line for debugging
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

# URL of the artist's page
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"

try:
    driver.get(url)

    # Debug: Print the page title
    print("Page title:", driver.title)

    # TEMPORARILY SKIPPING LANGUAGE SELECTION
    # Wait for the page to load fully
    time.sleep(5)  # Increase wait time for testing

    # Scroll and click "Load More" until all songs are loaded
    while True:
        try:
            load_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Load more')]"))
            )
            load_more_button.click()
            time.sleep(2)  # Allow time for content to load
        except:
            print("No more 'Load more' button found.")
            break

    # Parse the page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find all song containers
    song_elements = soup.find_all('div', class_='c-drag')  # Adjust based on actual class names
    print(f"Found {len(song_elements)} songs.")

    # Initialize counter for "Aditya Music"
    aditya_music_count = 0

    # Visit each song page to scrape copyright information
    for song_element in song_elements:
        song_link = song_element.get('href')
        if not song_link:
            continue
        song_link = "https://www.jiosaavn.com" + song_link

        driver.get(song_link)
        time.sleep(2)  # Wait for the page to load
        song_soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Locate copyright information
        copyright_info = song_soup.find('div', {'class': 'footer-copyright'})
        if copyright_info and 'Aditya Music' in copyright_info.text:
            aditya_music_count += 1

    # Output the total count of songs under "Aditya Music"
    print("Total songs with 'Aditya Music':", aditya_music_count)

finally:
    driver.quit()
