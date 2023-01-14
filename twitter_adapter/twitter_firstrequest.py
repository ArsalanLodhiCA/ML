import requests
import pandas as pd
import os

# bearer_token = os.environ.get('BEARER_TOKEN')
bearer_token = "AAAAAAAAAAAAAAAAAAAAACO1kgEAAAAAkaYcSL3tvkA%2FHfZegkGHVCl6FMw%3DuNX3p9Dk0Hp3sDQpBCTjls98G2iYZtfzuqARuMkd6Hwu7kNl7l"
headers = {"Authorization": "Bearer {}".format(bearer_token)}

url = "https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev"
response = requests.request("GET", url, headers=headers).json()

df = pd.DataFrame(response['data'])
df.to_csv('./response_python.csv')


