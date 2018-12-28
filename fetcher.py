# ***************************************************************************************
# TRUMP CRAWLER PROJECT - v1.1
# By B. Derakhshan
#
# ---------------------------------------------------------------------------------------
#
# 'Romanov' spider:
# Scrapes the CNN website for news on Donald Trump. Searches the URL specified below to
# retrieve the latest 25 articles on Trump.
#
# ---------------------------------------------------------------------------------------
#
# SYSTEM PARAMETERS - DO NOT ALTER!
# --------------------------------
URL = 'http://us.cnn.com/politics'
                                        # The URL the spider will scrape
PAUSE_TIME = 2
                                        # How long should the scraper wait for the site
                                        # to load
# ***************************************************************************************
# Import required libraries
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display

def romanov():
    start_time = time.time()

    print("Romanov started")
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
        #html2 = driver.execute_script("return document.documentElement.innerHTML;")
        driver.close()

        with open('politics.html', 'wb') as f:
            f.write(str.encode(html1))
            print("politics.html generated")
        end_time = time.time()
        elapsed = int(end_time-start_time)
        print(str(elapsed))
        return str(elapsed)