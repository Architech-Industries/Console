from utils import var, auth
from influxdb_client import InfluxDBClient
#Point = str
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = ""
org = ""
bucket = ""


def authTestLoop():
    client = InfluxDBClient(url="http://192.168.21.71:8086", token=token)
    write_api = client.write_api()
    query_api = client.query_api()

    while True:
                write_api.write("test", var.auth.org, [{"measurement": "h2o_feet", "tags": {"location": "coyote_creek"}, "fields": {"water_level": 1}, "time": 1}])
                #write_api.write(bucket=auth.bucket,org=auth.org,record=p)
                query = 'from(bucket: "test")\
                |> range(start: -10m)\
                |> filter(fn: (r) => r._measurement == "h2o_level")\
                |> filter(fn: (r) => r._field == "water_level")\
                |> filter(fn: (r) => r.location == "coyote_creek")'
                #window['Order#'](value=var.commandvals.V0)
                result = client.query_api().query(org=var.auth.org, query=query)
                results = []
                for table in result:
                    for record in table.records:
                        results.append((record.get_value(), record.get_field()))
                print(results)
                break