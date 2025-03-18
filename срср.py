# print(type(input("cc: ")))
# import tkinter as tk

# root = tk.Tk()
# dpi = root.winfo_fpixels('1i')
# root.destroy()

# print("DPI экрана:", int(dpi))

# from PyQt5.QtWidgets import QApplication
# app = QApplication([])
# for screen in app.screens():
#     dpi = screen.physicalDotsPerInch()
#     print(f"Screen {screen.name()} DPI =", dpi)
# app.quit()

# Получение пикселя изображения
# import pyautogui
# scrn = pyautogui.screenshot(region=(window_rect[0], window_rect[1], window_rect[2], window_rect[3]))
# pixel = scrn.getpixel((x, y))

# # Расчет яркости пикселя для черно-белого изображения
# brightness = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])

# # Печать значения яркости
# print(brightness)

# number = 30


# if 90 % number == 0:
#     print('Привет')
# from PIL import Image, ImageEnhance
# # import numpy as np
# # import matplotlib.pyplot as plt
# # from collections import Counter
# import pytesseract

# # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# image = Image.open('screenshot.png')

# #Повышенние резкости изображения:
# enhancer1 = ImageEnhance.Sharpness(image)
# factor1 = 0.01 #чем меньше, тем больше резкость
# im_s_1 = enhancer1.enhance(factor1)

# text = pytesseract.image_to_string(im_s_1, config='--psm 6 -c tessedit_char_whitelist=0123456789,. ').split('\n')
# print(text)

# def whatNumIsThis(filePath):

#     matchedAr = []
#     loadExamps = open('numArEx.txt','r').read()
#     loadExamps = loadExamps.split('\n')
#     i = Image.open(filePath)
#     iar = np.array(i)
#     iarl = iar.tolist()
#     inQuestion = str(iarl)
#     for eachExample in loadExamps:
#         try:
#             splitEx = eachExample.split('::')
#             currentNum = splitEx[0]
#             currentAr = splitEx[1]
#             eachPixEx = currentAr.split('],')
#             eachPixInQ = inQuestion.split('],')
#             x = 0
#             while x < len(eachPixEx):
#                 if eachPixEx[x] == eachPixInQ[x]:
#                     matchedAr.append(int(currentNum))

#                 x+=1
#         except Exception as e:
#             print(str(e))
                
#     x = Counter(matchedAr)
#     print(x)
#     graphX = []
#     graphY = []

#     ylimi = 0

#     for eachThing in x:
#         graphX.append(eachThing)
#         graphY.append(x[eachThing])
#         ylimi = x[eachThing]

# whatNumIsThis('screenshot.png')


# from PIL import Image
# import easyocr

# # Загрузка изображения с помощью Pillow
# image = Image.open('screenshot.png')

# # Преобразование изображения к формату, поддерживаемому easyocr
# image = image.convert('RGB')

# # Инициализация модели EasyOCR для распознавания цифр
# reader = easyocr.Reader(['en'])

# # Распознавание текста на изображении
# result = reader.readtext(image)

# # Фильтрация результатов для получения только цифр
# digits = [entry[1] for entry in result if entry[1].isdigit()]

# print(digits)

# import cv2
# import numpy as np

# # Загрузка скриншота
# image = cv2.imread('screenshot.png')

# # Преобразование изображения в оттенки серого
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Применение порогового фильтра для бинаризации изображения
# _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# # Нахождение контуров на изображении
# contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Цикл по контурам
# for contour in contours:
#     print(1)
#     # Получение координат прямоугольника, ограничивающего контур
#     x, y, w, h = cv2.boundingRect(contour)
    
#     # Отбросить слишком маленькие или слишком большие прямоугольники
#     if w < 5 or h < 5 or w > 100 or h > 100:
#         continue
    
#     # Вырезание цифры
#     digit = gray[y:y+h, x:x+w]
#     print(1)
    
#     # Распознавание цифры - примерный метод, можно заменить на более точный
#     # Пример: просто получение среднего значения пикселей в вырезанной области
#     digit_value = np.mean(digit)
    
#     # Вывод распознанной цифры
#     print("Распознанная цифра:", int(digit_value))

# # Показать изображение с контурами (опционально)
# cv2.imshow('Contours', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2

# # Загрузка скриншота
# image = cv2.imread('screenshot.png')

# # Преобразование изображения в оттенки серого
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Применение порогового фильтра для выделения цифр
# _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# # Нахождение контуров цифр
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Цикл по контурам
# for contour in contours:
#     # Получение координат прямоугольника, ограничивающего контур
#     x, y, w, h = cv2.boundingRect(contour)
    
#     # Вырезание цифры
#     digit = gray[y:y+h, x:x+w]
    
#     # Примерный метод распознавания цифры
#     # Можно реализовать более сложные алгоритмы распознавания
#     # Например, обучение модели машинного обучения на наборе цифр
#     digit_value = 0  # Здесь можно добавить ваш код для распознавания цифры
    
#     # Вывод распознанной цифры
#     print("Распознанная цифра:", digit_value)

# # Показать изображение с контурами (опционально)
# # cv2.imshow('Digits', image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# import tkinter as tk

# def get_dpi_tkinter():
#     root = tk.Tk()
#     root.withdraw()  # Скрыть главное окно
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
#     screen_inches_width = root.winfo_screenmmwidth() / 25.4
#     screen_inches_height = root.winfo_screenmmheight() / 25.4
#     dpi_x = screen_width / screen_inches_width
#     dpi_y = screen_height / screen_inches_height
#     return dpi_x, dpi_y

# dpi_x, dpi_y = get_dpi_tkinter()
# print(f"DPI X: {dpi_x:.2f}, DPI Y: {dpi_y:.2f}")

# import ctypes

# hdc = ctypes.windll.user32.GetDC(0)
# dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # 88 - это код CAPS для DPI
# ctypes.windll.user32.ReleaseDC(0, hdc)
# dpi_ratio = 96 / dpi


# import math


# def largest_divisor(n):
#     for i in range(n - 1, 0, -1):
#         if n % i == 0:
#             return i
#     return 1

# number = 1440
# largest_div = largest_divisor(number)

# print(f"Наибольший делитель {number} (кроме самого числа): {largest_div}")

# print("СТАРТ")

# from pygetwindow import getWindowsWithTitle
# from pyautogui import position, screenshot, scroll

# check = getWindowsWithTitle("TelegramDesktop")
# telegram_window = check[0]
# print(telegram_window)
# window_rect = (telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height)

# from pyautogui import position, screenshot, scroll
# from keyboard import is_pressed
# from pynput.mouse import Button, Controller
# from white_list import *
# from art import tprint
# from termcolor import colored
# from colorama import init

# from screeninfo import get_monitors

# monitors = get_monitors()
# main_monitor = monitors[0]
# print(f"Разрешение основного экрана: {main_monitor.width}x{main_monitor.height}")


# mouse = Controller()
# def click(x,y):
#     mouse.position = (x, y)


# similarity_desktop_x = 402
# similarity_desktop_y = 712

# similarity_win_x = 1920
# similarity_win_y = 1080
# width = window_rect[2]
# height = window_rect[3]
# X_line = window_rect[0]
# Y_line = window_rect[1]

# # width = 1440
# # height = 932

# # xx_absolute = 1 + (1 - (similarity_win_x / 1440))
# # yy_absolute = 1 + (1 - (similarity_win_y / 932))

# xx = 1 + ((1 - (similarity_desktop_x / width)) / 100)
# yy = 1 + ((1 - (similarity_desktop_y / height)) / 6)

# X_line = X_line + (0.795*width/xx)
# Y_line = Y_line + (0.645*height/yy)

# click(X_line, Y_line)




# if xx != 1:
#     xx = 1 - xx
# if yy != 1:
#     yy = 1 - yy


# # print(height)
# x = 0.784 / xx
# y = 0.645 / yy
# print(x, y)
# x = width * 0.784 + x
# y = height * 0.645 + y
# print(X_line, Y_line)
# X_line = X_line * xx_absolute
# Y_line = Y_line * yy_absolute
# print(X_line, Y_line)
# x = x + X_line
# y = y + Y_line

# click(x, y)

# import time
# time.sleep(1)

# scroll(-200)


# print("КОНЕЦ")
# time.sleep(20)

# r = 177
# for r in range(138, 177):
#     print(r)

from PIL import Image

# Загружаем изображение
image = Image.open('ldinka.png').convert('RGB')

# Получаем размеры изображения
width, height = image.size

for y in range(0, height, 1):
    for x in range(0, width, 1):
        r, g, b = image.getpixel((x, y))

        if ((b in range(88, 121)) and (r in range(88, 177)) and (g in range(88, 177))):
            print(r, g, b, x ,y) #158 #146 #112
