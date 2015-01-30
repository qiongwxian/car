#coding:utf-8
import tornado.web

from model.model import Model
from components.helper import Helper
import pb.CarCusApi_pb2 as ProtobufAPI

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 创建 request 对象
        request = ProtobufAPI.GetStationForLocationRequest()

        flag = Helper.fillBaseRequest(request.baseRequest)

        if not flag:
            self.render('index.html',author = 'Error')

        request.locate_id = 1;
        request.sort = 1;
        request.refresh_direct = 1;
        request.station_id = 0;

        model = Model('GetStationForLocation')
        response = model.communication(request)

        if response.baseResponse.status != 0:
            if hasattr(response.baseResponse,'info'):
                self.render('index.html',author = response.baseResponse.info)
            else:
                self.render('index.html',author = 'Zeta - Error')

        self.render('index.html', author = 'Zeta - Success')

    def post(self):
        self.render('index.html', author = 'Zeta - JCheng')


