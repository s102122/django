from django import forms
from . import DateChecker


class DateCheckForm(forms.ModelForm):
    class Meta:
	model = DateChecker
	fields('date1', 'date2', 'date3')