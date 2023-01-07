import utils

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
        self.timestamp = drone_data["timestamp"]
        self.is_naughty = utils.is_in_bad_zone(self.x,self.y)
        self.distance =  utils.get_distance_in_meters(self.x,self.y)
