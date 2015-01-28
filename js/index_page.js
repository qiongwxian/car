/**********************************
**********************************/

var headerFontSize = 16;
var merchantArr;
var curAddress;

window.onload = function()
{
	merchantArr = [];
	merchantArr.push(new merchant("新干线洗车店","www","最近可预约时段14:00-14:30",6,6));
	merchantArr.push(new merchant("新干线洗车洗车店洗车店洗车店","www","最近可预约时段14:00-14:30",6,6));
	//getLocation();
	showPosition();
	//while(!curAddress){};
}

window.onresize = function()
{
	var s = curAddress;
	var maxLen = (parseInt(document.getElementById("header").offsetWidth) - 75) / headerFontSize;
	var width = parseInt(document.getElementById("header").offsetWidth);
	maxLen = parseInt(maxLen) - 1;
	ss = s;
	if(s.length >= maxLen){
		var ss = s.substr(0,maxLen) + "...";
	}
	document.getElementById("location").innerHTML = ss;
	$(".merchant_detail").css("width",(width - 175) + "px");
	//alert((width - 165) + "px");
	s = document.getElementsByClassName("merchant_name");
	ss = document.getElementsByClassName("free_time");
	maxLen = parseInt((width - 175) / headerFontSize);
	for(var i = 0;i < merchantArr.length;i++){
		if(merchantArr[i].name.length >= maxLen){
			s[i].innerHTML = merchantArr[i].name.substr(0,maxLen-2) + "...";
		}
		else{
			s[i].innerHTML = merchantArr[i].name;
		}
		if(parseInt(width - 175) < 170){
			ss[i].innerHTML = merchantArr[i].freeTime.substr(0,parseInt(parseInt(width - 175) / 13)-1) + "...";
		}
		else{
			ss[i].innerHTML = merchantArr[i].freeTime;
		}
		//alert(merchantArr[i].freeTime)
		document.body.style.opacity = "1";
	}
	
	/*s = document.getElementsByClassName("free_time");
	maxLen = parseInt(width - 165);
	for(var i = 0;i < s.length;i++){
		if(maxLen < 170){
			s[i].innerHTML = s[i].innerHTML.substr(0,parseInt(maxLen / 13)-1) + "...";
		}
	}*/
}

function getLocation()
{
  if (navigator.geolocation)
  {
	navigator.geolocation.getCurrentPosition(showPosition,handleError);
  }
  else{curAddress = "定位失败";window.onresize();}
}
function showPosition(position)
{
	//var point = new BMap.Point(position.coords.longitude,position.coords.latitude);
	var point = new BMap.Point(113.384129,22.937244);
	var gc = new BMap.Geocoder();
	gc.getLocation(point, function(rs){
		//var addComp = rs.addressComponents;
		//alert(rs.address);
		curAddress = rs.address;
		window.onresize();
	});  
}
function handleError(error)
{
	curAddress = "定位失败";
	window.onresize();
}



var merchant = function(name,address,freeTime,freeCars,processing)
{
	this.name = name;
	this.address = address;
	this.freeTime = freeTime;
	this.freeCars = freeCars;
	this.processing = processing;
}