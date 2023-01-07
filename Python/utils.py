import math
#Globals
CENTER_POINT = 250000 # In mm, both X_0 and Y_0 being the same
ZONE_RANGE = 100000 # In mm

def is_in_bad_zone(x,y):
    return math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 ) < ZONE_RANGE

def get_distance_in_meters(x,y):
    return int(math.sqrt((x - CENTER_POINT)**2+(y - CENTER_POINT)**2 )/1000)
