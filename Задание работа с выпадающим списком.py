# Задание: работа с выпадающим списком
# Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

# Напишите код, который реализует следующий сценарий:

# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Отправить"
# Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

brow = webdriver.Chrome()
brow.get('http://suninjuly.github.io/selects1.html')

numfind = brow.find_element_by_id('num1')
num1 = numfind.text

numfind2 = brow.find_element_by_id('num2')
num2 = numfind2.text

sum = int(num1) + int(num2)

sel = Select(brow.find_element_by_id('dropdown'))
sel.select_by_value(str(sum)) 

button = brow.find_element_by_css_selector('button.btn')
button.click()
