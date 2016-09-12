from django.shortcuts import render
from .wxapp import WxApp

# Create your views here.
def wechat(request):
    app = WxApp()
    result = app.process(request.GET, request.body)
    return HttpResponse(result)
