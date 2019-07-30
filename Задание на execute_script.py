# Задание на execute_script
# В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "Подтверждаю, что являюсь роботом".
# Переключить radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
               
brow = webdriver.Chrome()
brow.get('http://SunInJuly.github.io/execute_script.html')

brow.execute_script("window.scrollBy(0, 75);")

fin = brow.find_element_by_xpath(".//*[@id='input_value']")
x = fin.text
y = calc(x)

inp = brow.find_element_by_id('answer')
inp.send_keys(y)

push = brow.find_element_by_id("robotCheckbox")
push.click()

push2 = brow.find_element_by_id("robotsRule")
push2.click()

button = brow.find_element_by_tag_name("button")
brow.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()