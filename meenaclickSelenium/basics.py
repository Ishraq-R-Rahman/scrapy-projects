from selenium import webdriver
from shutil import which

chrome_path = which("chromedriver")

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://duckduckgo.com" )
