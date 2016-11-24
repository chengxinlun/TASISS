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
        "&lt;a href=&quot;https://ks.sojump.hk/jq/10881815.aspx&quot;&gt;" + \
        "ETX125&lt;/a&gt; " + \
        "&lt;a href=&quot;https://ks.sojump.hk/jq/10881870.aspx&quot;&gt;" + \
        "Meadal130&lt;/a&gt; " + \
        "&lt;a href=&quot;https://ks.sojump.hk/jq/10880154.aspx&quot;&gt;" + \
        "EQ3D&lt;/a&gt; " + \
        "&lt;a href=&quot;https://ks.sojump.hk/jq/10880047.aspx&quot;&gt;" + \
        "GSO RC8&lt;/a&gt; " + \
        "&lt;a href=&quot;https://ks.sojump.hk/jq/10880491.aspx&quot;&gt;" + \
        "其他题目&lt;/a&gt;"
    return off.WxTextResponse(text, req)