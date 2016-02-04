from TwitterAPI import TwitterAPI
import re

access_token_key = '4845009934-sCsBzFY1HzVJGUZpn2IJthePy3DymfML86YTAKg'
access_token_secret = '0rKMMQh3G8W82zddmYAnKRVyZ4d0heyEaZdQamVpA3iWH'
consumer_key = 'uqd7kNdQ6rkEZref7P0FjtAgf'
consumer_secret = 'WKHt4JFdRTqLMFAagJM50fVs1NBegZEdHh7bpHxMIAB4remgNE'
proper_tweets = []
rtchecker = re.compile('[@|https]')
hashtagshecker = re.compile('#')

ids = []
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
aps = api.request('search/tweets', {'q': '#сарказм', 'until': '2016-02-04', 'count': 100})
for item in aps.get_iterator():
        ids.append(item['id'])
        m1 = rtchecker.search(item['text'])
        if m1 is None:
            m2 = hashtagshecker.findall(item['text'])
            if len(m2) > 2:
                proper_tweets.append(item['text'])

k = min(ids)-1
print('k is ', k)
#'until': '2016-02-04',
while k is not None and len(proper_tweets) <100:
    print('NEW PAGE')

    print(len(proper_tweets))
    aps = api.request('search/tweets', {'q': '#сарказм', 'count': 100, 'until': '2016-02-04', 'max_id': str(k)})
    for item1 in aps.get_iterator():
        ids.append(item1['id'])
        print('len of ids - ',len(ids))
        m3 = rtchecker.search(item1['text'])
        if m3 is None:
            m4 = hashtagshecker.findall(item1['text'])
            if len(m4) > 2:
                proper_tweets.append(item1['text'])

"""
    print('k is ', k)
    if len(ids) == 0:
        k -= 1
    else:
        k = min(ids)-1
    ids = []"""


print(proper_tweets[:10])








def req(ap, m):
    print('1')

    ids = []
    for item in aps.get_iterator():
        yield('TWEET\n', item)
        ids.append(item['id'])
    req(ap, str(min(ids()-1)))

#(req(aps,m))
