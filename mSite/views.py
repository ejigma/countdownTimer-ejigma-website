from django.shortcuts import render

# Create your views here.
from mSite.models import FirstPage


def web(request):
    context = {
        'data': FirstPage.objects.first(),
    }
    return render(request, 'index.html', context=context)
