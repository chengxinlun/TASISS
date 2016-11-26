import datetime
import pytz
import wechat.official as off


def stamp2date(timestamp):
    return datetime.datetime.fromtimestamp(
        int(timestamp)).replace(tzinfo=pytz.UTC)


def q_and_a(req):
    timestamp = req.CreateTime
    inputtime = stamp2date(timestamp)
    operation = [datetime.datetime(2016, 11, 27, 11, 30, 0, 0, pytz.UTC),
                 datetime.datetime(2016, 11, 27, 14, 0, 0, 0, pytz.UTC)]
    if inputtime < operation[0] or inputtime > operation[1]:
        return off.WxEmptyResponse(req)
    text = "欢迎来到天文夜！您需要完成的答题环节在以下连接中，" + \
        "请根据参与的项目完成相应的题目。请将至少三份得分为满分的问卷的完成" + \
        "界面截图并在奖品兑换处出示给工作人员，即可获得相应奖品。\n" + \
        '<a href="https://ks.sojump.hk/jq/10881815.aspx">' + \
        "ETX125望远镜</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10881870.aspx">' + \
        'Meade 130</a>，' + \
        '<a href="https://ks.sojump.hk/jq/10880154.aspx">' + \
        "信达小黑牛反</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10880047.aspx">' + \
        "GSO RC8望远镜</a>，" + \
        '<a href="https://ks.sojump.hk/jq/10880491.aspx">' + \
        "其他题目</a>"
    return off.WxTextResponse(text, req)
