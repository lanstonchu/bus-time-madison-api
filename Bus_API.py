
# json from https://www.cityofmadison.com/metro/business/information-for-developers
import urllib.request
import json
from urllib.request import urlopen
from datetime import datetime


buses_I_want = {"8381":"02","8382":"03","8461":"02","8462":"03"}
bus_stops_I_want = {"178":"Univ & N Orchard WB","581":"W Johnson & N Charter EB"}
API_address="http://transitdata.cityofmadison.com/TripUpdate/TripUpdates.json"

# get the json html content from Madison Bus Company
webRequest = urllib.request.Request(API_address)
html = urlopen(webRequest)

# convert json html content into jason object via a string
htmlStr=str(list(html))
htmlStrKey=htmlStr[3:-2]
jsonObj=json.loads(htmlStrKey)



# get current time
curr_timestamp = jsonObj.get("header").get("timestamp")
curr_time = datetime.fromtimestamp(curr_timestamp) # datetime already consider the timezone of my local system
print("################# Current time is #################")
print("############## ", curr_time, " ##############")
print("###################################################")

buses = jsonObj.get("entity")
num_bus = len(buses)

# create empty schedules-dictionary for storing values
schedules={}
for stop_id_i in bus_stops_I_want.keys():
    schedules[stop_id_i] = []

# update schedules-dictionary
for bus in buses:
    bus_id=bus.get("trip_update").get("trip").get("route_id")
    if bus_id in buses_I_want.keys():
        
        bus_stops = bus.get("trip_update").get("stop_time_update")
        # time should be equal to scheduled time + delay
        
        for bus_stop in bus_stops:
            delay_n_time = bus_stop.get("departure")
            stop_id = bus_stop.get("stop_id")
            
            if stop_id in bus_stops_I_want.keys() and delay_n_time!=None:
                bus_id_human=buses_I_want[bus_id]
                delay_in_minutes = delay_n_time.get("delay")/60
                timestamp = delay_n_time.get("time")
                if timestamp>=curr_timestamp:
                    time_depart = datetime.fromtimestamp(timestamp)
                    time_from_now = datetime.utcfromtimestamp(timestamp - curr_timestamp)
                    schedules[stop_id].append({ \
                             "bus_id_human":bus_id_human, \
                             "delay_in_minutes":delay_in_minutes, \
                             "time_depart":time_depart, \
                             "time_from_now":time_from_now})
                
# sort and print schedules-dictionary
for stop_id_i in schedules.keys():
    print("\n \nBus stop is: ",bus_stops_I_want[stop_id_i])
    
    # sort schedules according to time
    schedules[stop_id_i]=sorted(schedules[stop_id_i], key=lambda \
             stop: stop["time_depart"], reverse=True)

    for stop in reversed(schedules[stop_id_i]):  # reverse order so that from new to old
        bus_id_human = stop["bus_id_human"]
        delay_in_minutes = stop["delay_in_minutes"]
        time_depart = stop["time_depart"]
        time_from_now = stop["time_from_now"]
        print("    Route",bus_id_human,"|| Delay",int(delay_in_minutes+0.5), \
              "min || Time",time_depart.strftime("%a %H:%M:%S"), \
              "|| From now",time_from_now.strftime("%H:%M:%S"))