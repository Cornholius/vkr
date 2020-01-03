from django.shortcuts import render, redirect, render_to_response
from django.views.generic import View
from .models import Users


class Validation_data_entry():

    def ololo(self, request):
        phone_number = str(request.POST.get("phone_number"))
        firstname = str(request.POST.get("firstname"))
        lastname = str(request.POST.get("lastname"))
        entry_counter = str(request.POST.get("entry_counter"))
        start_time = str(request.POST.get("start_time"))
        end_time = str(request.POST.get("end_time"))
        if phone_number == 'name="phone_number"' or "":
           msg = 'Поле "Номер" не может быть пустым! Введите номер телефона в формате: "+71234567890"'
           return render_to_response('home/index.html', {'users': users, 'msg': msg})
        if firstname == 'name="firstname"':
            firstname = ''
        if lastname == 'name="lastname"':
            lastname = ''
        if entry_counter == 'name="entry_counter"':
            entry_counter = ''
        if start_time == 'name="start_time"':
            start_time = ''
        if end_time == 'name="end_time"':
            end_time = ''
        return phone_number, firstname, lastname, entry_counter, start_time, end_time

class UserView(View):

    def get(self, request):
        users = Users.objects.all()
        delete_button_id = request.GET.get('delete_button_id')
        Users.objects.filter(id=delete_button_id).delete()
        return render(request, 'home/index.html', {'users': users})

    def post(self, request):
        add_button = request.POST.get("add_button_id")
        phone_number = str(request.POST.get("phone_number"))
        firstname = str(request.POST.get("firstname"))
        lastname = str(request.POST.get("lastname"))
        entry_counter = str(request.POST.get("entry_counter"))
        start_time = str(request.POST.get("start_time"))
        end_time = str(request.POST.get("end_time"))
        if phone_number == 'name="phone_number"' or "":
           msg = 'Поле "Номер" не может быть пустым! Введите номер телефона в формате: "+71234567890"'
           return render_to_response('home/index.html', {'users': users, 'msg': msg})
        if firstname == 'name="firstname"' or 'firstname':
            firstname = ''
        if lastname == 'name="lastname"' or 'lastname':
            lastname = ''
        if entry_counter == 'name="entry_counter"' or 'entry_counter':
            entry_counter = ''
        if start_time == 'name="start_time"' or 'start_time':
            start_time = ''
        if end_time == 'name="end_time"' or 'end_time':
            end_time = ''
        users = Users.objects.all()

        Users.objects.create(
            phone_number=phone_number,
            firstname=firstname,
            lastname=lastname,
            entry_counter=entry_counter,
            start_time=start_time,
            end_time=end_time)
        return render(request, 'home/index.html', {'users': users})


class EditView(View):

    def get(self, request):
        string_id = request.GET.get('edit_button_id')
        edit_user = Users.objects.filter(id=string_id)
        return render(request, 'edit/index.html', {'edit_form': edit_user})

    def post(self, request):
        button_id = request.GET.get('edit_button_id')
        phone_number = str(request.POST.get("phone_number"))
        firstname = str(request.POST.get("firstname"))
        print(firstname)
        lastname = str(request.POST.get("lastname"))
        entry_counter = str(request.POST.get("entry_counter"))
        start_time = str(request.POST.get("start_time"))
        end_time = str(request.POST.get("end_time"))
        if firstname == 'name="firstname"' or 'firstname':
            firstname = ''
        if lastname == 'name="lastname"' or 'lastname':
            lastname = ''
        if entry_counter == 'name="entry_counter"' or 'entry_counter':
            entry_counter = ''
        if start_time == 'name="start_time"' or 'start_time':
            start_time = ''
        if end_time == 'name="end_time"' or 'end_time':
            end_time = ''
        Users.objects.filter(id=int(button_id)).update(
            phone_number=phone_number,
            firstname=firstname,
            lastname=lastname,
            entry_counter=entry_counter,
            start_time=start_time,
            end_time=end_time)
        return redirect('../')

