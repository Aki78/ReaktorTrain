import requests
from bs4 import BeautifulSoup
import xmltodict

# Parse the XML data
xml_data = requests.get('http://assignments.reaktor.com/birdnest/drones').text
soup = BeautifulSoup(xml_data, 'lxml')
print(xmltodict.parse(xml_data))

# Print the values of the XML data
for element in soup.find_all():
    print(element)
    # print(element.report, element.value)
