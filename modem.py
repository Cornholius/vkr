from gsmmodem.modem import GsmModem


class BarrierControl(GsmModem):

    def __init__(self):
        self.PORT = 'COM5'
        self.BAUDRATE = 115200

    def sms_catcher(self, sms):
        print("ЗАГЛУШКА(sms): отправить сигнал на GPIO")

    def call_catcher(self, call):
        print("ЗАГЛУШКА(call): отправить сигнал на GPIO")

    def main(self):
        print('Initializing modem...')
        modem = GsmModem(self.PORT, self.BAUDRATE,
                         smsReceivedCallbackFunc=self.sms_catcher,
                         incomingCallCallbackFunc=self.call_catcher)
        modem.smsTextMode = False
        modem.connect()
        print('Waiting for SMS or Call...')
        try:
            modem.rxThread.join()
        finally:
            modem.close()


BarrierControl().main()
