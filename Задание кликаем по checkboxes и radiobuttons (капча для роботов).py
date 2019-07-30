#Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
#Продолжим использовать силу роботов 🤖 для решения повседневных задач.
# На данной странице мы добавили капчу для #роботов, то есть тест, 
#являющийся простым для компьютера, но сложным для человека.

#Ваша программа должна выполнить следующие шаги:

#Открыть страницу http://suninjuly.github.io/math.html.
#Считать значение для переменной x.
#Посчитать математическую функцию от x (код для этого приведён ниже).
#Ввести ответ в текстовое поле.
#Отметить checkbox "Подтверждаю, что являюсь роботом".
#Выбрать radiobutton "Роботы рулят!".
#Нажать на кнопку Отправить.



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
