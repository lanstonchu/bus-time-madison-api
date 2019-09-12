# bus-time-madison-api
 This is the Python code to get bus time for Madison, WI via an API

For Windows
 1. Include the bus ID and bus stop ID you want in Bus_API.py
 2. put the file "bus.bat" on the same folder as Bus_API.py, click and run it.
 3. it will call Python to run Bus_API.py automatically

For Linux
1. Include the bus ID and bus stop ID you want in Bus_API.py
2. use whatever method you want to run Bus_API.py

Result will look like this:
![Bus Schedule][1]

 -----------------------------------------------

 json structure:

 .
 ├──"entity" \n
 |    ├──"alert"
 |    ├──"id"
 |    └──"trip_update"
 |         ├──"stop_time_update"
 |         |    ├──"arrival"
 |         |    ├──"departure"
 |         |    |    ├──"delay"
 |         |    |    └──"time"
 |         |    ├──"schedule_relationship"
 |         |    ├──"stop_id"
 |         |    └──"stop_sequence"
 |         ├──"timestamp"
 |         ├──"trip"
 |         |    ├──"route_id"
 |         |    ├──"schedule_relationship"
 |         |    ├──"start_date"
 |         |    └──"trip_id"
 |         └──"vehicle"
 |              ├──"id"
 |              └──"label"
 └──"header"
      ├──"incrementality"
      └──"timestamp"

[1]: https://github.com/lanstonchu/bus-time-madison-api/blob/master/Bus%20Screen.png?raw=true
