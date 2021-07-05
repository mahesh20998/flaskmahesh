from flask import Flask, render_template, url_for,request,redirect, session
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import os

app = Flask(__name__)
app.secret_key =  'mahesh'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testing")
def testing():
    print("here")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chromeOptions.add_argument("--no-sandbox") 
    chromeOptions.add_argument("--disable-setuid-sandbox") 
    chromeOptions.add_argument("--remote-debugging-port=9222")
    chromeOptions.add_argument("--disable-dev-shm-using") 
    chromeOptions.add_argument("--disable-extensions") 
    chromeOptions.add_argument("--disable-gpu") 
    chromeOptions.add_argument("start-maximized") 
    chromeOptions.add_argument("disable-infobars")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-sh-usage")
    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH") , options = chrome_options)
    driver.get('https://www.google.co.in/')
    driver.find_element_by_name("q").send_keys("mahesh")
    return "Success"

if __name__ == "__main__":
    app.run(debug=True)
