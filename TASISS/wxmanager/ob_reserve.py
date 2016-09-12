import datetime
import pytz
from .models import Ob_opening
import wechat.official as off


def stamp2date(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)
                                           ).replace(tzinfo=pytz.UTC)


def get_opening(inputtime):
    opening_list = Ob_opening.objects.all()
    for each in opening_list:
        start_time = each.starttime
        end_time = each.endtime
        if inputtime < end_time and inputtime > start_time:
            return each
    return None


def check_repeat(opening, openid):
    existing = opening.register_set.all()
    for each in existing:
        if each.openid == openid:
            return True
    return False


def reserve(opening, openid):
    if opening.max_num - opening.register_set.count() > 0:
        if check_repeat(opening, openid):
            return False
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
    # timestamp = req["CreateTime"]
    # openid = req["FromUserName"]
    inputtime = stamp2date(timestamp)
    opening = get_opening(inputtime)
    if opening is None:
        # return "not time"
        return off.WxTestResponse(u"抱歉，现在不是预约时间", req)
    else:
        if (reserve(opening, openid)):
            # return "success"
            return off.WxTestResponse(str(openid), req)
        else:
            # return "full"
            return off.WxTestResponse(u"预约名额已满或您在重复预约", req)
