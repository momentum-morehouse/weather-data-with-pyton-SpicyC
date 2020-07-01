import requests

city_list = [
(33.748997, -84.387985, "Atlanta"),
(-1.940278, 29.873888, "Rwanda"),
(37.871593, -122.272743, "Berkeley"),
(33.770050, -118.193741, "Long Beach"),
(15.185339, 145.744794, "Saipan"),
(38.9072, 77.0369, "DC"),
(38.9847, 77.0947, "Bethesda"),
(39.7589, 84.1916, "Dayton"),
(84.1916, 78.4595, "LuRay"),
(40.0293, 75.1746, "Germantown"),
(37.5594, 122.2869, "Mariners Island"),
(41.6020, 87.3372, "Gary")]


#print(response.text)
def climate(locations):
    climate_data_packet = {}
    for location in locations:
        url = "https://api.climacell.co/v3/weather/realtime"
        payload = {
        "apikey": "TKmzyG2VZUxoJTFVDGEmEhywZD6KB095",
        "lat":location[0],
        "lon":location[1],
        "fields": ["temp", "precipitation", "wind_gust"],
        "unit_system":"us",
        }

        response = requests.get(url, params=payload).json()

        climate_data_packet[location[2]] = response["temp"] ["value"]

    for city, temp in climate_data_packet.items():

        print(f"The temp is {temp} in {city}.")
    return climate_data_packet

climate_data = climate(city_list)

# get_weather_data[location[2]] = response["temp"] ["value"]

# #  print(response)
# #for location in locations:
# #    print(lat, lon)

# for location, temp in get_weather_data.items():

#     print(f"The temp is {temp} in {location })

# return get_data-packet

# #get_weather_data(33.748997, -84.387985)

# get_weather_data = weather(locations_list)

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