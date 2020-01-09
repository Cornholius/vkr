from __future__ import print_function
from gsmmodem.modem import GsmModem
import RPi.GPIO as GPIO
from time import sleep
import requests
import re


PORT = 'COM5'
BAUDRATE = 115200


def sms_open_barrier(sms):

    """проверить работу функции. отправляет запрос в джанго, там вьюха перехватывает,
        сверяет в базе время и номер, если всё совпадает - открывает шлагбаум"""

    url = 'http://127.0.0.1/'
    number = sms.number
    params = {'open_from_sms': 'open', 'phone_number': number}
    r = requests.get(url=url, params=params)
    # GPIO.setmod(GPIO.BCM)
    # GPIO.setup(24, GPIO.OUT)
    # GPIO.output(7, True)
    # sleep(0.5)
    # GPIO.output(7, False)
    # GPIO.cleanup()


def sms_add_user(sms):
    url = 'http://127.0.0.1/'
    client = requests.session()
    client.get(url)
    csrftoken = client.cookies['csrftoken']
    login_data = {'phone_number': sms.text[4:], 'firstname': '', 'lastname': '', 'entry_counter': '',
                  'start_time': '', 'end_time': '', 'csrfmiddlewaretoken': csrftoken}
    r = client.post(url, data=login_data)


def sms_del_number(check_del_number):
    url = 'http://127.0.0.1/'
    number = check_del_number.group(0)
    params = {'delete_from_sms': 'del', 'phone_number': number[4:]}
    r = requests.get(url=url, params=params)


def sms_catcher(sms):
    check_open_barrier = sms.text
    check_add_number = re.match(r'^Add\s{1}[+]{1}[0-9]{11}$', sms.text)
    check_del_number = re.match(r'^Del\s{1}[+]{1}[0-9]{11}$', sms.text)

    if check_open_barrier == 'Open' or 'open':
        sms_open_barrier(sms)

    if check_add_number != None:
        sms_add_user(sms)

    if check_del_number != None:
        sms_del_number(check_del_number)


# def call_catcher(call):
#     print("ЗАГЛУШКА(call): отправить сигнал на GPIO")


def main():
    print('Initializing modem...')
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=sms_catcher)
                     # incomingCallCallbackFunc=call_catcher)
    modem.smsTextMode = False
    modem.connect()
    print('Waiting for SMS or Call...')
    try:
        modem.rxThread.join()
    finally:
        modem.close()


main()
