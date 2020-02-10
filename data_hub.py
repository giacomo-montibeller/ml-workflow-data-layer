import asyncio
import requests
from urllib.parse import urlencode

class DataHub:
    async def stations_for(self, category):
        return await asyncio.create_task(async_stations_for(category))

    async def records_for(self, category, station, data_type, start_time, end_time):
        return await asyncio.create_task(async_records_for(category, station, data_type, start_time, end_time))

async def async_stations_for(category):
    url = url_for(category, "get-station-details")
    stations = get(url)
    return list(filter(lambda it: valid_location(it), stations))

async def async_records_for(category, station, data_type_id, start, end):
    query_string = urlencode({
        "station": station["id"],
        "name": data_type_id, "from": int(start.timestamp()) * 1000,
        "to": int(end.timestamp()) * 1000
    })
    url = url_for(category, "get-records-in-timeframe", query_string)
    return get(url)

def url_for(category, operation, query_string=None):
    if query_string is None:
        query_string = ""
    else:
        query_string = "?%s" % query_string
    return "http://ipchannels.integreen-life.bz.it/" + category + "/rest/" + operation + query_string

def get(url):
    try:
        resp = requests.get(url=url)
        data = resp.json()
    except:
        print("An exception occurred")
        data = []
    return data

def valid_location(station: dict):
    if "latitude" not in station.keys():
        return False

    return (46.45629 <= station["latitude"] <= 46.51586 and
            11.29115 <= station["longitude"] <= 11.37938)
