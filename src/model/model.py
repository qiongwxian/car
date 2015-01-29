#coding:utf-8
import tornado.httpclient as httpclient
import pb.CarCusApi_pb2 as ProtobufAPI

class Model:
    def __init__(self,handlerName):
        self.handlerName = handlerName
        self.baseUrl = 'http://42.121.129.102:10000/?r='

    def communication(self,request):
        data = request.SerializeToString()

        http_client = httpclient.HTTPClient()
        url = self.baseUrl + self.handlerName
        req = httpclient.HTTPRequest(url,method = 'POST',body = data)
        ret = http_client.fetch(req)

        response = eval('ProtobufAPI.' + self.handlerName + 'Response()')
        response.ParseFromString(ret.body)
        return response
