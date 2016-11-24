import wechat.official as off
from .ob_reserve import ob_reserve
from .ob_checkin import ob_checkin
from .le_reserve import le_reserve
from .le_checkin import le_checkin
from .q_and_a import q_and_a


class WxApp(off.WxApplication):

    SECRET_TOKEN = 'chengxinlun'
    WECHAT_APPID = 'wxa82797bd3ebf1281'
    WECHAT_APPSECRET = '9b17411116a08143a177537a0c851646'
    ENCODING_AES_KEY = None
    UNSUPPORT_TXT = u'您的消息已收到，转为人工服务'
    WELCOME_TXT = u'欢迎参加测试'

    def on_text(self, req):
        if req.Content == u'天文台预约':
            result = ob_reserve(req)
        elif req.Content == u'天文台签到':
            result = ob_checkin(req)
        elif req.Content == u'讲座预约':
            result = le_reserve(req)
        elif req.Content == u'讲座签到':
            result = le_checkin(req)
        elif req.content == u'天文夜答题':
            result = q_and_a(req)
        else:
            result = off.WxEmptyResponse(req)
        return result
