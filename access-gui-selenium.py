#import webdriver 
from selenium import webdriver

selenium_driver = webdriver.Chrome()

# Google Search

url = input("Enter you want to search :")

# replace whitespace
url.replace(" ","%20")

# search the url
selenium_driver.get('https://www.google.com/search?q='+url)

# Close the browser
selenium_driver.close()
