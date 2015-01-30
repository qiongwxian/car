#coding:utf-8

class Helper:

    def __init__(self):
        pass

    # 填充 baseRequest
    @staticmethod
    def fillBaseRequest(baseRequest,user = []):
        baseRequest.sdk_version = 23333
        baseRequest.device_type = 2
        baseRequest.device_id = '233333'

        if len(user) == 2:
            baseRequest.userIdentity.user_id = user[0]
            baseRequest.userIdentity.token = user[1]
            return True
        elif len(user) == 0:
            return True

        return False

