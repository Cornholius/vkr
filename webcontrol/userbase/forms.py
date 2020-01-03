from django import forms


class UserForm(forms.Form):
    phone_number = forms.CharField(label='Номер', widget=forms.TextInput(attrs={'size': '40'}))
    firstname = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'size': '40'}))
    lastname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'size': '40'}))
    entry_counter = forms.CharField(label='Кол-во въездов', widget=forms.TextInput(attrs={'size': '40'}))
    start_time = forms.CharField(label='Время С', widget=forms.TextInput(attrs={'size': '40'}))
    end_time = forms.CharField(label='Вредя До', widget=forms.TextInput(attrs={'size': '40'}))
