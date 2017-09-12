from flask import Flask, request, render_template
import requests
app = Flask(__name__)
pre_history = []

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

    p_city = data["results"][0]["location"]['name']
    now_weather = data["results"][0]["now"]["text"]
    now_tmp = data["results"][0]['now']['temperature']
    time = data['results'][0]['last_update']
    p_weather = p_city + "天气" + now_weather + "，气温为" + now_tmp + "，更新时间" + time + "。"
    pre_history.append(p_weather)
    return p_weather

@app.route('/', methods=['GET','POST'])
def index_page():
    return render_template('layout.html')

@app.route('/search', methods=['GET','POST'])
def search_weather():
    while True:
        if request.args.get('help') == "帮助":
            return render_template('program_help.html')
        elif request.args.get('history') == "历史":
            return render_template('history.html',history=pre_history)
        elif request.args.get('search') == "查询":
            city = request.args.get('instruct')
            try:
                weather_result = fetchWeather(city)
                return render_template('search.html', weather_result=weather_result)
            except:
                return render_template("404.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
