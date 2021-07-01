from flask import Flask, render_template, url_for,request,redirect, session
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)
app.secret_key =  'mahesh'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testing")
def testing():
    print("here")
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
    driver.get('https://www.google.co.in/')
    driver.find_element_by_name("q").send_keys("mahesh")
    return "Success"

if __name__ == "__main__":
    app.run(debug=True, port=33507)
