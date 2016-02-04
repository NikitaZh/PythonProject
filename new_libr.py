from TwitterAPI import TwitterAPI
import re

access_token_key = '4845009934-sCsBzFY1HzVJGUZpn2IJthePy3DymfML86YTAKg'
access_token_secret = '0rKMMQh3G8W82zddmYAnKRVyZ4d0heyEaZdQamVpA3iWH'
consumer_key = 'uqd7kNdQ6rkEZref7P0FjtAgf'
consumer_secret = 'WKHt4JFdRTqLMFAagJM50fVs1NBegZEdHh7bpHxMIAB4remgNE'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)



def func(m=None):
    r = api.request('search/tweets', {'q': '#сарказм', 'count': 200, 'max_id': m})
    
    
    
    
    
ids = []
for item in r.get_iterator():
    print('TWEET\n', item)
    ids.append(item['id'])

print(min(ids))
