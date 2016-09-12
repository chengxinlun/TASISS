import wechat.official as off
from .ob_reserve import ob_reserve


class WxApp(off.WxApplication):

    SECRET_TOKEN = 'test_token'
    WECHAT_APPID = 'taswx00'
    WECHAT_APPSECRET = 'lianren'
    ENCODING_AES_KEY = None
    UNSUPPORT_TXT = u'暂不支持此类型消息'
    WELCOME_TXT = u'你好！感谢您的关注！'

    def on_text(self, req):
        if req.content == u'ob reserve':
            result = ob_reserve(req)
            return result
        else:
            return off.WxTextResponse(self.UNSUPPORT_TXT, req)


'''
class WxApp:
    def process(self, a, b):
        req = {"CreateTime": "1474156800", "FromUserName": "00000000001"}
        print(ob_reserve(req))
'''
