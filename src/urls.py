#coding:utf-8

from handlers.index import MainHandler
from handlers.BaseHandler import BaseHandler
from handlers.SendVerifyCodeHandler import SendVerifyCodeHandler
from handlers.VerifyPhoneHandler import VerifyPhoneHandler
from handlers.UserChangeUsernameHandler import UserChangeUsernameHandler
from handlers.GetStationForLocationHandler import GetStationForLocationHandler
from handlers.GetServiceInStationHandler import GetServiceInStationHandler
from handlers.GetStationFromIdHandler import GetStationFromIdHandler
from handlers.GetProductFromIdHandler import GetProductFromIdHandler
from handlers.UserCreateOrderHandler import UserCreateOrderHandler
from handlers.UserQueryOrderHandler import UserQueryOrderHandler
from handlers.UserApplyCancelOrderHandler import UserApplyCancelOrderHandler
from handlers.GetOrderFromIdHandler import GetOrderFromIdHandler
from handlers.CheckFreeStateForStationHandler import CheckFreeStateForStationHandler
from handlers.UserEvaluateOrderHandler import UserEvaluateOrderHandler
from handlers.GetStationDetailHandler import GetStationDetailHandler
from handlers.UserRegisterPushTokenHandler import UserRegisterPushTokenHandler
from handlers.UserGetCouponHandler import UserGetCouponHandler
from handlers.UploadViolationQueryCarInfoHandler import UploadViolationQueryCarInfoHandler
from handlers.GetUserViolationQueryCarInfoHandler import GetUserViolationQueryCarInfoHandler
from handlers.GetViolationQueryResultHandler import GetViolationQueryResultHandler
from handlers.CusRongCloudTokenIncorrectHandler import CusRongCloudTokenIncorrectHandler
from handlers.UserAddCarInfoHandler import UserAddCarInfoHandler
from handlers.UserModifyCarInfoHandler import UserModifyCarInfoHandler
from handlers.UserDeleteCarInfoHandler import UserDeleteCarInfoHandler
from handlers.UserAddStationCollectionHandler import UserAddStationCollectionHandler
from handlers.UserCancelStationCollectionHandler import UserCancelStationCollectionHandler
from handlers.UserGetStationCollectionHandler import UserGetStationCollectionHandler

urls = [
	(r'/',MainHandler),
	(r'/Base', BaseHandler),
	(r'/SendVerifyCode', SendVerifyCodeHandler),
	(r'/VerifyPhone', VerifyPhoneHandler),
	(r'/UserChangeUsername', UserChangeUsernameHandler),
	(r'/GetStationForLocation', GetStationForLocationHandler),
	(r'/GetServiceInStation', GetServiceInStationHandler),
	(r'/GetStationFromId', GetStationFromIdHandler),
	(r'/GetProductFromId', GetProductFromIdHandler),
	(r'/UserCreateOrder', UserCreateOrderHandler),
	(r'/UserQueryOrder', UserQueryOrderHandler),
	(r'/UserApplyCancelOrder', UserApplyCancelOrderHandler),
	(r'/GetOrderFromId', GetOrderFromIdHandler),
	(r'/CheckFreeStateForStation', CheckFreeStateForStationHandler),
	(r'/UserEvaluateOrder', UserEvaluateOrderHandler),
	(r'/GetStationDetail', GetStationDetailHandler),
	(r'/UserRegisterPushToken', UserRegisterPushTokenHandler),
	(r'/UserGetCoupon', UserGetCouponHandler),
	(r'/UploadViolationQueryCarInfo', UploadViolationQueryCarInfoHandler),
	(r'/GetUserViolationQueryCarInfo', GetUserViolationQueryCarInfoHandler),
	(r'/GetViolationQueryResult', GetViolationQueryResultHandler),
	(r'/CusRongCloudTokenIncorrect', CusRongCloudTokenIncorrectHandler),
	(r'/UserAddCarInfo', UserAddCarInfoHandler),
	(r'/UserModifyCarInfo', UserModifyCarInfoHandler),
	(r'/UserDeleteCarInfo', UserDeleteCarInfoHandler),
	(r'/UserAddStationCollection', UserAddStationCollectionHandler),
	(r'/UserCancelStationCollection', UserCancelStationCollectionHandler),
	(r'/UserGetStationCollection', UserGetStationCollectionHandler),
]
