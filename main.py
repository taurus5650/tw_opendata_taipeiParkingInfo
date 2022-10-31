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

# print (json.dumps(respLoads, indent=2, ensure_ascii=False))

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

def everyAreaCarAndMotor () :
        print ("------  ------  ------  列出每個 area  的 car 和 motor 總停車格數  ------  ------  ------")
        print ("e.g. 松山區、內湖區、大同區 etc.")
        userInput = input(str("Input the area : "))

        carSum = 0
        motorSum = 0

        for result in respLoads["data"]["park"]:
            car = result["totalcar"]
            motor = result["totalmotor"]
            area = result["area"]
            if userInput in str(area) :
                carSum += int(car)
            if userInput in str(area) :
                motorSum += int(motor)
            ## print area details
            if userInput in str(area) :
                print (result)

        print (">>> TOTAL <<<")
        print (f"Area : {str(userInput)} | Total Parking of Car {carSum}")
        print (f"Area : {str(userInput)} | Total Parking of Motor {motorSum}")

def carMotorTop5 () :
    print ("------  ------  ------  列出 car 和 motor 相加總數，列出最高 5 名  ------  ------  ------")

    carMotorTotalSum = []
    N = 5

    for result in respLoads["data"]["park"] :
        id = result["id"]
        name = result["name"]
        car = result["totalcar"]
        motor = result["totalmotor"]
        carMotorTotalSum += [[str(id), str(name), int(car)+int(motor)]]

    carMotorTotalSort = sorted(carMotorTotalSum, key=lambda x:x[2], reverse=True)[:N]

    # print (carMotorTotalSum)
    print (carMotorTotalSort)

    ## pretty print
    for finalPrint in carMotorTotalSort:
        print ("id : ", finalPrint[0], end="")
        print (" | name : ", finalPrint[1], end="")
        print (" | total (car & motor) : ", finalPrint[2])


if __name__ == "__main__" :
    carMotorLessThan10()
    everyAreaCarAndMotor()
    carMotorTop5 ()
