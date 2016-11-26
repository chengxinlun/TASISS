import datetime
import pytz
import wechat.official as off


def stamp2date(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).replace(tzinfo=pytz.UTC)


def q_and_a(req):
    timestamp = req.CreateTime
    inputtime = stamp2date(timestamp)
    text = "欢迎来到天文夜！您需要完成的答题环节在以下连接中，" + \
        "请根据参与的项目完成相应的题目。完成后将获得相应奖励。" + \
        '<a href="https://ks.sojump.hk/jq/10881815.aspx">' + \
        "ETX125</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10881870.aspx">' + \
        'Meadal130</a>，' + \
        '<a href="https://ks.sojump.hk/jq/10880154.aspx">' + \
        "EQ3D</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10880047.aspx">' + \
        "GSO RC8</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10880491.aspx">' + \
        "其他题目</a>"
    return off.WxTextResponse(text, req)
