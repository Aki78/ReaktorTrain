import requests
import time
import xmltodict
from hashlib import sha256
sha_old = ""
while True:
    # Parse the XML data
    xml_data = requests.get('http://assignments.reaktor.com/birdnest/drones').text
    sha_value = sha256(xml_data.encode('utf-8')).hexdigest()
    print(sha_value == sha_old)
    # Checking if it is the same or not from before
    if sha_value != sha_old:
        sha_old = sha_value
        test = xmltodict.parse(xml_data)
        incoming_drones =  test["report"]["capture"]["drone"]
        try:
            print(test["report"]["deviceInformation"])
            print(test["report"]["capture"]["drone"][1]["positionX"])
            print(test["report"]["capture"]["drone"][1]["positionY"])
        except:
            print("error")

        if type(incoming_drones) == list:
            print(incoming_drones)
        else:
            raise Exception(TypeError)

        drone_data = []
        # position int because there is no point storing data in micrometers or nanometers
        for i in  incoming_drones:
            x =  int(float(i["positionX"]))
            y =  int(float(i["positionY"]))
            drone_data.append({"id":i["serialNumber"], "pos":(x,y)})
        print(drone_data)
        time.sleep(1)
