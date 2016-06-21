
import json
import urllib2

response =  urllib2.urlopen("http://dataservice.accuweather.com/forecasts/v1/daily/1day/33028?apikey=G21JDHkpPG1QkGZJAnkusYI6YUEWTddH").read()
json = json.loads(response)

temperature_min = json['DailyForecasts'][0]['Temperature']['Minimum']['Value']
temperature_max = json['DailyForecasts'][0]['Temperature']['Maximum']['Value']
day_forcast = json['DailyForecasts'][0]['Day']['IconPhrase']
keywords_for_rain = ['storms', 'rain']

print 'minimum temperature', temperature_min, 'and maximum', temperature_max

if any(True if item in day_forcast else False for item in keywords_for_rain):
    print 'Possible rain tomorrow, dont ride to work'
else:
    print 'No rain tomorrow, ride to work!'
