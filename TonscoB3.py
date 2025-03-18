
import time
import pyscreeze
import collectsystem
from Cls_er import clicker
from white_list import *
from art import tprint
from exactly_b import *
from art import text2art
from termcolor import colored
from colorama import init, Fore
from chern import main as mm
init()


###################################     MAIN     ######################################


def test_mouse():
    tprint("Test mouse")
    print(colored(f'\n[Tonsco] | Гравитация которая используется в скрипте - 9\n', 'cyan'))
    time.sleep(0.5)
    Gravity = input(colored(text='Введите цифру: ', attrs=["blink"]))
    time.sleep(0.5)
    print(colored(f'\n[Tonsco] | Скорость ветра которая используется в скрипте - 6\n', 'cyan'))
    time.sleep(0.5)
    Wind = input(colored(f'Введите цифру: ', 'white'))
    from matplotlib import pyplot as plt

    fig = plt.figure(figsize=[13,13])
    plt.axis('off')
    for y in linspace(-200,200,25):
        points = []
        wind_mouse(0,y,500,y,move_mouse=lambda x,y: points.append([x,y]), G_0=int(Gravity), W_0=int(Wind))
        points = asarray(points)
        plt.plot(*points.T)
    plt.xlim(-50,550)
    plt.ylim(-250,250)
    plt.show()

    window_name = input(colored('\n[WIND] | Выбери действие:\n\n1 - Blum\n2 - Test Mouse\n\nВыбери цифру: ', 'green'))
    if window_name == '1':
        clicker()
    if window_name == '2':
        test_mouse()


db_scr = Table_scr(collectsystem.DataUrl)



def MENUu():
    window_name = input(colored('\n[WIND] | Выбери действие:\n\n1 -- Blum\n2 -- Авто-сбор Blum на всех аккаунтах\n3 -- Test Mouse\n\nВыбери цифру: ', 'green'))
    if window_name == '1':
        clicker()
    if window_name == '2':
        print(colored('Еще не добавлено', 'blue'))
        MENUu()
    if window_name == '3':
        test_mouse()


def mainn():
    art = text2art("Tonsco   is   G.O.A.T")
    print(Fore.MAGENTA + art)
    NumComp = mm()
    print(colored('Провека в базе данных...', 'light_green'))
    print("(На некоторых компьютерах, подключение может задержаться)")
    if not db_scr.CheckRegistr(NumComp):
        db_scr.AddUser(NumComp)
    if not db_scr.CheckUnicKey(NumComp):
        bool_valu = True
        while bool_valu:
            UnicKey = input(colored('🔑 Введи свой ключ, сэр: ', "magenta"))
            if UnicKey == "log11n":
                print("Твой уникальный логин", NumComp)
            if UnicKey in db_scr.GetFreeKey():
                bool_valu = False
                db_scr.DeleteFreeKey(UnicKey)
                db_scr.AddFreeKey_toUser(NumComp, UnicKey)
                MENUu()
            else:
                print(colored(f"[FALSE]", "red"), "| Код не верный!\n")
                time.sleep(1)
    else:
        MENUu()

if __name__ == "__main__":
    mainn()


# auto-py-to-exe
# myenv\Scripts\activate
# pyinstaller --clean rer.spec