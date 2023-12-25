import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
api_key="**********************************"
##https://www.twilio.com/docs/messaging/quickstart/python
account_sid= "****************************"
auth_token="**************************"

weather_params={
	"lat":51.507351,
	"lon":-0.127758,
	"appid": api_key,
	"cnt": 4,
}
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data=response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain=False

for hour_data in weather_data["list"]:
	condition_code=(hour_data["weather"][0]["id"])
	if int(condition_code) < 700:
		will_rain=True

if will_rain:
	proxy_client=TwilioHttpClient()
	proxy_client.session.proxies={'https': os.environ['https_proxy']}
	client=Client(account_sid,auth_token,http_client=proxy_client)
	message=client.messages\
	.create(
		body="It's goingto rain today. You must to bring an umbrella☂️",
		from_='************',
		to='**************'
	)

	print(message.status)


