import requests
import json
# URL='http://127.0.0.1:8000/api/stu/'
# a=input('inter the name:-')
# b=int(input('inter the roll:-'))
# c=input('inter the city:-')
# data={'name':a,
# 		'roll':b,
# 		'city':c,
# 	}
# json_data=json.dumps(data)
# r=requests.post(url=URL,data=json_data)
# print(data)


URLs = "http://127.0.0.1:8000/api/"

def get_data(id=None):
	data={}
	if id is not None:
		data={'id':id }
	json_data=json.dumps(data)
	rs=requests.get(url=URLs,data=json_data)
	data = rs.json()
	print("get data in to table:-",data)
get_data()