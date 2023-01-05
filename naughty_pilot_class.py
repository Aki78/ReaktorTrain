from datetime import datetime
#make sure to store only pilots who violated the rules for privacy reasons.
class NaughtyPilot():
    def __init__(self,drone,pilot_info):
        self.pilotId = pilot_info["pilotId"]
        self.firstName = pilot_info["firstName"]
        self.lastName = pilot_info["lastName"]
        self.phoneNumber = pilot_info["phoneNumber"]
        self.createdDt = datetime.strptime(pilot_info["createdDt"],"%Y-%m-%dT%H:%M:%S.%fZ")
        self.email = pilot_info["email"]
        #drone class
        self.drone = drone
        #timestamp int since 2 seconds is the interval. and pointless to store in milliseconds
        # self.timestamp = int(datetime.timestamp(datetime.now()))
        self.datetime = datetime.now()
