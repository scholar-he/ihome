#coding=utf-8

from ihome.libs.yuntongxun.CCPRestSDK import REST

# 主帐号
accountSid= '8a216da86b2bc78f016b32273331016c'

# 主帐号Token
accountToken= 'e335f8ce1370432381c013cc91378276'

# 应用Id
appId= '8a216da86b2bc78f016b322733980173'

# 请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com'

# 请求端口
serverPort='8883'

# REST版本号
softVersion='2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的类，如果没有，创建一个并保存
        # 如果有， 则将保存对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)
            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls.instance = obj
        return cls.instance

    def send_template_sms(self, to, datas, tempId):
        result = self.rest.sendTemplateSMS(to, datas, tempId)
        # for k, v in result.items():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.items():
        #             print('%s:%s' % (k, s))
        #     else:
        #         print('%s:%s' % (k, v))
        # statusCode: 000000
        # smsMessageSid: e0237073731149dca39dff21c50ac27e
        # dateCreated: 20190608102735
        statusCode = result.get("statusCode")
        if statusCode == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1


if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms('18729555808', ['6666', '5'], 1)
    print(ret)