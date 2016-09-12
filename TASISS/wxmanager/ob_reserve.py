import datetime
import hashlib
from .models import Ob_opening
from wechat.official import WxApplication, WxTestResponse, WxImageResponse


def stamp2date(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp))


def get_opening(inputtime):
    opening_list = Ob_opening.objects.all
    for each in opening_list:
        start_time = each.starttime
        end_time = each.endtime
        if inputtime < end_time and inputtime > start_time:
            return each
    return None


def reserve(opening, openid):
    if opening.available > 0:
        opening.available = opening.available - 1
        # This is the part where a license number will be generated
        name = str(openid)
        # The simpler the better
        opening.register_set.create(openid=name, signed=0)
        return True
    else:
        return False


def ob_reserve(req):
    timestamp = req.CreateTime
    openid = req.FromUserName
    inputtime = stamp2date(timestamp)
    opening = get_opening(inputtime)
    if opening == None:
        return WxTestResponse(u"抱歉，现在不是预约时间", req)
    else:
        if (reserve(opening, openid)):
            return WxTestResponse(str(openid), req)
        else:
            return WxTestResponse(u"可惜，预约名额已满", req)
