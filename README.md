# Introduction #
[TrumpTracker](http://wraith.pythonanywhere.com) is a simple website which can load the latest 25 articles from [CNN US Politics](https://us.cnn.com/politics/) about Donald Trump. You can visit the [website](http://wraith.pythonanywhere.com)  or use the instructions below are to run a local version on your computer.

# Prerequisites #
This website is built to run on the address `localhost:5000` using the [Flask](http://flask.pocoo.org/) framework. In order to run the website, the following dependencies must be present on the system:
1. [Python3](https://www.python.org/downloads/) – This website is built upon the Flask framework which runs on python. There are also custom codes for data fetching and processing written in python3.5.
2. [Flask](http://flask.pocoo.org/) – Flask is a lightweight framework to build websites using python. 
3. [Selenium](https://selenium-python.readthedocs.io/installation.html) – This library is used as a web driver, something that acts like a browser and emulates its actions, in order to load the scraping target website and fetch its data.
4. [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) - A python library which facilitates the parsing of HTML document. Make sure to install Beautifulsoup4 as the older versions are no longer being maintained.
5. [PhantomJS](https://gist.github.com/julionc/7476620) - The headless browser used in this code by Selenium to crawl the web. You will need to have this executable in one of your `$PATH` directories. You can see them by executing `echo $PATH` in a Linux terminal.

# Installation #
After installing all the outlined prerequisites, you can use the one of the following ways to get a copy of the website and all its required components to function properly:
1. Use the following code to clone this repository and set things up in Linux (this will install all of the prerequisite packages except for PhantomJS, if you already have [pip](https://packaging.python.org/tutorials/installing-packages/#installing-from-pypi) on your system):
```
git clone https://github.com/JerichoIX/TrumpTracker.git
cd TrumpTracker/
pip3 install -r requirements.txt  # Add '--user' if you do not have root access
```
2. Visit the website's [github](https://github.com/JerichoIX/TrumpTracker/) repository and download a compressed version of all the files manually. Please note that you will need to install the prerequisites yourself.

# Running the Website #
Open a Linux terminal, head to the website directory (`somePath/TrumpTracker/`) and run the following code:
```
python3 basic.py
```
This will run a local server at `localhost:5000`. Now you can visit the webpage by typing this address into your browser of choice, which should have Javascript enabled.
To shut the server down, just press `Ctrl+C` in the same Linux terminal that you used to start the server.
