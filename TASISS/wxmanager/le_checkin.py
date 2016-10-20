import datetime
import pytz
from .models import Ob_opening
from .ob_reserve import stamp2date
import wechat.official as off


def get_opening(inputtime):
    return Ob_opening.objects.filter(startcheckin__lt=inputtime, endcheckin__gt=inputtime).first()


def checkin(opening, openid, checkintime):
    # If the stored name is changed, please change this part
    register_name = openid
    # The rest should remain unchanged
    register = opening.register_set.filter(openid=register_name).first()
    if register is None:
        return u"您未预约讲座"
    else:
        if register.signed == 0:
            register.signed += 1
            register.save()
            return u"您于" + checkintime + "签到成功"
        else:
            return u"您在重复签到。"


def le_checkin(req):
    timestamp = req.CreateTime
    openid = req.FromUserName
    inputtime = stamp2date(timestamp)
    opening = get_opening(inputtime)
    if opening is None:
        return off.WxTextResponse(u"抱歉，现在不是签到时间", req)
    else:
        checkintime = inputtime.astimezone(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
        response_text = checkin(opening, openid, checkintime)
        return off.WxTextResponse(response_text, req)
