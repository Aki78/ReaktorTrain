class NaughtyPilot():
    def __init__(self,drone,pilot_info):
        self.pilotId = pilot_info["pilotId"]
        self.firstName = pilot_info["firstName"]
        self.lastName = pilot_info["lastName"]
        self.phoneNumber = pilot_info["phoneNumber"]
        self.createdDt = pilot_info["createdDt"]
        self.email = pilot_info["email"]
        #drone class
        self.drone = drone
