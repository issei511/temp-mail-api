#from flask import Flask, render_template
from flask import *
import requests as r
from selenium import webdriver as w
import time
from bs4 import BeautifulSoup as bs



def slp(sec):
	time.sleep(sec)
def gm():
	f = -1
	while (f == -1):
		email = str(d.find_element_by_xpath('//*[@id="mail"]').get_attribute('value'))
		if (int(email.find("@")) != -1):
			return email
		else:
			pass
status = 0
options = w.ChromeOptions()
options.add_argument("-headless")
d = w.Chrome(executable_path="/home/kajawali/softwares/chrome_driver/chromedriver",options=options)
d.get("https://temp-mail.org/en/")
status = 1
app = Flask(__name__)

@app.route('/')
def index():
	if status == 0:
		return "Inactive"
	else:
		return "Active_options{get_id,get_mail,change}"

@app.route("/get_id")
def start():
	if status == 0:
		return "Error In server"
	else:
		return gm()

@app.route("/get_mail")
def get_mail():
	tmp =  d.find_element_by_class_name("inbox-dataList").get_attribute("innerHTML")
	soup = bs(tmp, "html.parser")
	tmp = soup.find_all("a")
	tc = 0
	for i in tmp:
		tc += 1
	if tc > 5:
		mail_link = tmp[4].get("href")
		d.execute_script(f"window.open('{mail_link}')")
		d.switch_to.window(d.window_handles[1])
		slp(3)
		text =  d.find_element_by_class_name("inbox-data-content-intro").text
		d.close()
		d.switch_to.window(d.window_handles[0])
		slp(1)
		d.find_element_by_id("click-to-delete").click()
		return text
	else:
		return "no mail"

@app.route("/change")
def change():
	d.find_element_by_xpath('//*[@id="click-to-delete"]').click()
	slp(1)
	return gm()


if __name__ == '__main__':
	app.run(debug = True)