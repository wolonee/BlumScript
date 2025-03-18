
from pygetwindow import getWindowsWithTitle
# from check_imgs import find_img
from pyautogui import position, screenshot, scroll
from keyboard import is_pressed
from pynput.mouse import Button, Controller
from white_list import *
from art import tprint
from exactly_b import *
from termcolor import colored
from colorama import init
from win32api import SetCursorPos
import time, ctypes
init()


def closest_aspect_ratio():
    aspect_ratio_width = 1920
    aspect_ratio_height = 1080
    user32 = ctypes.windll.user32
    target_width = user32.GetSystemMetrics(0)
    target_height = user32.GetSystemMetrics(1)
    if target_width == 1920:
        height_sootnoch_2 = 1 + (1 - (aspect_ratio_height / target_height))
        return 1, height_sootnoch_2
    else:
        width_sootnoch = aspect_ratio_width / target_width
        # new_width = (target_width / aspect_ratio_width)*aspect_ratio_width
        new_height = aspect_ratio_height * width_sootnoch
        new_height_2 = new_height/aspect_ratio_height
        return 1, new_height_2

resolution = closest_aspect_ratio()
print(resolution)

hdc = ctypes.windll.user32.GetDC(0)
dpi = ctypes.windll.gdi32.GetDeviceCaps(hdc, 88)  # 88 - это код CAPS для DPI
ctypes.windll.user32.ReleaseDC(0, hdc)
# dpi_ratio = 96 / dpi


def clicker():
    last_x = 1000
    last_y = 500
    Total_games = 0

    mouse = Controller()
    time.sleep(0.5)

    #############################    RebootBlum    ################################
    
    def Cursor(screen_x, screen_y):
        current_position = position()
        last_x = current_position[0]
        last_y = current_position[1]

        points = []
        rand_time_for_sleep_22 = random.randint(70,200)
        INPUT_time_for_curso = float(1/rand_time_for_sleep_22)
        wind_mouse(last_x, last_y, screen_x, screen_y, move_mouse=lambda x,y: points.append([x,y]))
        last_x = screen_x
        last_y = screen_y
        points = asarray(points)
        for i in range(len(points)):
            SetCursorPos((points[i][0], points[i][1]))
            time.sleep(INPUT_time_for_curso)




    def StartBlum():
        check = getWindowsWithTitle(window_name)
        telegram_window = check[0]
        randoms_time_for_choice = [0.3, 0.4, 0.5, 0.6, 0.7]
        rand_time_for_sleep = random.choice(randoms_time_for_choice)


        window_rect = (telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height)

        x = window_rect[2] * 0.784
        y = window_rect[3] * 0.645
        screen_x_1 = window_rect[0] + x  # * dpi_ratio
        screen_y_1 = (window_rect[1] * resolution[1]) + y  # * dpi_ratio
        Cursor(screen_x_1, screen_y_1)
        scroll(-200)
        time.sleep(rand_time_for_sleep)
        click(screen_x_1, screen_y_1)

        rand_num = random.randint(1,5)
        x = window_rect[2] * 0.5
        y = window_rect[3] * 0.843
        screen_x = window_rect[0] + x + rand_num  # * dpi_ratio
        screen_y = (window_rect[1] * resolution[1]) + y + rand_num  # * dpi_ratio
        Cursor(screen_x, screen_y)
        click(screen_x, screen_y)



    def Check_Notification():
        print("Закрываю уведомление если оно есть")
        for i in range(1):
            window_name = "TelegramDesktop"
            check = getWindowsWithTitle(window_name)
            telegram_window = check[0]
            window_rect_DESKTOP = (telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height)
            if window_rect_DESKTOP[2] <= 320 and window_rect_DESKTOP[3] <= 80:
                telegram_window.close()


    def RebootBlum():
        check = getWindowsWithTitle(window_name)
        telegram_window = check[0]
        randoms_time_for_choice = [0.3, 0.4, 0.5, 0.6, 0.7]
        rand_time_for_sleep = random.choice(randoms_time_for_choice)
        window_rect = (telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height)

        x = window_rect[2] * 0.784
        y = window_rect[3] * 0.645
        screen_x_1 = window_rect[0] + x  # * dpi_ratio
        screen_y_1 = (window_rect[1] * resolution[1]) + y  # * dpi_ratio
        Cursor(screen_x_1, screen_y_1)
        scroll(-200)
        time.sleep(rand_time_for_sleep)
        click(screen_x_1, screen_y_1)

        x = window_rect[2] * 0.487
        y = window_rect[3] * 0.596
        screen_x_11 = window_rect[0] + x    # * dpi_ratio
        screen_y_11 = (window_rect[1] * resolution[1]) + y   # * dpi_ratio
        Cursor(screen_x_11, screen_y_11)
        click(screen_x_11, screen_y_11)
        time.sleep(rand_time_for_sleep)

        # x = window_rect[2] * 0.487
        # y = window_rect[3] * 0.281
        # screen_x_22 = window_rect[0] + x
        # screen_y_22 = window_rect[1] + y
        # Cursor(screen_x_22, screen_y_22)
        # click(screen_x_22, screen_y_22)
        # time.sleep(10)

        rand_num = random.randint(1,5)
        rand_num_2 = random.randint(1,3)
        x = window_rect[2] * 0.5
        y = window_rect[3] * 0.843
        screen_x = (window_rect[0] + x + rand_num)    # * dpi_ratio
        screen_y = ((window_rect[1] * resolution[1]) + y + rand_num_2)    # * dpi_ratio
        Cursor(screen_x, screen_y)
        click(screen_x, screen_y)


        #############################    ######    ################################



    def click(x,y):
        mouse.position = (x, y+random.randint(1,2))
        mouse.press(Button.left)
        mouse.release(Button.left)

    window_name = "TelegramDesktop"

    INPUT_total_games = int(input(colored('\n[VALUE] | Количество игр: ','light_green')))
    INPUT_time_for_cursor = input(colored('\n[VALUE] | Введите скорость (0 - медленно; 1 - обычно; 2 - быстро): ','light_green'))

    if INPUT_time_for_cursor == "0":
        INPUT_time_for_cursor = float(1/500)
        plus_y_value = 45

    elif INPUT_time_for_cursor == "1":
        INPUT_time_for_cursor = float(1/600)
        plus_y_value = 41

    elif INPUT_time_for_cursor == "2":
        INPUT_time_for_cursor = float(1/700)
        plus_y_value = 37

    time_dirty = INPUT_total_games * 35
    hours = time_dirty // 3600
    minutes = (time_dirty % 3600) // 60

    total_time = f"{hours} часов {minutes:02d} минут"

    check = getWindowsWithTitle(window_name)
    if not check:
        print(f"[NOT WIND] | Окно - {window_name} не найдено!")
        time.sleep(1)
    else:
        tprint("Tonsco  is  GOAT")
        print(colored(f"[Tonsco] | ", "magenta"),f"Скрипт перезапускает игру каждые", colored(f"32", "light_green") ,"секунды")
        print(colored(f"[Tonsco] | ", "magenta"),f"Перерыв после 30 игр")
        print(colored(f"[Tonsco] | ", "magenta"),f"Нажмите ", colored(f"Q", "red") ," для остановки")
        print(colored(f"[Tonsco] | ", "magenta"),f"Все игры закончатся через ", colored(f"{total_time}", "light_green"))
        print(f"-------------------------------------------------")
        print(colored('---->> Ссылка на обновления | t.me/Tonsco_drops <<----', 'light_green', attrs=['blink']))
        StartBlum()
        # time.sleep(0.5)
        # print(colored(f"\n[Tonsco] | ", "magenta"),f"Ищу кнопку для запуска DropGame...", colored(f"{total_time}", "light_green"))

        start_time = time.time()

    telegram_window = check[0]
    # window_rect = (
    #     telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height
    # )
    # scrn = screenshot(region=(window_rect[0]+10, window_rect[1]+50, window_rect[2]-25, window_rect[3]-150))    # width, height = scrn.size
    # scrn.save("screenshot.png")
    # time.sleep(111)

    #############################       ПОЛУЧАЮ DPI      #####################################


    #############################      НАЧАЛО ЦИКЛА      ####################################

    restart_after_10_sec = False
    count_fake = 0

    while is_pressed('q') == False:
        window_rect = (
            telegram_window.left,telegram_window.top,telegram_window.width,telegram_window.height
        )

        if time.time() - start_time > 33 or restart_after_10_sec == True:
            if restart_after_10_sec == False:
                Total_games = Total_games + 1
                print(f"Прошло игр: {Total_games}")
            else:
                print(f"Перезапускаю игру")
                restart_after_10_sec = False
            if INPUT_total_games == Total_games:
                break
            if Total_games % 30 == 0 and Total_games != 0:
                rand_time_sleepp = random.randint(20,40)
                print(f"Перерыв {rand_time_sleepp} секунд, чтобы нас не поймали)")
                time.sleep(rand_time_sleepp)
                
            Check_Notification()
            RebootBlum()
            time.sleep(0.2)
            rand_num = random.randint(1,5)
            x = window_rect[2] * 0.5
            y = window_rect[3] * 0.843
            screen_x = (window_rect[0] + x + rand_num)    # * dpi_ratio
            screen_y = ((window_rect[1] * resolution[1]) + y + rand_num)   # * dpi_ratio
            click(screen_x, screen_y)
            time.sleep(0.2)

            count_fake = 0
            start_time = time.time()


        if telegram_window != []:
            try:
                telegram_window.activate()
            except:
                telegram_window.minimize()
                telegram_window.restore()

        scrn = screenshot(region=(window_rect[0]+10, window_rect[1]+50, window_rect[2]-25, window_rect[3]-150))

        # if time.time() - start_time > 35:
        #     scrn = screenshot(region=(window_rect[0]+10, window_rect[1]+50, window_rect[2]-25, window_rect[3]-355))

        width, height = scrn.size
        
        pixel_found = False
        if pixel_found == True:
            break

        for y in range(0, height, 20):
            for x in range(0, width, 10):
                r, g, b = scrn.getpixel((x, y))
                # if (r in range(100, 255)) and (g in range(0, 242)) and (b in range(100, 255)):
                # if (b in range(0, 90)) and (r in range(102, 200)) and (g in range(230, 255)):
                if ((b in range(37, 52)) and (r in range(199, 227)) and (g in range(97, 122))) or ((b in range(88, 121)) and (r in range(88, 177)) and (g in range(88, 177))): #rgb(227,120,52) rgb(207,100,41) rgb(138,130,130)
                    screen_x = (window_rect[0]+10 + x)   # * dpi_ratio
                    screen_y = (((window_rect[1] * resolution[1])+50 + y)+plus_y_value)    # * dpi_ratio
                    points = []
                    wind_mouse(last_x, last_y, screen_x, screen_y, move_mouse=lambda x,y: points.append([x,y]))
                    last_x = screen_x
                    last_y = screen_y
                    points = asarray(points)

                    for i in range(len(points)):
                        SetCursorPos((points[i][0], points[i][1]))
                        time.sleep(INPUT_time_for_cursor)
                    click(screen_x, screen_y)

                    pixel_found = True
                    break

            else:
                count_fake += 1
                if time.time() - start_time > 10 and time.time() - start_time < 10.6 and count_fake > 6000:
                    # print("END")
                    count_fake = 0
                    restart_after_10_sec = True




    print('[❌] | Остановлено.\n')
    time.sleep(1)
    reboot_clicker = input(colored('\n[REBOOT] | Sir, чтобы перезапустить отправьте "S": ', 'yellow'))
    if reboot_clicker == "S" or reboot_clicker == "s":
        clicker()

# clicker()