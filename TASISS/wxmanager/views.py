from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .wxapp import WxApp
from .models import Ob_opening

# Create your views here.


# Wechat request handler
@csrf_exempt
def wechat(request):
    app = WxApp()
    result = app.process(request.GET, request.body)
    return HttpResponse(result)


@login_required()
def selectopening(request):
    opening_all = Ob_opening.objects.all()
    context = {'opening_list': opening_all}
    return render(request, 'wxmanager/selectopening.html', context)


@login_required()
def checkin(request, opening_id):
    opening = get_object_or_404(Ob_opening, pk=opening_id)
    context = {"opening": opening}
    return render(request, 'wxmanager/checkin.html', context)


@login_required()
def check(request, opening_id):
    opening = get_object_or_404(Ob_opening, pk=opening_id)
    try:
        openid = request.POST['openid']
    except Exception:
        context = {'opening': opening, 'error_message': 'Malformed post'}
        return render(request, 'wxmanager/checkin.html', context)
    else:
        # If the stored name is not openid, chang this part
        register_name = openid
        # The rest should be left unchanged
        register = opening.register_set.filter(openid=register_name).first()
        if register is None:
            # Not registered
            context = {'opening': opening,
                       'error_message': 'Not registered'}
            return render(request, 'wxmanager/checkin.html', context)
        else:
            isChecked = register.signed
            if isChecked != 0:
                # Repeated checkin
                context = {'opening': opening,
                           'error_message': 'Repeated checkin'}
                return render(request, 'wxmanager/checkin.html', context)
            else:
                # Successful checkin
                register.signed += 1
                register.save()
                context = {'opening': opening,
                           'error_message': 'Successful checkin'}
                return render(request, 'wxmanager/checkin.html', context)
