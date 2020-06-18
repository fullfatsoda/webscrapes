# uses data from finnhub api covid 19 tracker for US stats
# displays the number of active cases and deaths in each state
import requests

# you will need to get an api key from https://finnhub.io and enter it here
key = ''

us_data = requests.get('https://finnhub.io/api/v1/covid19/us?token=' + key)
us_data_json = us_data.json()
try:
    for i in range(len(us_data_json)):
        state = us_data_json[i]['state']
        cases = us_data_json[i]['case']
        deaths = us_data_json[i]['death']
        print(f"State : {state}\nCases : {cases}\nDeaths: {deaths}\n")
except:
    # possibly a 500 server error?
    status = requests.get('https://finnhub.io/api/v1/covid19/us?token=' + key)
    print(status)
