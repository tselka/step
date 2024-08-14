from django.http import HttpResponse


def home_page(request):
    """домашняя страница"""
    return HttpResponse('<html><title>иди нахуй</title></html>')
