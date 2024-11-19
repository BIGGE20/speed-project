import requests,json

url= "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

if response.status_code == 200:
    response_dict = json.loads(response.text)
    position = response_dict['iss_position']
    print(f"The international space station is now on latitude{position['latitude']} and longitude {position['longitude']}")


else:
    print(f"Badagry,there is a problem {response.status_code}")

