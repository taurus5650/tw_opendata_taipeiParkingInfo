"""
api : https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json
dataset : https://data.gov.tw/dataset/128435

1. 列出 car 和 motor 小於 5 的停車格數
2. 列出每個 area  的 car 和 motor 總停車格數
3. 列出 car 和 motor 相加總數，列出最高 5 名

"""


import requests
import json

url = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"

resp = requests.get(url = url)
respLoads = json.loads(resp.text)

#print (json.dumps(respLoads, indent=2, ensure_ascii=False))

def carMotorLessThan10 ():
    print ("------  ------  ------  列出 car 和 motor 小於 5 的停車格數  ------  ------  ------")

    # for result in respLoads :
    #     carResult = respLoads["data"]["park"]
    #     for result2 in carResult :
    #         carFinal = result2["totalcar"]
    #         if int(carFinal) <= 5 :
    #             print (result2)

    for result in respLoads["data"]["park"] :
        car = result["totalcar"]
        motor = result["totalmotor"]
        if int(car) <= 5 and int(motor) <= 5 :
            #print (result)
            print (json.dumps(result, indent=2, ensure_ascii=False))












if __name__ == "__main__" :
    carMotorLessThan10()

