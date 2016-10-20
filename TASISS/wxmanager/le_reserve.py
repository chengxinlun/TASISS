import datetime
import pytz
from .models import Ob_opening
import wechat.official as off


def stamp2date(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).replace(tzinfo=pytz.UTC)


def get_opening(inputtime):
    return Ob_opening.objects.filter(starttime__lt=inputtime, endtime__gt=inputtime).first()


def check_repeat(opening, openid):
    existing = opening.register_set.filter(openid=openid).first()
    if existing is None:
        return False
    else:
        return True


def reserve(opening, openid, inputtime):
    if opening.max_num - opening.register_set.count() > 0:
        if check_repeat(opening, openid):
            return u"您在重复预约"
        # This is the part where a license number will be generated
        name = str(openid)
        # The simpler the better
        opening.register_set.create(openid=name, signed=0)
        reservetime = inputtime.astimezone(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
        startcheckin = opening.startcheckin.astimezone(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
        endcheckin = opening.endcheckin.astimezone(pytz.timezone("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M:%S")
        return u"您于"+ reservetime + "预约讲座，请您于" + startcheckin + "至" + endcheckin +"到达讲座地点。参观前工作人员会要求您发送验证信息至本公众号，以便确认您的预约。"
    else:
        return u"预约名额已满"


def le_reserve(req):
    timestamp = req.CreateTime
    openid = req.FromUserName
    inputtime = stamp2date(timestamp)
    opening = get_opening(inputtime)
    if opening is None:
        return off.WxTextResponse(u"抱歉，现在不是预约时间", req)
    else:
        response_text = reserve(opening, openid, inputtime)
        return off.WxTextResponse(response_text, req)
