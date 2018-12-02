from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import *
from .models import *
from django.views.generic import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import *
from django.urls import reverse_lazy
import datetime
from orders.models import *
from products.models import *
from django.http import JsonResponse
from django.shortcuts import resolve_url



class ListViewLanding(ListView):
    model = ProductImages
    template_name = "home.html"


    def dispatch(self, request, *args, **kwargs):  # dispath определяет с каким запросом к нам прилетел запрос
        # Создаем переменную в которую кладем весь масив request.GET, а именно даннные которые пришли от пользователя в строке запроса,
        # будем с request.GET брать наш search и sort
        self.form = FormSearch(request.GET)
        # метод проверяет соответствуют ли данные той форме которую мы прописали, после чего можем оперировать таким атрибутом как cleaned_data
        self.form.is_valid()
        #
        self.search = ProductImages(request.POST or None)  # Создали переменную для работы с POST, используется когда fprm.modelform
        return super(ListViewLanding, self).dispatch(request, *args, **kwargs)  # после чего вызываем super, что бы функция работала стандартно


    def get_context_data(self, **kwargs):

        querys = ProductImages.objects.all()

        queryset = ProductImages.objects.filter(product_image__category__name__iexact="bike")
        #auto = ProductImages.objects.filter(product_image__category__name__iexact="auto")


        if self.form.cleaned_data.get("search"):  # Проверям засабмичен ли с формы search
            # при поске можно сортировать по нескольким полям, но запятая ето как and, поиск будет осуществлен, с условием чтобы запрос был
            # найден одновременно в двух полях, для отдельного поиска нужно использовать класс Q, указав опера (| или)
            queryset = querys.filter(Q(product_image__product_name__icontains=self.form.cleaned_data["search"]) | Q(product_image__discription_product__icontains=self.form.cleaned_data["search"]))  # если да, то фильтруем
        if self.form.cleaned_data.get("sort"):  #
            queryset = querys.order_by(self.form.cleaned_data["sort"])

        paginator = Paginator(queryset, 12)  # сортируем по 3 обьекта в queryset

        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""

        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewLanding, self).get_context_data(**kwargs)  # вызываем метод у родителя и добавляем контекст который нужен
        context["form"] = self.form  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["search"] = self.search  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url
        return context

class ListViewLandingAuto(ListView):
    model = ProductImages
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):  # dispath определяет с каким запросом к нам прилетел запрос
        # Создаем переменную в которую кладем весь масив request.GET, а именно даннные которые пришли от пользователя в строке запроса,
        # будем с request.GET брать наш search и sort
        self.form = FormSearch(request.GET)
        # метод проверяет соответствуют ли данные той форме которую мы прописали, после чего можем оперировать таким атрибутом как cleaned_data
        self.form.is_valid()
        #
        self.search = ProductImages(
            request.POST or None)  # Создали переменную для работы с POST, используется когда fprm.modelform
        return super(ListViewLandingAuto, self).dispatch(request, *args,
                                                     **kwargs)  # после чего вызываем super, что бы функция работала стандартно

    def get_context_data(self, **kwargs):
        #queryset = ProductImages.objects.all()  # filter(product_image__category__name__iexact="bike")
        #bike = ProductImages.objects.filter(product_image__category__name__iexact="bike")
        queryset = ProductImages.objects.filter(product_image__category__name__iexact="auto")
        querys = ProductImages.objects.all()


        if self.form.cleaned_data.get("search"):  # Проверям засабмичен ли с формы search
            # при поске можно сортировать по нескольким полям, но запятая ето как and, поиск будет осуществлен, с условием чтобы запрос был
            # найден одновременно в двух полях, для отдельного поиска нужно использовать класс Q, указав опера (| или)
            queryset = querys.filter(
                Q(product_image__product_name__icontains=self.form.cleaned_data["search"]) | Q(
                    product_image__discription_product__icontains=self.form.cleaned_data[
                        "search"]))  # если да, то фильтруем
        if self.form.cleaned_data.get("sort"):  #
            queryset = querys.order_by(self.form.cleaned_data["sort"])

        paginator = Paginator(queryset, 12)  # сортируем по 3 обьекта в queryset

        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""

        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewLandingAuto, self).get_context_data(
            **kwargs)  # вызываем метод у родителя и добавляем контекст который нужен
        context["form"] = self.form  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["search"] = self.search  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url


        return context



# def landing(request):
#     #products = Product.objects.filter(is_active=True) #Фильтруем отображая только активные
#     image = ProductImages.objects.all()
#     return render(request, "home.html", context={"image": image})  # locals() - отображает все переменные которые есть в контекст

class LandingDetailView(DetailView):
    model = ProductImages
    template_name = "card_detail.html"

    def dispatch(self, request, *args, **kwargs):
        return super(LandingDetailView, self).dispatch(request, *args, **kwargs)



class AddCarView(CreateView):
    model = AddCarModel
    template_name = "AddCar.html"
    fields = ["product_name", "price", "discription_product", "category", "image_product"] #

    # Мметод который возвращает url на который мы редиректим пользователся при успешной валидации формы
    #def get_success_url(self):
        #return resolve_url("detail_new_car_url", pk=self.object.pk)


class AddDetailView(DetailView):
    model = AddCarModel
    template_name = "NrwCar.html"


class ListViewNewAuto(ListView):
    model = AddCarModel
    template_name = "NewCarList.html"

    def dispatch(self, request, *args, **kwargs):  # dispath определяет с каким запросом к нам прилетел запрос
        # Создаем переменную в которую кладем весь масив request.GET, а именно даннные которые пришли от пользователя в строке запроса,
        # будем с request.GET брать наш search и sort

        self.form = FormSearch(request.GET)
        # метод проверяет соответствуют ли данные той форме которую мы прописали, после чего можем оперировать таким атрибутом как cleaned_data
        self.form.is_valid()
        #
        self.search = ProductImages(request.POST or None)  # Создали переменную для работы с POST, используется когда fprm.modelform

        return super(ListViewNewAuto, self).dispatch(request, *args,**kwargs)  # после чего вызываем super, что бы функция работала стандартно

    def get_context_data(self, **kwargs):
        #queryset = ProductImages.objects.all()  # filter(product_image__category__name__iexact="bike")
        #bike = ProductImages.objects.filter(product_image__category__name__iexact="bike")
        queryset = AddCarModel.objects.filter(category__name__iexact="auto")
        querys = AddCarModel.objects.all()


        if self.form.cleaned_data.get("search"):  # Проверям засабмичен ли с формы search
            # при поске можно сортировать по нескольким полям, но запятая ето как and, поиск будет осуществлен, с условием чтобы запрос был
            # найден одновременно в двух полях, для отдельного поиска нужно использовать класс Q, указав опера (| или)
            queryset = querys.filter(
                Q(product_name__icontains=self.form.cleaned_data["search"]) | Q(
                    discription_product__icontains=self.form.cleaned_data[
                        "search"]))  # если да, то фильтруем
        if self.form.cleaned_data.get("sort"):  #
            queryset = querys.order_by(self.form.cleaned_data["sort"])

        paginator = Paginator(queryset, 12)  # сортируем по 3 обьекта в queryset

        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)

        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = "?page={}".format(page.previous_page_number())
        else:
            prev_url = ""

        if page.has_next():
            next_url = "?page={}".format(page.next_page_number())
        else:
            next_url = ""

        context = super(ListViewNewAuto, self).get_context_data(
            **kwargs)  # вызываем метод у родителя и добавляем контекст который нужен
        context["form"] = self.form  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["search"] = self.search  # добавляем нашу форму, кторая потом доступна в шаблоне
        context["page"] = page
        context["is_paginated"] = is_paginated
        context["prev_url"] = prev_url
        context["next_url"] = next_url

        return context

class CarUpdateViwe(UpdateView):
    model = AddCarModel
    fields = ["product_name", "price", "discription_product", "category", "image_product"]
    template_name = "Update_car.html"



class CarDeleteView(DeleteView):
    model = AddCarModel
    success_url = reverse_lazy('list_new_auto_url')
    template_name = "Delete_car.html"




class TestView(TemplateView):
    template_name = "test.html"

    def dispatch(self, request, *args, **kwargs):

        self.date = datetime.datetime.now()
        print(request.GET)
        self.name = request.GET.get('name')
        self.session_key = request.session.session_key
        print(request.POST)
        self.csrf = request.GET.get('csrfmiddlewaretoken')
        return super(TestView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context ["data"] = self.date
        context ["csrf"] = self.csrf
        context ["key"] =  self.session_key

        return context

def Basket(request):

    # Через POST можно вытянуть то что передажи в ajax
    new_car_price = request.POST.get('new_car_price')
    new_car_name = request.POST.get('new_car_name')
    product_id = request.POST.get('product_id')
    session_key = request.POST.get('session_key')
    #number = BasketModel.objects.get("number")


    #price = float(new_car_price.split(",")[0])

    #return_dict = dict()

    # делаем новый продукт кторый будем сохранять в базу create

    # new_product = BasketModel.objects.create(session_key=session_key, product_name = new_car_name) #price=new_car_price
    # num = new_product.number

    # тест

    number = 1
    new_product, created = BasketModel.objects.update_or_create(session_key=session_key, product_name=new_car_name,
                                                             defaults={"number": number, "price" : new_car_price})

    # такой конструкцией увиличиваем количество в базе
    if not created:
        new_product.number += number
        new_product.save()





    #if new_product:
        #good = "Product in Basket"
        #return_dict['good'] = good
    # для обновления и создания
    #BasketModel.objects.update_or_create(session_key=session_key, product_name = new_car_name)

    # для проверки есть ли и обновления используется
    # naw_product, create = BasketModel.objects.get_or_create(session_key=session_key, product_name = new_car_name, defaults{})
    # если такая запись есть то ничего не делаем, если нету то создаем такую запись + то что в дефолте


    # считываем количество, которое потом будем отображать в корзине
    products_total = BasketModel.objects.filter(session_key=session_key, is_active=True)
    products_total_num = products_total.count()
    #num = BasketModel.objects.filter("number")




    queryset = BasketModel.objects.all()




    # Поместив в словарь которы передаем в rcdesponse можем потом использовать в data в js
    #return_dict['products_total_num'] = products_total_num



    #return_dict['number'] = BasketModel.objects.get("number")
    #num = BasketModel.objects.filter("number")


    return render(request, "basket.html", context={"products_total_num" : products_total_num, "queryset": queryset, "number": number})
    #return JsonResponse(return_dict)