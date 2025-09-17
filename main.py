
# Twitter API Configuration in Python

import tweepy

# API Authentication (Insert your keys)
API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_API_SECRET'
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_SECRET'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# Selenium Script for Likes and Retweets Automation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random

# Chrome Configuration with Random User-Agent
ua = UserAgent()
chrome_options = Options()
chrome_options.add_argument(f"user-agent={ua.random}")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--headless")  # Run in hidden mode

# Chrome driver path
driver = webdriver.Chrome(service=Service("Path/to/chromedriver"), options=chrome_options)

# Twitter Login Function
def login_twitter():
    driver.get("https://twitter.com/login")
    time.sleep(random.uniform(3, 6))

    # Login elements
    username = driver.find_element(By.NAME, "session[username_or_email]")
    password = driver.find_element(By.NAME, "session[password]")
    username.send_keys("YOUR_EMAIL")
    password.send_keys("YOUR_PASSWORD")
    password.submit()

    time.sleep(random.uniform(5, 8))

# Function to Like, Comment and Retweet
def interact_tweet(url, comment):
    driver.get(url)
    time.sleep(random.uniform(3, 5))

    # Like
    try:
        like_button = driver.find_element(By.XPATH, "//div[@data-testid='like']")
        like_button.click()
        time.sleep(random.uniform(1, 3))
    except:
        pass  # In case it's already liked

    # Retweet
    try:
        retweet_button = driver.find_element(By.XPATH, "//div[@data-testid='retweet']")
        retweet_button.click()
        confirm_button = driver.find_element(By.XPATH, "//div[@data-testid='retweetConfirm']")
        confirm_button.click()
        time.sleep(random.uniform(1, 3))
    except:
        pass

    # Comment
    try:
        reply_box = driver.find_element(By.XPATH, "//div[@aria-label='Reply']")
        reply_box.click()
        reply_box = driver.find_element(By.XPATH, "//div[@aria-label='Tweet your reply']")
        reply_box.send_keys(comment)
        reply_box.submit()
        time.sleep(random.uniform(1, 3))
    except:
        pass

# Mass Automation
login_twitter()
urls = ["https://twitter.com/status/1", "https://twitter.com/status/2"]
comments = ["Great post!", "Totally agree!"]

for url, comment in zip(urls, comments):
    interact_tweet(url, comment)
    time.sleep(random.uniform(30, 60))  # Random interval between interactions