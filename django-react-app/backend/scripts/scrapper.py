# This script scrapes the UFC Stats website to extract fighter data and save it to an Excel file. The script uses the Selenium WebDriver to interact with the website and extract the necessary information.
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time as pytime

# def scrape_data():
#     # Set up the Selenium WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#     fighter_data = []

#     try:
#         # Only process the first 5 fighters starting with 'a'
#         driver.get(f'http://www.ufcstats.com/statistics/fighters?char=a&page=all')

#         # Wait for the page to load
#         pytime.sleep(5)

#         # Scrape fighter data
#         rows = driver.find_elements(By.CLASS_NAME, 'b-statistics__table-row')
#         for row in rows[1:6]:  # Limit to first 5 fighters (1:6 means skipping the header row)
#             try:
#                 first_name = row.find_element(By.XPATH, './td[1]/a').text
#                 last_name = row.find_element(By.XPATH, './td[2]/a').text
#                 try:
#                     nickname = row.find_element(By.XPATH, './td[3]').text
#                 except:
#                     nickname = ''  # Assign a blank space if nickname is not found

#                 # Navigate to fighter's detail page
#                 detail_url = row.find_element(By.XPATH, './td[1]/a').get_attribute('href')
#                 print(f"Navigating to URL: {detail_url}")
#                 driver.get(detail_url)

#                 # Wait for the career statistics section to be present
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CLASS_NAME, 'b-list__info-box-left'))
#                 )

#                 # Scrape career statistics
#                 career_stats = {}
#                 left_stats_rows = driver.find_elements(By.XPATH, '//div[contains(@class,"b-list__info-box-left")]/ul/li')
#                 right_stats_rows = driver.find_elements(By.XPATH, '//div[contains(@class,"b-list__info-box-right")]/ul/li')

#                 for stat_row in left_stats_rows + right_stats_rows:
#                     try:
#                         key = stat_row.find_element(By.CLASS_NAME, 'b-list__box-item-title').text
#                         value = stat_row.text.replace(key, '').strip()
#                         career_stats[key.strip()] = value
#                         print(f"Found stat: {key.strip()} - {value.strip()}")
#                     except Exception as e:
#                         print(f"Error occurred while parsing stats: {e}")

#                 # Scrape win/loss record
#                 record = driver.find_element(By.CLASS_NAME, 'b-content__title-record').text.replace('Record: ', '').strip()
#                 print(f"Record: {record}")

#                 # Scrape fight history
#                 fights = []
#                 fight_rows = driver.find_elements(By.CLASS_NAME, 'b-fight-details__table-row')
#                 for fight_row in fight_rows:
#                     try:
#                         outcome = fight_row.find_element(By.CLASS_NAME, 'b-flag__text').text.strip()
#                         opponent = fight_row.find_elements(By.CLASS_NAME, 'b-link_style_black')[1].text.strip()
#                         event = fight_row.find_element(By.XPATH, './td[7]/p/a').text.strip()
#                         event_date = fight_row.find_element(By.XPATH, './td[7]/p[2]').text.strip()
#                         method = fight_row.find_element(By.XPATH, './td[8]/p').text.strip()
#                         round_info = fight_row.find_element(By.XPATH, './td[9]/p').text.strip()
#                         time_info = fight_row.find_element(By.XPATH, './td[10]/p').text.strip()

#                         fight_detail = {
#                             'Outcome': outcome,
#                             'Opponent': opponent,
#                             'Event': event,
#                             'Event Date': event_date,
#                             'Method': method,
#                             'Round': round_info,
#                             'Time': time_info
#                         }
#                         fights.append(fight_detail)
#                         print(f"Fight: {fight_detail}")
#                     except Exception as e:
#                         print(f"Error occurred while parsing fight history: {e}")

#                 fighter_data.append({
#                     'First Name': first_name,
#                     'Last Name': last_name,
#                     'Nickname': nickname,
#                     'Record': record,
#                     'Career Statistics': career_stats,
#                     'Fight History': fights
#                 })

#                 # Go back to the main page
#                 driver.back()
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CLASS_NAME, 'b-statistics__table-row'))
#                 )

#             except Exception as e:
#                 print(f"Error occurred while processing row: {e}")

#     except Exception as e:
#         print(f"Error occurred: {e}")

#     finally:
#         driver.quit()

#     # Create a DataFrame and save to Excel
#     df = pd.DataFrame(fighter_data)
#     df.to_excel('fighter_data.xlsx', index=False)

#     print("Data saved to fighter_data.xlsx")

# if __name__ == '__main__':
#     scrape_data()


# This script works properly only for the first five fighters whose names start with the letter 'a'. The script navigates to the UFC Stats website, scrapes the data for each fighter, and saves the data to an Excel file. The script uses the Selenium WebDriver to interact with the website and extract the necessary information.

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# import time as pytime

# def scrape_data():
#     # Set up the Selenium WebDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#     fighter_data = []

#     try:
#         char = 'a'
#         driver.get(f'http://www.ufcstats.com/statistics/fighters?char={char}&page=all')
#         print(f"Scraping fighters starting with '{char}'")

#         # Wait for the page to load
#         pytime.sleep(5)

#         # Scrape fighter data
#         rows = driver.find_elements(By.CLASS_NAME, 'b-statistics__table-row')
#         for row in rows[1:]:  # Skip the header row
#             try:
#                 first_name = row.find_element(By.XPATH, './td[1]/a').text
#                 last_name = row.find_element(By.XPATH, './td[2]/a').text
#                 try:
#                     nickname = row.find_element(By.XPATH, './td[3]').text
#                 except:
#                     nickname = ''  # Assign a blank space if nickname is not found

#                 # Navigate to fighter's detail page
#                 detail_url = row.find_element(By.XPATH, './td[1]/a').get_attribute('href')
#                 print(f"Navigating to URL: {detail_url}")
#                 driver.get(detail_url)

#                 # Wait for the career statistics section to be present
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CLASS_NAME, 'b-list__info-box-left'))
#                 )

#                 # Scrape career statistics
#                 career_stats = {}
#                 left_stats_rows = driver.find_elements(By.XPATH, '//div[@class="b-list__info-box-left"]/ul/li')
#                 right_stats_rows = driver.find_elements(By.XPATH, '//div[@class="b-list__info-box-right"]/ul/li')

#                 for stat_row in left_stats_rows + right_stats_rows:
#                     try:
#                         key_element = stat_row.find_element(By.CLASS_NAME, 'b-list__box-item-title')
#                         value = stat_row.text.replace(key_element.text, '').strip()
#                         key = key_element.text.strip(':').strip()
#                         career_stats[key] = value
#                         print(f"Found stat: {key} - {value}")
#                     except Exception as e:
#                         print(f"Error occurred while parsing stats: {e}")

#                 # Append the data to the list
#                 fighter_data.append({
#                     'First Name': first_name,
#                     'Last Name': last_name,
#                     'Nickname': nickname,
#                     'Career Statistics': career_stats,
#                 })

#                 # Go back to the main page
#                 driver.back()
#                 WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CLASS_NAME, 'b-statistics__table-row'))
#                 )

#             except Exception as e:
#                 print(f"Error occurred while processing row: {e}")

#         # Wait for a while after processing to avoid overwhelming the server
#         pytime.sleep(15)

#     except Exception as e:
#         print(f"Error occurred: {e}")

#     finally:
#         driver.quit()

#     # Create a DataFrame and save to Excel
#     df = pd.DataFrame(fighter_data)
#     df.to_excel('fighter_data_a.xlsx', index=False)

#     print("Data saved to fighter_data_a.xlsx")

# if __name__ == '__main__':
#     scrape_data()








from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time as pytime
import string

def scrape_data():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    fighter_data = []

    try:
        for char in string.ascii_lowercase:  # Loop through 'a' to 'z'
            driver.get(f'http://www.ufcstats.com/statistics/fighters?char={char}&page=all')
            print(f"Scraping fighters starting with '{char}'")

            # Wait for the page to load
            pytime.sleep(5)

            # Scrape fighter data
            rows = driver.find_elements(By.CLASS_NAME, 'b-statistics__table-row')
            for row in rows[1:]:  # Skip the header row
                try:
                    first_name = row.find_element(By.XPATH, './td[1]/a').text
                    last_name = row.find_element(By.XPATH, './td[2]/a').text
                    try:
                        nickname = row.find_element(By.XPATH, './td[3]').text
                    except:
                        nickname = ''  # Assign a blank space if nickname is not found

                    # Navigate to fighter's detail page
                    detail_url = row.find_element(By.XPATH, './td[1]/a').get_attribute('href')
                    print(f"Navigating to URL: {detail_url}")
                    driver.get(detail_url)

                    # Wait for the career statistics section to be present
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'b-list__info-box-left'))
                    )

                    # Scrape career statistics
                    career_stats = {}
                    left_stats_rows = driver.find_elements(By.XPATH, '//div[@class="b-list__info-box-left"]/ul/li')
                    right_stats_rows = driver.find_elements(By.XPATH, '//div[@class="b-list__info-box-right"]/ul/li')

                    for stat_row in left_stats_rows + right_stats_rows:
                        try:
                            key_element = stat_row.find_element(By.CLASS_NAME, 'b-list__box-item-title')
                            value = stat_row.text.replace(key_element.text, '').strip()
                            key = key_element.text.strip(':').strip()
                            career_stats[key] = value
                            print(f"Found stat: {key} - {value}")
                        except Exception as e:
                            print(f"Error occurred while parsing stats: {e}")

                    # Scrape fighter's record
                    record = driver.find_element(By.CLASS_NAME, 'b-content__title-record').text.replace('Record: ', '').strip()
                    print(f"Record: {record}")

                    # Scrape fight history
                    fights = []
                    fight_rows = driver.find_elements(By.CLASS_NAME, 'b-fight-details__table-row')
                    for fight_row in fight_rows:
                        try:
                            outcome = fight_row.find_element(By.CLASS_NAME, 'b-flag__text').text.strip()
                            opponent = fight_row.find_elements(By.CLASS_NAME, 'b-link_style_black')[1].text.strip()
                            event = fight_row.find_element(By.XPATH, './td[7]/p/a').text.strip()
                            event_date = fight_row.find_element(By.XPATH, './td[7]/p[2]').text.strip()
                            method = fight_row.find_element(By.XPATH, './td[8]/p').text.strip()
                            round_info = fight_row.find_element(By.XPATH, './td[9]/p').text.strip()
                            time_info = fight_row.find_element(By.XPATH, './td[10]/p').text.strip()

                            fight_detail = {
                                'Outcome': outcome,
                                'Opponent': opponent,
                                'Event': event,
                                'Event Date': event_date,
                                'Method': method,
                                'Round': round_info,
                                'Time': time_info
                            }
                            fights.append(fight_detail)
                            print(f"Fight: {fight_detail}")
                        except Exception as e:
                            print(f"Error occurred while parsing fight history: {e}")

                    # Append the data to the list
                    fighter_data.append({
                        'First Name': first_name,
                        'Last Name': last_name,
                        'Nickname': nickname,
                        'Record': record,
                        'Career Statistics': career_stats,
                        'Fight History': fights
                    })

                    # Go back to the main page
                    driver.back()
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, 'b-statistics__table-row'))
                    )

                except Exception as e:
                    print(f"Error occurred while processing row: {e}")

            # Wait for a while after processing each letter to avoid overwhelming the server
            pytime.sleep(15)  # Adjust sleep time as needed

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        driver.quit()

    # Create a DataFrame and save to Excel
    df = pd.DataFrame(fighter_data)
    df.to_excel('fighter_data.xlsx', index=False)

    print("Data saved to fighter_data.xlsx")

if __name__ == '__main__':
    scrape_data()
