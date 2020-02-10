import asyncio
import json
import os
import datetime as dt
import data_hub
import saver

class App:
    def __init__(self, config_file, data_hub, saver):
        if not os.path.exists("data"):
            os.makedirs("data")

        configs = get_configs_from(config_file)
        self.data_hub = data_hub
        self.saver = saver
        self.time_frame_size = configs["time_frame_size"]
        self.time_from = date_from(configs["time_from"])
        self.time_to = date_from(configs["time_to"])
        self.data_type = configs["data_type"]
        self.category = configs["category"]

    async def execute(self):
        stations = await self.data_hub.stations_for(self.category)
        time_frames = time_frames_from(self.time_from, self.time_to, self.time_frame_size)

        for station in stations:
            for frame_index in range(len(time_frames) - 1):
                start_time = time_frames[frame_index]
                end_time = time_frames[frame_index + 1]
                records = await self.data_hub.records_for(self.category, station, self.data_type, start_time, end_time)
                self.saver.add(records)
                print_record(self.category, station, self.data_type, records, start_time, end_time)

        self.saver.save()

def get_configs_from(configs_file):
    with open(configs_file) as configfile:
        return json.loads("".join(configfile.readlines()))

def time_frames_from(start, end, time_frame_size):
    actual = end
    while True:
        if actual <= start:
            start = actual
            break
        actual -= dt.timedelta(days=1)

    date_range = range(0, (end - start).days + 1, time_frame_size)
    return reverse([end - dt.timedelta(days=x) for x in date_range])

def reverse(elements):
    return elements[::-1]

def date_from(date_as_string):
    return dt.datetime.strptime(date_as_string, '%Y-%m-%d')

def print_record(category, station, data_type, records, start_time, end_time):
    print("obtained %i records for %s %s %s (%s -> %s)" % (
        len(records),
        category,
        station["id"],
        data_type,
        start_time.strftime('%Y-%m-%d'),
        end_time.strftime('%Y-%m-%d')))

if __name__ == "__main__":
    data_hub = data_hub.DataHub()
    saver = saver.Saver('data/dataset.csv')

    app = App("config.json", data_hub, saver)
    asyncio.run(app.execute())
