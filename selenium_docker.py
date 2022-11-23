from selenium import webdriver
 
driver = webdriver.Chrome()
driver.get("http://www.qxf2.com")
print (driver.title)
driver.quit()