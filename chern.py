# import time
# for i in range(100):
#     print(1000)
#     time.sleep(0.1)
# print(000)

# import random

# a = random.randint(1,5)

# bbb = 1
# print(bbb/10000)

# from uuid import getnode
# print(getnode())

# import uuid

# # Генерируем уникальный идентификатор
# unique_key = str(uuid.uuid4())

# # Пример вывода ключа
# print(f"Уникальный ключ для exe файла: {unique_key}")

# """ Добавляем его как свободный """

# """ Проверяем наличее такого свободного ключа OR Проверяем наличее такого ключа у юзера """

# """ Подсасываем его к Юзеру ЕСЛИ ЕГО НЕТ"""

# a = 123

# time_hour = a // 60
# time_min = a % 60
# total_time = f"{time_hour} час(а) {time_min} минут"
# print(total_time)

# import psutil
# # Iterate over all the keys in the dictionary
# for interface in psutil.net_if_addrs():
#     if psutil.net_if_addrs()[interface][0].address:
#         print(psutil.net_if_addrs()[interface][0].address)


from subprocess import check_output
from random import randint
from psutil import cpu_freq, cpu_count
from platform import uname


def correct_size(bts, ending='iB'):
    size = 1024
    for item in ["", "K", "M", "G", "T", "P"]:
        if bts < size:
            return f"{bts:.2f}{item}{ending}"
        bts /= size


def creating_file():
    collect_info_dict = dict()
    if 'info' not in collect_info_dict:
        collect_info_dict['info'] = dict()
        collect_info_dict['info']['system_info'] = dict()
        collect_info_dict['info']['system_info'] = {'system': {'comp_name': uname().node,
                                                               'os_name': f"{uname().system} {uname().release}",
                                                               'version': uname().version,
                                                               'machine': uname().machine},
                                                    'processor': {'name': uname().processor,
                                                                  'phisycal_core': cpu_count(logical=False),
                                                                  'all_core': cpu_count(logical=True),
                                                                  'freq_max': f"{cpu_freq().max:.2f}Мгц"}}


    return collect_info_dict


def win_dop_info(dict_info):
    import windows_tools.product_key


    prod_com = 'WMIC BASEBOARD GET Product /VALUE'.split()
    try:
        product = str(check_output(prod_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]
    except:
        product = randint(12312, 345551525531453)
    

    # processor info
    proc_name_com = 'WMIC CPU GET Name /VALUE'.split()
    processor_name = str(check_output(proc_name_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]

    proc_id_com = 'WMIC CPU GET ProcessorId /VALUE'.split()
    processor_id = str(check_output(proc_id_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]

    # system info from SMBIOS
    uuid_sys_com = 'WMIC CSPRODUCT GET UUID /VALUE'.split()
    uuid_system = str(check_output(uuid_sys_com, shell=True)).split("\\n")[2].split("\\r")[0].split("=")[1]



    if 'other_info' not in dict_info['info']:
        dict_info['info']['other_info'] = dict()
        dict_info['info']['other_info'] = {'processor_name': processor_name,
                                           'processor_id': processor_id,
                                           'uuid_system': uuid_system,
                                           'motherboard_product': product,}

    return dict_info


def print_dop_info(dict_info_dop):
    for item in dict_info_dop['info']:
        if item == "other_info":
            processor_id = "non"
            uuid_system = "non"
            processor_name = "non"
            disk = "non"
            motherboard_product = "non"

            for elem in dict_info_dop['info'][item]:
                if elem == 'processor_id':
                    processor_id = dict_info_dop['info'][item][elem]
                elif elem == 'uuid_system':
                    uuid_system = dict_info_dop['info'][item][elem]
                elif elem == 'processor_name':
                    processor_name = dict_info_dop['info'][item][elem]
                elif elem == 'motherboard_product':
                    try:
                        motherboard_product = dict_info_dop['info'][item][elem]
                    except:
                        motherboard_product = randint(12312, 345551525531453)
                
            total = f"{processor_id}__{uuid_system}__{processor_name}__{motherboard_product}"
            return total



def main():
    if uname().system == "Windows":
        dict_info = creating_file()
        dict_info_dop = win_dop_info(dict_info)
        return print_dop_info(dict_info_dop)
    elif uname().system == "Linux":
        dict_info = creating_file()
        dict_info_dop = win_dop_info(dict_info)
        return dict_info_dop


if __name__ == "__main__":
    main()