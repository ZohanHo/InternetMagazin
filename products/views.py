from django.shortcuts import render, HttpResponse
from django.views.generic import *
from .models import *
from django.views.generic import *
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import *

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

