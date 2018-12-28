# ***************************************************************************************
# TRUMP CRAWLER PROJECT - v1.1
# By B. Derakhshan
#
# ---------------------------------------------------------------------------------------
#
# 'Romanov' crawling package:
# Crawls and retrieves data from CNN US Politics and lists the latest 25 articles about
# Trump and their URLs.
#
# ---------------------------------------------------------------------------------------
#
# CONFIGURATION
# --------------

MAX_ARTICLES = 25
                                        # The maximum number of articles retrieved


# SYSTEM PARAMETERS - DO NOT ALTER!
# ---------------------------------

URL = 'https://us.cnn.com/politics'
                                        # The URL the spider will scrape
BASE_URL = 'https://us.cnn.com'
                                        # Used to complete the href link addresses
PAUSE_TIME = 2
                                        # How long should the scraper wait for the site
                                        # to load on each scroll
LINK_FORMATS = [
    '/2018',
    'https://www.cnn.com/politics/',
    'https://www.cnn.com/specials/politics/'
]

# ***************************************************************************************

# Import libraries
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display

def run():
    source = fetcher()
    soup = BeautifulSoup(source, 'html.parser')

    # Parse the CNN page to find the Trump-related articles
    headers = soup.find_all('h3', attrs={'class': 'cd__headline'})
    titles = []
    links = []
    counter = 0

    for header in headers:
        temp = header.find('span', attrs={'class': 'cd__headline-text'})

        # Filter out the irrelevant entries
        # We only want the articles which contain the word 'Trump'
        if 'Trump' in temp.text:

            # Found a match!
            counter += 1

            # Add the article title to our list
            titles.append(temp.text)

            # The links have one of these formats:
            #     '/2018/...'
            #     'https://www.cnn.com/politics/...'
            #     'https://www.cnn.com/specials/politics/...'
            # We modify the links with the first format to produce an absolute path
            temp = header.find('a', href=True)['href']
            if 'www.cnn.com' in temp:
                links.append(temp)
            else:
                links.append(BASE_URL + temp)

        if counter >= MAX_ARTICLES:
            break

    # Build a dict variable to write the results in JSON format
    result = {}
    for title in titles:
        # We are sure that no two articles have the exact same titles, so we can use
        # the following approach to enumerate over the titles list
        i = titles.index(title)
        result[title] = links[i]

    return json.dumps(result)

def fetcher():
    #print("Romanov started")
    display = Display(visible=0, size=(800, 600))
    display.start()
    # print("Screen created")
    cap = DesiredCapabilities().FIREFOX
    # cap["marionette"] = False
    driver = webdriver.Firefox(capabilities=cap, executable_path="/home/shahrooz/.local/bin/geckodriver")
    try:
        driver.get(URL)
        if driver is None:
            print("Driver error!")
            #return redirect(url_for('error'))
            return None

        print("Got URL")

        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            # Check if the page height has remained the same
            if new_height == last_height:
                # If so, we are done
                break
            # If not, move on to the next loop
            else:
                print("Scrolling again...")
                last_height = new_height
                continue

        html1 = driver.page_source

    finally:
        driver.close()

        #with open('politics.html', 'wb') as f:
        #    f.write(str.encode(html1))
        #    print("politics.html generated")
        #end_time = time.time()
        return html1