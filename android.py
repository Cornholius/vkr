from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout


class MyApp(App):

    def send_sms(self, *args):
        print("ЗАГЛУШКА: сделать отправку смс")
    def build(self):
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        open_button = Button(text='Open', size_hint=(.4, .4), on_press=self.send_sms)
        anchor_layout.add_widget(open_button)
        return anchor_layout


MyApp().run()
