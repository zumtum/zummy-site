from django.shortcuts import render

def index(request):
    return render(request, 'landing/index_page.html', {})