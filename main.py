"""
api : https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json
dataset : https://data.gov.tw/dataset/128435

1. 列出 car 和 motor 小於 5 的停車格數 | List out the car and motor parking quantities less than 5
2. 列出 area 的 car 和 motor 總停車格數 | List out the area's car and motor total parking quantities
3. 列出 car 和 motor 相加總數，列出最高 5 名 | Add-up car and motor parking quantities total, and list out the highest parking quantities top 5
"""

import requests
import json
import textwrap


class Solution:
    url = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"
    resp = requests.get(url=url)
    respLoads = json.loads(resp.text)
    """
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    print(textwrap.dedent('''
    ---------------- request ----------------
    {req.method} {req.url}
    {reqHeader}

    Request Body :
    {req.body}
    ---------------- response ----------------
    {resp.status_code} {resp.reason} {resp.url}
    {respHeader}
    Duration : {respDuration}

    Response Context :
    {resp.text}
    ''').format(
        req=resp.request,
        resp=resp,
        respDuration=resp.elapsed.total_seconds(),
        reqHeader=format_headers(resp.request.headers),
        respHeader=format_headers(resp.headers),
    ))
    """

    def Questions1(self, carParkingQuantities: int, motorParkingQuantities: int):

        for result in self.respLoads['data']['park']:
            car = int(result['totalcar'])
            motor = int(result['totalmotor'])
            name = str(result['name'])
            if car <= carParkingQuantities and motor <= motorParkingQuantities:
                print(textwrap.dedent('''\
                    Total Car   : {car}     |   Total Motor : {motor}   | Parking Name    : {name}\
                ''').format(
                    name=name,
                    car=car,
                    motor=motor, end=''
                ))
                # print(json.dumps(result, indent=2, ensure_ascii=False))

    def Questions2(self, areaParking: str):

        carSum = 0
        motorSum = 0

        for result in self.respLoads['data']['park']:
            area = str(result['area'])
            car = int(result['totalcar'])
            motor = int(result['totalmotor'])
            if area == areaParking:
                carSum += car
            if area == areaParking:
                motorSum += motor
        finalSum = carSum + motorSum

        print(textwrap.dedent('''
                Area                                        : {areaParking}
                Total Parking Quantities of Car             : {carSum}
                Total Parking Quantities of Motor           : {motorSum}
                Total Parking Quantities of Car AND Motor   : {finalSum}

            ''').format(
            areaParking=areaParking,
            carSum=carSum,
            motorSum=motorSum,
            finalSum=finalSum
        ))

    def Questions3(self, topNo: int):

        carMotorList = []
        N = topNo

        for result in self.respLoads["data"]["park"]:
            id = str(result["id"])
            area = str(result['area'])
            name = str(result["name"])
            car = int(result["totalcar"])
            motor = int(result["totalmotor"])
            carMotorTotalSum = car + motor
            carMotorList += [[id, name, area, car, motor, carMotorTotalSum]]

        # List out the top, which in list no. 5 | N means the top
        finalTotalSort = sorted(carMotorList, key=lambda x: x[5], reverse=True)[:N]

        # print(finalTotalSort)

        # Pretty print method 1
        for finalPrint in finalTotalSort:
            information = {
                'Total Parking Quantity ': f"{finalPrint[5]}",
                'Id                     ': f"{finalPrint[0]}",
                'Name                   ': f"{finalPrint[1]}",
                'Area                   ': f"{finalPrint[2]}",
                'Car Parking Quantity   ': f"{finalPrint[3]}",
                'Motor Parking Quantity ': f"{finalPrint[4]}"
            }
            print(textwrap.dedent('''\
                {content}
                ''').format(
                content=''.join([f"\n {key}: {val}" for key, val in information.items()]))
            )

        """
        # Pretty print method 2
        for finalPrint in carTotalSort:
            print("Id : ", finalPrint[0], end="")
            print(" | Name : ", finalPrint[1], end="")
            print(" | Total Parking Quantity  : ", finalPrint[5])
        """


if __name__ == "__main__":
    solution = Solution()
    print("----- ----- Q1 列出 car 和 motor 小於 5 的停車格數 ----- -----\n")
    solution.Questions1(carParkingQuantities=5, motorParkingQuantities=5)
    print("\n----- ----- Q2 列出 area 的 car 和 motor 總停車格數 ----- -----")
    solution.Questions2(areaParking='南港區')
    print("----- ----- Q3 列出 car 和 motor 相加總數，列出最高 5 名 ----- -----")
    solution.Questions3(topNo=5)
