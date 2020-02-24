#coding:utf-8
import requests
import json
import time

def one():
	fileone = open('edusrc.txt','r+')
	for i in fileone:
		urls=i.replace('\n','')
		url = "https://192.168.56.1:3443/api/v1/targets"
		headersjson = {
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
			"Content-Type": "application/json;charset=UTF-8",
			"X-Auth":"2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c",
			"Origin":"https://192.168.56.1:3443",
			"Referer":"https://192.168.56.1:3443/",
			"Sec-Fetch-Site":"same-origin",
			"Sec-Fetch-Mode":"cors",
			"Accept": "application/json, text/plain, */*",
			"Cookie": "ui_session=2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c"
		}
		datajson= {
			'address':urls,
			'description':'',
			'criticality':'10'
		}
		res = requests.post(url,headers=headersjson,verify=False,data=json.dumps(datajson))
		respa = res.headers
		try:
			respa = respa['Location']
		except:
			pass
		if "/api/v1/targets/" in respa:
			respa = respa.replace('/api/v1/targets/','')
			two(respa)
		else:
			pass

def two(Locationone):
	url = 'https://192.168.56.1:3443/api/v1/targets/'+Locationone+'/configuration'
	datajson={
		"enabled":"true",
		"address":"127.0.0.1",
		"protocol":"http",
		"port":"7777"
	}
	headersjson = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
		"Content-Type": "application/json;charset=UTF-8",
		"X-Auth":"2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c",
		"Origin":"https://192.168.56.1:3443",
		"Referer":"https://192.168.56.1:3443/",
		"Sec-Fetch-Site":"same-origin",
		"Sec-Fetch-Mode":"cors",
		"Accept": "application/json, text/plain, */*",
		"Cookie": "ui_session=2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c"
	}
	datajsontwo={
		"proxy":datajson
	}
	res = requests.patch(url,headers=headersjson,verify=False,data=json.dumps(datajsontwo))
	try:
		three(Locationone)
	except:
		pass
def three(Locationone):
	url = "https://192.168.56.1:3443/api/v1/scans"
	datajsona={
		"disable":"false",
		"start_date":None,
		"time_sensitive":"false"
	}
	headersjson = {
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
		"Content-Type": "application/json;charset=UTF-8",
		"X-Auth":"2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c",
		"Origin":"https://192.168.56.1:3443",
		"Referer":"https://192.168.56.1:3443/",
		"Sec-Fetch-Site":"same-origin",
		"Sec-Fetch-Mode":"cors",
		"Accept": "application/json, text/plain, */*",
		"Cookie": "ui_session=2986ad8c0a5b3df4d7028d5f3c06e936c5e3b1f14dd6ed95c627e48be9264ff63c8368f4ebd056c28cf9b4979a122d37a929f504f0b5bb9c7c83279a534e5eb9c"
	}
	datajson={
		"target_id":Locationone,
		"profile_id":"11111111-1111-1111-1111-111111111111",
		"schedule":datajsona,
		"ui_session_id":"8d06fc15a6502cfe52bbad480d2b7191"
	}
	res = requests.post(url,headers=headersjson,verify=False,data=json.dumps(datajson))
	respa = res.headers
	print(respa)
	respa = respa['Location']
	if "/api/v1/scans/" in respa:
		respa = respa.replace('/api/v1//scans/','')
		urls="https://192.168.56.1:3443/api/v1/scans/"+respa
		res = requests.get(urls,headers=headersjson,verify=False)
		
	else:
		pass	

if __name__ == '__main__':
	one()
	time.sleep(1)