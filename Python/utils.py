import math
import config
from datetime import datetime, timedelta
#Globals
CENTER_POINT = config.CENTER_POINT #in mm
ZONE_RANGE = config.ZONE_RANGE #in mm

def is_in_bad_zone(x,y):
    return math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 ) < ZONE_RANGE

def get_distance_in_meters(x,y):
    return int(math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 )/1000)

def remove_old_objects(objects: list) -> list:
    current_time = datetime.utcnow()
    updated_objects = []
    for obj in objects:
        print("obj: ", obj)
        time_difference = current_time - obj["timestamp"]
        print("TIMEDIFF IS:", time_difference)
        if time_difference < timedelta(minutes=config.ERASE_TIME):
            print("HIT ", time_difference, " ", timedelta(minutes=config.ERASE_TIME))
            updated_objects.append(obj)

        else:
            print("SERIOUSHIT")
    return updated_objects
