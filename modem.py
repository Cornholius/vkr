from __future__ import print_function
from gsmmodem.modem import GsmModem
import requests


PORT = 'COM5'
BAUDRATE = 115200


def sms_catcher(sms):
    if sms.text == 'open':  #  Отправить сигнал на GPIO
        pass

    if sms.text == 'add':   #   регуляркой отделить add  и номер. в словарь передать номер
        url = 'http://127.0.0.1/'
        client = requests.session()
        client.get(url)
        csrftoken = client.cookies['csrftoken']
        login_data = {'phone_number': sms.number, 'firstname': '', 'lastname': '', 'entry_counter': '',
                      'start_time': '', 'end_time': '', 'csrfmiddlewaretoken': csrftoken}
        r = client.post(url, data=login_data)

    if sms.text == 'del':   #   доделать удаление из базы



def call_catcher(call):
    print("ЗАГЛУШКА(call): отправить сигнал на GPIO")


def main():
    print('Initializing modem...')
    modem = GsmModem(PORT, BAUDRATE,
                     smsReceivedCallbackFunc=sms_catcher,
                     incomingCallCallbackFunc=call_catcher)
    modem.smsTextMode = False
    modem.connect()
    print('Waiting for SMS or Call...')
    try:
        modem.rxThread.join()
    finally:
        modem.close()


main()
