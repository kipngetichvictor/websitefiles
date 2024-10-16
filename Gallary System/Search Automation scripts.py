from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver Chrome
driver = webdriver.Chrome()

try:
    #
    driver.get("http://localhost/gallery/")
    driver.maximize_window()

    # Locate the search box and enter the search term
    search_box = WebDriverWait(driver, 900).until(
        EC.presence_of_element_located((By.ID, "searchCriteria"))
    )
    search_term = "album"
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Allow time for search results to appear
    time.sleep(60)

#  Validate the results
    results = driver.find_elements(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/form/div/div[3]/table/tbody/tr/td/a/img")

    print(f"Found {len(results)} results matching the search term.")

    if len(results) > 0:
        print("Search results:")
        for result in results:
            print(result.get_attribute("alt"))
    else:
        print("No matching results found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
# Close the browser
    driver.quit()
