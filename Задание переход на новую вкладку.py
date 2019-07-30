# Задание: переход на новую вкладку
# В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

# Сценарий для реализации выглядит так:

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом.


from selenium import webdriver
from selenium.webdriver.common.by import By

brow = webdriver.Chrome()
brow.get('http://suninjuly.github.io/redirect_accept.html')

but = brow.find_element_by_css_selector('button.btn')
but.click()

new_window = brow.window_handles[1]
brow.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
x_el = brow.find_element(By.ID,'input_value')   
x = x_el.text
y = calc(x)

input_x = brow.find_element_by_id('answer')
input_x.send_keys(y)

send_but = brow.find_element_by_css_selector('button.btn')
send_but.click()