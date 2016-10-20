import wechat.official as off
from .ob_reserve import ob_reserve
from .ob_checkin import ob_checkin


class WxApp(off.WxApplication):

    SECRET_TOKEN = 'chengxinlun'
    WECHAT_APPID = 'wx958984c33a0f4d2b'
    WECHAT_APPSECRET = '2bdb1b2766ca818ebf8538e3d104af90'
    ENCODING_AES_KEY = None
    UNSUPPORT_TXT = u'您的消息已收到，转为人工服务'
    WELCOME_TXT = u'欢迎参加测试'

    def on_text(self, req):
        if req.Content == u'天文台预约':
            result = ob_reserve(req)
        elif req.Content == u'天文台签到':
            result = ob_checkin(req)
        else:
            result = off.WxTextResponse(self.UNSUPPORT_TXT, req)
        return result
