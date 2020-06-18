import requests
# get current position of and who is onboard the international space station
# using the api http://api.open-notify.org

# get json data from pages
try:
    iss_now = requests.get('http://api.open-notify.org/iss-now.json').json()
    astronauts = requests.get('http://api.open-notify.org/astros.json').json()
    lat, lon = iss_now['iss_position']['latitude'], iss_now['iss_position']['longitude']
    print(f"ISS is currently at {lat} latitude and {lon} longitude.\nThe crew currently aboard consist of:")
    for crew in astronauts['people']:
        print(" - " + crew['name'])
except:
    # possibly a 500 server error?
    status = requests.get('http://api.open-notify.org/')
    print(status)
