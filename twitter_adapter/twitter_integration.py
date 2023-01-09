import tweepy

# This will import the Twarc2 client and expansions class from twarc library and also the json library
from twarc import Twarc2, expansions
import json
import datetime
import requests
from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened

# Bearer tokens
bearer_tok = "AAAAAAAAAAAAAAAAAAAAACO1kgEAAAAAkaYcSL3tvkA%2FHfZegkGHVCl6FMw%3DuNX3p9Dk0Hp3sDQpBCTjls98G2iYZtfzuqARuMkd6Hwu7kNl7l"


t = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAACO1kgEAAAAAkaYcSL3tvkA%2FHfZegkGHVCl6FMw%3DuNX3p9Dk0Hp3sDQpBCTjls98G2iYZtfzuqARuMkd6Hwu7kNl7l")

# Start and end times must be in UTC
start_time = datetime.datetime(2022, 12, 21, 0, 0, 0, 0, datetime.timezone.utc)
end_time = datetime.datetime(2022, 12, 22, 0, 0, 0, 0, datetime.timezone.utc)

# search_results is a generator, max_results is max tweets per page, 100 max for full archive search with all expansions.
search_results = t.search_all(query="dogs lang:en -is:retweet", start_time=start_time, end_time=end_time, max_results=50)

# Get all results page by page:
for page in search_results:
    # Do something with the whole page of results:
    # print(page)
    # or alternatively, "flatten" results returning 1 tweet at a time, with expansions inline:
    for tweet in ensure_flattened(page):
        # Do something with the tweet
        print(tweet)

    # Stop iteration prematurely, to only get 1 page of results.
    break


