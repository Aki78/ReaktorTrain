import requests
import time

while True:
    r = requests.get('http://aki78.pythonanywhere.com/fetch_drones')
    print(r.status_code)
    time.sleep(1)
