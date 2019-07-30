# Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
# Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Забронировать"
# Решить уже известную нам математическую задачу  и отправить решение
# Чтобы определить момент, когда стоимость дома уменьшится до 10000 RUR, 
# используйтe метод text_to_be_present_in_element из библиотеки expected_conditions.



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False) #тк у меня браузер 75 версии, без этих строк выдает ошибку С:


brow = webdriver.Chrome(chrome_options=opt) 
brow.get('http://suninjuly.github.io/explicit_wait2.html')

price = WebDriverWait(brow, 12).until((EC.text_to_be_present_in_element((By.ID, "price"),'10000 RUR')))

button = WebDriverWait(brow, 13).until(EC.element_to_be_clickable((By.ID, "book"))) 
button.click()


but = brow.find_element_by_css_selector('button.btn')
but.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
x_el = brow.find_element(By.ID,'input_value')   
x = x_el.text
y = calc(x)

input_x = brow.find_element_by_id('answer')
input_x.send_keys(y)

send_but = brow.find_element_by_id('solve')
send_but.click()