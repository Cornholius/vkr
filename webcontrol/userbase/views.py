from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Users
from .forms import UserForm
# import RPi.GPIO as GPIO
import re
from time import sleep
import datetime


class UserView(View):

    def delete_from_sms(self, request):
        phone_number = request.GET.get('phone_number')
        Users.objects.filter(phone_number=phone_number).delete()

    def open_from_sms(self, request):
        phone_number = request.GET.get('phone_number')
        user = Users.objects.filter(phone_number=phone_number).first()
        time_with = Users.objects.get(phone_number=phone_number).start_time
        time_to = Users.objects.get(phone_number=phone_number).end_time
        entry_counter = Users.objects.get(phone_number=phone_number).entry_counter
        time_now = datetime.datetime.now().strftime('%H')
        if time_with == '': time_with = 0
        if time_to == '': time_to = 24
        if entry_counter == '': entry_counter = -1
        if user is not None:
            if int(time_with) < int(time_now) < int(time_to):
                if int(entry_counter) > 0:
                    count = int(entry_counter)
                    count -= 1
                    Users.objects.filter(phone_number=phone_number).update(entry_counter=count)
                # GPIO.setmod(GPIO.BCM)
                # GPIO.setup(24, GPIO.OUT)
                # GPIO.output(7, True)
                # sleep(0.5)
                # GPIO.output(7, False)
                # GPIO.cleanup()
                print("test passed")

        else:
            print('заглушка: нет в списке')

    def get(self, request):
        if request.GET.get('delete_from_sms') == 'del':
            self.delete_from_sms(request)
        if request.GET.get('open_from_phone') == 'open':
            self.open_from_sms(request)
        users = Users.objects.all()
        delete_button_id = request.GET.get('delete_button_id')
        Users.objects.filter(id=delete_button_id).delete()
        return render(request, 'home/index.html', {'users': users, 'add_user': UserForm})

    def post(self, request):
        print(request.POST)
        print(request.POST.get('sms_add_user'))
        users = Users.objects.all()
        phone_number = request.POST.get("phone_number")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        entry_counter = request.POST.get("entry_counter")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        check_number = re.match(r'^[+]{1}[0-9]{11}$', phone_number)
        if check_number is None:
            return render(request, 'home/index.html',
                          {'users': users,
                           'add_user': UserForm,
                           'data_entry_error': 'Запись не добавлена. Проверьте правильность ввода номера'})
        try:
            if phone_number == Users.objects.get(phone_number=phone_number).phone_number:
                return render(request, 'home/index.html',
                              {'users': users,
                               'add_user': UserForm,
                               'data_entry_error': 'Такой номер уже есть в базе'})
        except:
            Users.objects.create(
                phone_number=phone_number,
                firstname=firstname,
                lastname=lastname,
                entry_counter=entry_counter,
                start_time=start_time,
                end_time=end_time)
            return render(request, 'home/index.html',
                          {'users': users,
                           'add_user': UserForm})


class EditView(View):

    def get(self, request):
        edit_user = Users.objects.filter(id=request.GET.get('edit_button_id'))
        form = UserForm(edit_user.values()[0])
        return render(request, 'edit/index.html', {'edit_form': form})

    def post(self, request):
        button_id = request.GET.get('edit_button_id')
        phone_number = str(request.POST.get("phone_number"))
        firstname = request.POST.get("firstname")
        lastname = str(request.POST.get("lastname"))
        entry_counter = str(request.POST.get("entry_counter"))
        start_time = str(request.POST.get("start_time"))
        end_time = str(request.POST.get("end_time"))
        if Users.objects.get(phone_number=phone_number).id == int(button_id):
            Users.objects.filter(id=int(button_id)).update(
                phone_number=phone_number,
                firstname=firstname,
                lastname=lastname,
                entry_counter=entry_counter,
                start_time=start_time,
                end_time=end_time)
            return redirect('../')
        else:
            edit_user = Users.objects.filter(id=request.GET.get('edit_button_id'))
            form = UserForm(edit_user.values()[0])
            return render(request, 'edit/index.html', {'edit_form': form,
                                                       'data_entry_error': 'Вы пытаетесь создать в базе две'
                                                                           ' записи с одинаковым номером.'})
