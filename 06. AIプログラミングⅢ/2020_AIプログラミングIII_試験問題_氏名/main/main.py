import requests
import json, pprint
import datetime as dt


api = "https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

cities = ['Sapporo', 'Tokyo']
apikey = '44a91992b7b41d804fdc35d624db9e18'

# kelvin to celsius
def k2c(temp):
    return temp-273.15

# unixtime to dt
def unix2jst(ut):
    return dt.datetime.fromtimestamp(ut).strftime('%Y-%m-%d %H:%M:%S')

for name in cities:
    url = api.format(city=name, key=apikey)
    r = requests.get(url)
    data = json.loads(r.text)

    print("+ 都市=", data['name'])
    print("| 天気=", data['weather'][0]['description'])
    print("| 天気=")
    print("| 気温=", k2c(data['main']['temp']))
    print("| 湿度=", data['main']['humidity'])
    print("| 風速=", data['wind']['speed'])
    print("| 雲量=")
    print("| データ時刻=", unix2jst(data['dt']))
    print("")