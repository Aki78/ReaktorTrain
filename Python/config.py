#Globals

#Connection
USER = "root"
PASSWORD = "root"
HOST = "localhost"
DB = "naughty"

#URLs
BASE_URL = 'http://assignments.reaktor.com/birdnest/drones'
BASE_PILOT_URL = "http://assignments.reaktor.com/birdnest/pilots/"

#Table names
PILOT_TABLE_NAME = "naughty_pilot_info"
VIOLATION_TABLE_NAME = "violation_info"

# call data snapshot 
POOL_TIME = 1 # make sure to have smaller than 2 seconds for realtime update


CENTER_POINT = 250000 # In mm, both X_0 and Y_0 being the same
ZONE_RANGE = 100000 # In mm
