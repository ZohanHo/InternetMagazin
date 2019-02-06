from django.shortcuts import render, HttpResponse, redirect

def test(request):

    return render(request, "test/test.html", context={})