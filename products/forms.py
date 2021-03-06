from django import forms
from .models import *
from orders.models import *


class FormSearch(forms.Form):  # Класс Form - принимает данные из запроса(в виде текстовых строк),валидирует относительно типа полей, приводит к нужному представлению на языке питон

    search = forms.CharField(required=False)  # текстовое поле, required=False - не ртебуется для успешной валидации формы
    sort = forms.ChoiceField(choices=(("auto", "auto"),("bike", "bike")), required=False )


class AddCarForm(forms.ModelForm):


    class Meta:
        model = AddCarModel
        fields = ["product_name", "price", "discription_product", "category", "image_product"] #



class ContactForm(forms.Form):
    name = forms.CharField()



class Basket(forms.ModelForm):


    class Meta:
        model = BasketModel
        fields = ["number"] #

class Likes(forms.ModelForm):


    class Meta:
        model = Product
        fields = ["likes"] #