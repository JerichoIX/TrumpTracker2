# ***************************************************************************************
# TRUMP CRAWLER PROJECT - v1.1
# By B. Derakhshan
#
# ---------------------------------------------------------------------------------------
#
# 'Tweety' scraping package:
# Scrapes Twitter for the latest 25 tweets made by Donald Trump on his official account.
#
# ---------------------------------------------------------------------------------------
#
# SYSTEM PARAMETERS - DO NOT ALTER!
# --------------------------------
URL = 'https://twitter.com/realDonaldTrump'
                                        # The URL the scraper will crawl
PAUSE_TIME = 2
                                        # How long should the scraper wait for tweets
                                        # to load on each scroll
MAX_SCROLLS = 3
                                        # Maximum number of times the scraper scrolls to
                                        # bottom of the page, 3 is usually enough to retrieve
                                        # 25 tweets.
MAX_TWEETS = 25
                                        # Maximum number of retrieved tweets

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
                                        # User agent to be passed in the HTTP request header

# CSS SELECTORS FOR TWEET SCRAPING
# --------------------------------
P_CLASS = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"


# ***************************************************************************************
# Import required libraries
import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display
from flask import redirect, url_for
from bs4 import BeautifulSoup

# Parser to analyze Trump's Twitter page to extract the latest tweets
def run():
    print("Tweety started")
    source = fetcher()
    soup = BeautifulSoup(source, 'html.parser')

    # Parse the HTML code to find tweet texts
    texts = soup.find_all('p', attrs={"class": P_CLASS})

    # Keep only the desired number of tweets
    texts = texts[0:MAX_TWEETS-1]

    # Do some filtering to remove the picture addresses from tweet texts, as Twitter includes
    # the the URL for pictures at the end of each <p> body string. They all start with
    # 'pic.twitter.com'
    counter = 1
    bodies = []
    for body in texts:
        body = body.text
        counter += 1
        if 'pic.twitter' in body:
            # Find the starting point fo the URL and slice the string accordingly
            i = body.find('pic.twitter')
            body = body[0:i]

        bodies.append(body)

        if counter >= MAX_TWEETS:
            print("Enough tweets!")
            break

    # Build a dict variable to write the results in JSON format
    result = {}
    for body in bodies:
        i = bodies.index(body)
        result[str(i)] = body

    return json.dumps(result)

# --------------------------------------------------------------------

# Fetcher to get Trump's Twitter page source
def fetcher():
    start_time = time.time()
    print("Tweety started")
    display = Display(visible=0, size=(800, 600))
    display.start()
    print("Screen created")
    cap = DesiredCapabilities().FIREFOX
    #cap["marionette"] = False
    driver = webdriver.Firefox(capabilities=cap, executable_path="/home/shahrooz/.local/bin/geckodriver")
    try:
        driver.get(URL)
        if driver is None:
            print("Driver error!")
            #return redirect(url_for('error'))
            return None

        print("Got URL")
        scrolls = 0
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            scrolls += 1

            # Check if the page height has remained the same
            if (new_height == last_height) or (scrolls >= MAX_SCROLLS):
                # If so, we are done
                break
            # If not, move on to the next loop
            else:
                last_height = new_height
                print("scrolling again")
                continue

        html1 = driver.page_source
        # html2 = driver.execute_script("return document.documentElement.innerHTML;")
    finally:
        driver.close()
        #with open('tweets.html', 'wb') as f:
        #    f.write(str.encode(html1))
        #    print("tweets.html generated")
        #end_time = time.time()
        #print(str(end_time - start_time))
        return html1
