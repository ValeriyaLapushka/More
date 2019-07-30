# Задание: загрузка файла
# В этом задании в форме регистрации требуется загрузить текстовый файл.

# Напишите скрипт, который будет выполнять следующий сценарий:

# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Отправить"
# Если все сделано правильно и быстро, вы увидете окно с числом. 

from selenium import webdriver
import os

brow = webdriver.Chrome()
brow.get("http://suninjuly.github.io/file_input.html")

name = brow.find_element_by_name('firstname')
name.send_keys('Leo')

lastname = brow.find_element_by_name('lastname')
lastname.send_keys('LeoLeo')

email = brow.find_element_by_name('email')
email.send_keys('Leo@leo.com')


fil = brow.find_element_by_css_selector("input[id='file']")

current_dir = os.path.abspath(os.path.dirname(r'C:\Users\Лео Лапушка\Desktop\text.txt'))
file_path = os.path.join(current_dir, 'text.txt')
print(file_path)

fil.send_keys(file_path)


button = brow.find_element_by_css_selector('button.btn')
button.click()