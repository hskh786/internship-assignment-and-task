from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# ============ Configuration ============
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
CSV_FILE = "top_influencer5.csv"  # Must have 'username', 'followers', 'bio'

# ============ Setup Chrome Driver ============
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# ============ Instagram Login ============
def login():
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(3)

    # Accept cookies if prompted
    try:
        driver.find_element(By.XPATH, "//button[text()='Allow all cookies']").click()
        time.sleep(2)
    except:
        pass

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.ENTER)
    time.sleep(10)

# ============ Read and Filter CSV ============
#
        # Click message button
        message_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Message')]")
        message_button.click()
        time.sleep(3)

        # Type message
        message_box = driver.find_element(By.TAG_NAME, 'textarea')
        message_box.send_keys("Hi! I loved your profile. Let's collaborate!")
        time.sleep(1)
        message_box.send_keys(Keys.ENTER)
        print(f"✅ Message sent to {username}")
        time.sleep(3)
    except Exception as e:
        print(f"❌ Could not message {username}: {e}")

# ============ Main Execution ============
def main():
    login()
    influencers = load_and_filter_csv()
    print(f"Found {len(influencers)} influencers after filtering")

    for _, row in influencers.iterrows():
        visit_and_message(row['username'])

    driver.quit()

if __name__ == "__main__":
    main()
