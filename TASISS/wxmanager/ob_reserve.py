import datetime
import io
import PIL
import pytz
import qrcode
from .models import Ob_opening
import wechat.official as off
from wechat.models import WxImage


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
            return [False, None]
        # This is the part where a license number will be generated
        name = str(openid)
        # The simpler the better
        opening.register_set.create(openid=name, signed=0)
        return [True, name]
    else:
        return [False, name]


def ob_reserve(req, Api):
    timestamp = req.CreateTime
    openid = req.FromUserName
    inputtime = stamp2date(timestamp)
    opening = get_opening(inputtime)
    if opening is None:
        return off.WxTextResponse(u"抱歉，现在不是预约时间", req)
    else:
        return_res = reserve(opening, openid)
        if return_res[0]:
            img = qrcode.make(return_res[1])
            imgba = io.BytesIO()
            img.save(imgba, format='JPEG')
            imgba = imgba.getvalue()
            imginfo = {"media_content": imgba}
            media_id = Api._get_media_id(imginfo, 'media', 'image')
            if media_id is None:
                return off.WxTextResponse(return_res[1], req)
            else:
                return off.WxImageResponse(WxImage(MediaId=media_id), req)
        else:
            return off.WxTextResponse(u"预约名额已满或您在重复预约", req)
