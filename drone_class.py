import math

#Globals
center_point = 250000 # In mm, both X_0 and Y_0 being the same
zone_range = 100000 # In mm

def is_in_bad_zone(x,y):
    return math.sqrt((x - center_point)**2+(y - center_point)**2 ) < zone_range

def get_distance_in_meters(x,y):
    return int(math.sqrt((x - center_point)**2+(y - center_point)**2 )/1000)

class Drone():
    def __init__(self,drone_data):
        self.serialNumber = drone_data["serialNumber"]
        self.model = drone_data["model"]
        self.manufacturer = drone_data["manufacturer"]
        self.mac = drone_data["mac"]
        self.ipv4 = drone_data["ipv4"]
        self.ipv6 = drone_data["ipv6"]
        self.firmware = drone_data["firmware"]
        self.x = int(float(drone_data["positionX"]))
        self.y = int(float(drone_data["positionY"]))
        self.altitude = drone_data["altitude"]
        self.is_naughty = is_in_bad_zone(self.x,self.y)
        self.distance =  get_distance_in_meters(x,y)
