import requests

pre_history = []
program_help = '''
            输入城市名，查询该城市天气情况。
            输入‘h’或‘help’，获取帮助文档。
            输入history，获取历史查询记录。
            输入‘quit’或‘exit’，退出查询系统。
            '''
print(program_help)
print("            本页面数据来源为心知天气。\n")

def fetchWeather(city):
    r = requests.get(
        "https://api.seniverse.com/v3/weather/now.json",
        params={
            'key': 'p3yhkjqouvndzw7k',
            'location': city,
            'language': 'zh-Hans',
            'unit': 'c'
        },
        timeout=1)
    data = r.json()
    return data

def weather_data():
    result = fetchWeather(city)
    p_city = result["results"][0]["location"]['name']
    now_weather = result["results"][0]["now"]["text"]
    now_tmp = result["results"][0]['now']['temperature']
    time = result['results'][0]['last_update']
    p_weather = p_city + "天气" + now_weather + "，气温为" + now_tmp + "，更新时间" + time + "。"
    print(p_weather)
    print()
    pre_history.append(p_weather)

def history():
    if len(pre_history) == 0:
        print("您还没有任何查询，请输入指令或城市名，如需帮助请输入'h'。\n")
    else:
        for i in range(len(pre_history)):
            print(pre_history[i - 1])
        print()

while True:
    city = input("请输入指令或城市名：")

    if city in ("h", "help"):
        print(program_help)

    elif city == "history":
        history()

    elif city in ('quit', 'exit'):
        history()
        print("感谢您的查询，希望你查询的城市天气如您所愿。")
        break

    else:
        try:
            weather_data()
        except:
            print("你所查询的城市或指令不在服务区，请输入“h”或“help”获取帮助。\n")
