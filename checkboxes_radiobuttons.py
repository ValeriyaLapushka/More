from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
brow = webdriver.Chrome()
brow.get('http://suninjuly.github.io/math.html')
x_element = brow.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

find = brow.find_element_by_tag_name('input')
find.send_keys(y)

push = brow.find_element_by_css_selector("[for='robotCheckbox']")
push.click()

push2 = brow.find_element_by_css_selector("[value='robots']")
push2.click()

button = brow.find_element_by_css_selector("button.btn")
button.click()
