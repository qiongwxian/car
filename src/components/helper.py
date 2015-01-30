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

    @staticmethod
    def distance(lat1,lng1,lat2,lng2):
        radlat1 = rad(lat1)
        radlat2 = rad(lat2)
        a = radlat1 - radlat2
        b = rad(lng1) - rad(lng2)
        s = 2*math.asin(math.sqrt(math.pow(math.sin(a/2),2) + math.cos(radlat1)*math.cos(radlat2)*math.pow(math.sin(b/2),2)))
        earth_radius = 6378.137
        s = s*earth_radius
        if s < 0:
            return -s
        else:
            return s

