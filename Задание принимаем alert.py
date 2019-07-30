# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),вы увидите окно с числом. 



from selenium import webdriver as wb
import math

brow = wb.Chrome()
brow.get('http://suninjuly.github.io/alert_accept.html')

but = brow.find_element_by_css_selector('button.btn')
but.click()

conf = brow.switch_to.alert
conf.accept()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
x_el = brow.find_element_by_id('input_value')   
x = x_el.text
y = calc(x)

input_x = brow.find_element_by_id('answer')
input_x.send_keys(y)

send_but = brow.find_element_by_css_selector('button.btn')
send_but.click()
