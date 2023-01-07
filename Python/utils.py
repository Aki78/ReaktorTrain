import math
import config
#Globals
CENTER_POINT = config.CENTER_POINT #in mm
ZONE_RANGE = config.ZONE_RANGE #in mm

def is_in_bad_zone(x,y):
    return math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 ) < ZONE_RANGE

def get_distance_in_meters(x,y):
    return int(math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 )/1000)
