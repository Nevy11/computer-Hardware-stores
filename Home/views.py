from django.http import HttpResponse
from django.template import loader
from django.conf import settings

def home(request):
    template = loader.get_template('home.html')
    CompanyName = "Rusty"
    email = "rusty224@gmail.com"
    phoneNumber = "0792700138"
    MEDIA_URL = settings.MEDIA_URL
    context = {
        "cname": CompanyName,
        "email": email,
        "phoneNumber": phoneNumber,
        "MEDIA_URL": MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))

def test(request):
    template = loader.get_template('test.html')
    MEDIA_URL = settings.MEDIA_URL
    context = {
        "MEDIA_URL": MEDIA_URL,
    }
    return HttpResponse(template.render(context, request))