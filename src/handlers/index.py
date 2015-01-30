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

        # 判断经纬度
        self.la = self.get_argument('la',0)
        self.lo = self.get_argument('lo',0)
        print 'la:' + str(la)
        print 'lo:' + str(lo)

        # 城市 id
        request.locate_id = 1;
        # 排序方式
        request.sort = 1;
        # 刷新方式
        request.refresh_direct = 1;
        # 加载的 station_id 偏移量
        request.station_id = 1;

        if la != 0:
            request.latitude = la
        if lo != 0:
            request.longitude = lo

        # 通信
        model = Model('GetStationForLocation')
        response = model.communication(request)

        # 判断状态
        if response.baseResponse.status != 0:
            if hasattr(response.baseResponse,'info'):
                self.render('index.html',author = response.baseResponse.info)
            else:
                self.render('index.html',author = 'Zeta - Error')

        # 解析 station 对象
        station = self.parsingStation(response.stations)

        print station

        self.render('index.html', author = 'Zeta - Success')

    def post(self):
        self.render('index.html', author = 'Zeta - JCheng')

    def parsingStation(self,stations):
        station_list = []
        for item in stations:
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

            station_list.append(tmp)

        return station_list


