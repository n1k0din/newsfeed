from django.shortcuts import render


def show_feed(request):
    return render(request, 'index.html')
