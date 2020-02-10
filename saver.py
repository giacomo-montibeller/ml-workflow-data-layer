import datetime as dt

class Saver:
    def __init__(self, file_path):
        self.csv_file = open(file_path, "w")
        self.csv_file.write("time,value\n")

    def add(self, records):
        for record in records:
            self.csv_file.write("%s,%s\n" % (hour_from_timestamp(record["timestamp"]), record["value"]))

    def save(self):
        self.csv_file.close()

def hour_from_timestamp(timestamp):
    return dt.datetime.fromtimestamp(timestamp / 1000).hour
