import requests

locations = (33.748997, -84.387985, 'Atlanta, Georgia', -1.940278, 29.873888,
             'Rwanda, Africa', 37.871593, -122.272743, 'Berkeley, California',
             33.770050, -118.193741, 'Long Beach, California', 15.185339,
             145.744794, 'Saipan, CNMI', 38.9072, 77.0369, 'Washington, D.C.',
             38.9847, 77.0947, 'Bethesda, Maryland', 39.7589, 84.1916,
             'Dayton, Ohio', 84.1916, 78.4595, 'LuRay, Virginia', 40.0293,
             75.1746, 'Germantown, Pennsylvania', 37.5594, 122.2869,
             'Mariners Island, California', 41.6020, 87.3372, 'Gary, Indiana')


#print(response.text)
def get_weather_data(lat, lon):

  url = "https://api.climacell.co/v3/weather/realtime"


  payload = {
    "apikey": "TKmzyG2VZUxoJTFVDGEmEhywZD6KB095",
    "lat": lat,
    "lon": lon,
    "fields": ["feels_like", "temp", "precipitation", "wind_gust"],
    "unit_system": "us",
}

  response = requests.get(url, params=payload).json()

  print(response)
#for location in locations:
#    print()


get_weather_data(33.748997, -84.387985)

#from climacell_api import ClimacellApiClient
#client = ClimacellApiClient(TKmzyG2VZUxoJTFVDGEmEhywZD6KB095)
#r = client.nowcast(lat=40, lon=50, timestep=30, start_time='now', end_time='', fields=['temp', 'wind_gust'])
#r.status_code
#200
#r.json() # for raw json
#[{ 'lat':, 'lon':,}, { 'lat':, 'lon':,},]
# data = ()
# data[0].lat
# 40
# data[0].lon
# 50
# data[0].observation_time
# #datetime.datetime(2020, 6, 26, 13, 45, 26, tzinfo=tzutc())
# measurements = data[0].measurements
# measurements['temp'].value
# 43
# measurements['temp'].units
# 'C'
# measurements['wind_gust'].value
# 7.5
# measurements['wind_gust'].units
# 'm/s'

#get_weather_data(lat, lon)
