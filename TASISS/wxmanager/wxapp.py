from wechat.official import WxApplication, WxTestResponse
from ob_reserve import ob_reserve
from django.http import HttpResponse


class WxApp(WxApplication):

    SECRET_TOKEN = 'test_token'
    WECHAT_APPID = 'taswx00'
    WECHAT_APPSECRET = 'lianren'
    ENCODING_AES_KEY = None
    UNSUPPORT_TXT = u'暂不支持此类型消息'
    WELCOME_TXT = u'你好！感谢您的关注！'


    def on_text(self, req):
        if req.content == u'ob reserve':
            result= ob_reserve(req)            
            return result
        else:
            return WxTextResponse(self.UNSUPPORT_TXT, req)        
