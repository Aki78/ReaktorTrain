import requests
import xmltodict

# Parse the XML data
xml_data = requests.get('http://assignments.reaktor.com/birdnest/drones').text
test = xmltodict.parse(xml_data)
try:
    print(test["report"]["deviceInformation"])
    print(test["report"]["capture"]["drone"][1]["positionX"])
    print(test["report"]["capture"]["drone"][1]["positionY"])
except:
    print("error")
