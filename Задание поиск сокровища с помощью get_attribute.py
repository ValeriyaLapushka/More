# Задание: поиск сокровища с помощью get_attribute
# В данной задаче вам нужно с помощью роботов решить ту же математическую задачу. 

#значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

# Ваша программа должна:

# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".



from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
brow = webdriver.Chrome()
brow.get('http://suninjuly.github.io/get_attribute.html')

pic = brow.find_element_by_tag_name('img')
x = pic.get_attribute("valuex")
print(x)
print(type(x))
y = calc(x)

find = brow.find_element_by_css_selector('input')
find.send_keys(y)

check = brow.find_element_by_id('robotCheckbox')
check.click()

radio = brow.find_element_by_css_selector("[value='robots']")
radio.click()

button = brow.find_element_by_css_selector('button.btn')
button.click()