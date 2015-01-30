#coding:utf-8
import tornado.web
import tornado.httpclient as httpclient

from model.model import Model
from components.helper import Helper
import pb.CarCusApi_pb2 as ProtobufAPI

class GetStationFromIdHandler(tornado.web.RequestHandler):

    def get(self,station_id):
        request = ProtobufAPI.GetStationFromIdRequest()

        flag = Helper.fillBaseRequest(request.baseRequest)

        if not flag:
            self.render('index.html',author = 'Error')

        request.station_id = station_id

        model = Model('GetStationFromId')
        response = model.communication(request)

        # 判断状态
        if response.baseResponse.status != 0:
            if hasattr(response.baseResponse,'info'):
                self.render('index.html',author = response.baseResponse.info)
            else:
                self.render('index.html',author = 'Zeta - Error')

        # 解析 station 对象
        station = self.parsingStation(response.stations)

        # 创建 request 对象
        request = ProtobufAPI.GetServiceInStationRequest()

        flag = Helper.fillBaseRequest(request.baseRequest)

        if not flag:
            self.render('index.html',author = 'Error')

        model = Model('GetServiceInStation')
        response = model.communication(request)

        # 判断状态
        if response.baseResponse.status != 0:
            if hasattr(response.baseResponse,'info'):
                self.render('index.html',author = response.baseResponse.info)
            else:
                self.render('index.html',author = 'Zeta - Error')

        services = self.parsingProduct(response.services)

        self.render('index.html',author = 'Zeta -JCheng')

    def post(self):
        # 接收 POST 过来的数据
        rawData = self.request.body

        # 创建 request 对象
        request = ProtobufAPI.GetStationFromIdRequest()

        #
        # 此处一定要对 request 对象进行赋值
        # 例如: request.baserequest.sdk_version = 1
        #

        model = Model('GetStationFromId')
        response = model.communication(request)

        self.render('index.html',author = 'Zeta - JCheng')

    def parsingStation(self,item):
        station = dict([])

        station['station_id'] = item.station_id
        station['manage_id'] = item.manage_id
        station['name'] = item.name

        # 得到空位数
        if hasattr(item,'car_space_num'):
            station['car_space_num'] = item.car_space_num
        else:
            station['car_space_num'] = 0

        # 得到服务中数量
        if hasattr(item,'serving_num'):
            station['serving_num'] = item.serving_num
        else:
            station['serving_num'] = 0

        # 空闲时间端
        if hasattr(item,'next_free_time'):
            station['next_free_time'] = item.next_free_time
        else:
            station['next_free_time'] = ''

        # 经纬度
        if hasattr(item,'latitude'):
            station['latitude'] = item.latitude
        else:
            station['latitude'] = 0
        if hasattr(item,'longitude'):
            station['longitude'] = item.longitude
        else:
            station['longitude'] = 0

        if station['latitude'] == 0 or tmp['longitude'] == 0 or self.la == 0 or self.lo == 0:
            station['distance'] = Helper.distance(tmp['latitude'],tmp['longitude'],self.la,self.lo)
        else:
            station['distance'] = -1

        return station

    def parsingProduct(self,services):
        service_list = []

        for item in services:
            tmp = dict([])
            tmp['station_id'] = item.station_id
            tmp['manage_id'] = item.manage_id
            tmp['name'] = item.name

            # 得到空位数
            if hasattr(item,'car_space_num'):
                tmp['car_space_num'] = item.car_space_num
            else:
                tmp['car_space_num'] = 0

            # 得到服务中数量
            if hasattr(item,'serving_num'):
                tmp['serving_num'] = item.serving_num
            else:
                tmp['serving_num'] = 0

            # 空闲时间端
            if hasattr(item,'next_free_time'):
                tmp['next_free_time'] = item.next_free_time
            else:
                tmp['next_free_time'] = ''

            # 经纬度
            if hasattr(item,'latitude'):
                tmp['latitude'] = item.latitude
            else:
                tmp['latitude'] = 0
            if hasattr(item,'longitude'):
                tmp['longitude'] = item.longitude
            else:
                tmp['longitude'] = 0

            if tmp['latitude'] == 0 or tmp['longitude'] == 0 or self.la == 0 or self.lo == 0:
                tmp['distance'] = Helper.distance(tmp['latitude'],tmp['longitude'],self.la,self.lo)
            else:
                tmp['distance'] = -1

            service_list.append(tmp)

        return service_list
