from django import forms
from .models import *


class FormSearch(forms.Form):  # Класс Form - принимает данные из запроса(в виде текстовых строк),валидирует относительно типа полей, приводит к нужному представлению на языке питон

    search = forms.CharField(required=False)  # текстовое поле, required=False - не ртебуется для успешной валидации формы
    sort = forms.ChoiceField(choices=(("auto", "auto"),("bike", "bike")), required=False )





