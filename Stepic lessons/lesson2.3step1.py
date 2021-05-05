from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("button")
    input1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    input3 = browser.find_element_by_id("answer")
    input3.send_keys(calc(x))
    input4 = browser.find_element_by_tag_name("button")
    input4.click()
    

finally:
    time.sleep(10)
    browser.quit()    