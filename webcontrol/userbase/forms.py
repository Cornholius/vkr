from django import forms
from .models import Users


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('phone_number', 'firstname', 'lastname', 'entry_counter', 'start_time', 'end_time')
        labels = {'phone_number': '',
                  'firstname': '',
                  'lastname': '',
                  'entry_counter': '',
                  'start_time': '',
                  'end_time': ''}

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20', 'placeholder': 'формат: +71234567890'}))
        self.fields['firstname'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20'}), required=False)
        self.fields['lastname'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20'}), required=False)
        self.fields['entry_counter'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20', 'placeholder': 'пусто - умолчанию 10000'}), required=False)
        self.fields['start_time'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20', 'placeholder': 'пусто - без ограничений'}), required=False)
        self.fields['end_time'] = forms.CharField(widget=forms.TextInput(attrs={'size': '20', 'placeholder': 'пусто - без ограничений'}), required=False)
