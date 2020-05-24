from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.motortrend.com/news/ultimate-22-car-supercar-roundup-hot-hypercars-2019-geneva-motor-show/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

hyperCarArr = []
for motortrend in content.findAll('div', attrs={"class": "_3oV0c"}):
    motortrendObject = {
        "image": motortrend.find('figure', attrs={"class": "z1F90"}),
        "what": motortrend.find('strong', attrs={"class": "what"}).text.encode('utf-8'),
        "powertrain": motortrend.find('strong', attrs={"class": "powertrain"}).text.encode('utf-8'),
        "power": motortrend.find('strong', attrs={"class": "power"}).text.encode('utf-8'),
        "torque": motortrend.find('strong', attrs={"class": "torque"}).text.encode('utf-8'),
        "0-60": motortrend.find('strong', attrs={"class": "0-60"}).text.encode('utf-8'),
        "top speed": motortrend.find('strong', attrs={"class": "top speed"}).text.encode('utf-8'),
        "price": motortrend.find('strong', attrs={"class": "price"}).text.encode('utf-8'),
        "sum-up": motortrend.find('strong', attrs={"class": "sum-up"}).text.encode('utf-8')

    }

    hyperCarArr.append(motortrendObject)
    with open('motortrendData.json', 'w') as outfile:
        json.dump(hyperCarArr, outfile)