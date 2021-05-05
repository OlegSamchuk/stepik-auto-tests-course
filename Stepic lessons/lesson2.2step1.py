from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def sum(x, y):
    return str (x + y)
    
 
try:  
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    number_x = browser.find_element_by_id("num1")
    x = int (number_x.text)
    number_y = browser.find_element_by_id("num2")
    y = int (number_y.text)
    print(sum(x, y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum(x, y))
    option3 = browser.find_element_by_class_name("btn")
    option3.click()
    
    
finally:
       time.sleep(10)
       browser.quit()