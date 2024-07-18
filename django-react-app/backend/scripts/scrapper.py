from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

def scrape_data():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    fighter_data = []

    # Loop through each character from 'a' to 'z'
    for char in 'abcdefghijklmnopqrstuvwxyz':
        driver.get(f'http://www.ufcstats.com/statistics/fighters?char={char}&page=all')

        # Wait for the page to load
        time.sleep(5)

        rows = driver.find_elements(By.CSS_SELECTOR, 'tr.b-statistics__table-row')  # Get all table rows
        for row in rows[1:]:  # Skip the header row
            try:
                first_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(1) a').text
                last_name = row.find_element(By.CSS_SELECTOR, 'td:nth-child(2) a').text
                try:
                    nickname = row.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
                except:
                    nickname = ''  # Assign a blank space if nickname is not found
                fighter_data.append({
                    'First Name': first_name,
                    'Last Name': last_name,
                    'Nickname': nickname
                })
            except Exception as e:
                print(f"Error occurred: {e}")  # Debugging line to print the error

    # Close the browser
    driver.quit()

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(fighter_data)
    df.to_excel('fighter_data.xlsx', index=False)

    print("Data saved to fighter_data.xlsx")

if __name__ == '__main__':
    scrape_data()
