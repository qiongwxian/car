#coding:utf-8
import tornado.web
import tornado.httpclient as httpclient

from model.model import Model
import pb.CarCusApi_pb2 as ProtobufAPI

class UserGetCouponHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html',author = 'Zeta -JCheng')

    def post(self):
        # 接收 POST 过来的数据
        rawData = self.request.body

        # 创建 request 对象
        request = ProtobufAPI.UserGetCouponRequest()

        #
        # 此处一定要对 request 对象进行赋值
        # 例如: request.baserequest.sdk_version = 1
        #

        model = Model('UserGetCoupon')
        response = model.communication(request)

        self.render('index.html',author = 'Zeta - JCheng')
