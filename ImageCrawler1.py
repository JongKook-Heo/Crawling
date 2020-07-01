from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import json
import argparse

parser = argparse.ArgumentParser(description = 'Chrome Image Crawler')
parser.add_argument('--keyword', required = True, help = 'input keyword')
parser.add_argument('--driverpath', required = False, default = 'chromedriver', help = 'input driver path')
args = parser.parse_args()

keyword = str(args.keyword)
driverpath = str(args.driverpath)

url = ''.join(["https://www.google.com/search?q=", keyword, "&source=lnms&tbm=isch"])
driver = webdriver.Chrome(os.path.join(os.getcwd(),driverpath))

if not os.path.exists(keyword):
    os.mkdir(keyword)
save_path = os.path.join(os.getcwd(), keyword)

driver.get(url)

for _ in range(500):
    driver.execute_script("window.scrollBy(0,10000)")

for idx, img in enumerate(driver.find_elements_by_class_name("rg_i")):
    img.screenshot(os.path.join(save_path,"%s_%05d.png"%(keyword,idx)))

driver.close()
