#coding:utf-8

from handlers.index import MainHandler
from handlers.BaseHandler import BaseHandler
from handlers.SendVerifyCodeHandler import SendVerifyCodeHandler
from handlers.VerifyPhoneHandler import VerifyPhoneHandler
from handlers.UserLoginHandler import UserLoginHandler
from handlers.UserChangeUsernameHandler import UserChangeUsernameHandler
from handlers.GetStationForLocationHandler import GetStationForLocationHandler
from handlers.GetServiceInStationHandler import GetServiceInStationHandler
from handlers.GetStationFromIdHandler import GetStationFromIdHandler
from handlers.GetProductFromIdHandler import GetProductFromIdHandler
from handlers.UserCreateOrderHandler import UserCreateOrderHandler
from handlers.UserQueryOrderHandler import UserQueryOrderHandler
from handlers.UserConfirmFinishServiceHandler import UserConfirmFinishServiceHandler
from handlers.UserApplyCancelOrderHandler import UserApplyCancelOrderHandler
from handlers.GetOrderFromIdHandler import GetOrderFromIdHandler
from handlers.GetIndexStationHandler import GetIndexStationHandler
from handlers.CheckFreeStateForStationHandler import CheckFreeStateForStationHandler
from handlers.UserEvaluateOrderHandler import UserEvaluateOrderHandler
from handlers.GetStationDetailHandler import GetStationDetailHandler
from handlers.UserRegisterPushTokenHandler import UserRegisterPushTokenHandler
from handlers.UserGetCouponHandler import UserGetCouponHandler
from handlers.UserSearchStationHandler import UserSearchStationHandler
from handlers.UploadViolationQueryCarInfoHandler import UploadViolationQueryCarInfoHandler
from handlers.GetUserViolationQueryCarInfoHandler import GetUserViolationQueryCarInfoHandler
from handlers.GetViolationQueryResultHandler import GetViolationQueryResultHandler

urls = [
	(r'/',MainHandler),
	(r'/?r=Base', BaseHandler),
	(r'/?r=SendVerifyCode', SendVerifyCodeHandler),
	(r'/?r=VerifyPhone', VerifyPhoneHandler),
	(r'/?r=UserLogin', UserLoginHandler),
	(r'/?r=UserChangeUsername', UserChangeUsernameHandler),
	(r'/?r=GetStationForLocation', GetStationForLocationHandler),
	(r'/?r=GetServiceInStation', GetServiceInStationHandler),
	(r'/?r=GetStationFromId', GetStationFromIdHandler),
	(r'/?r=GetProductFromId', GetProductFromIdHandler),
	(r'/?r=UserCreateOrder', UserCreateOrderHandler),
	(r'/?r=UserQueryOrder', UserQueryOrderHandler),
	(r'/?r=UserConfirmFinishService', UserConfirmFinishServiceHandler),
	(r'/?r=UserApplyCancelOrder', UserApplyCancelOrderHandler),
	(r'/?r=GetOrderFromId', GetOrderFromIdHandler),
	(r'/?r=GetIndexStation', GetIndexStationHandler),
	(r'/?r=CheckFreeStateForStation', CheckFreeStateForStationHandler),
	(r'/?r=UserEvaluateOrder', UserEvaluateOrderHandler),
	(r'/?r=GetStationDetail', GetStationDetailHandler),
	(r'/?r=UserRegisterPushToken', UserRegisterPushTokenHandler),
	(r'/?r=UserGetCoupon', UserGetCouponHandler),
	(r'/?r=UserSearchStation', UserSearchStationHandler),
	(r'/?r=UploadViolationQueryCarInfo', UploadViolationQueryCarInfoHandler),
	(r'/?r=GetUserViolationQueryCarInfo', GetUserViolationQueryCarInfoHandler),
	(r'/?r=GetViolationQueryResult', GetViolationQueryResultHandler),
]
