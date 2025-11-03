from django.shortcuts import render

def home_view(request):
    return render(request, 'mainapp/home.html')

def about_view(request):
    return render(request, 'mainapp/about.html')
