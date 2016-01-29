# -*- coding: utf8 -*-
from twitter import *
import re
token = '4845009934-sCsBzFY1HzVJGUZpn2IJthePy3DymfML86YTAKg'
token_key = '0rKMMQh3G8W82zddmYAnKRVyZ4d0heyEaZdQamVpA3iWH'
con_secret = 'uqd7kNdQ6rkEZref7P0FjtAgf'
con_secret_key = 'WKHt4JFdRTqLMFAagJM50fVs1NBegZEdHh7bpHxMIAB4remgNE'
t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key))

s = t.search.tweets(q='#сарказм')

#'text': 'Разгуливать по городу со зрением -5 без очков и линз вообще нормас. #сарказм'

m = re.findall('text\': \'(.*?)#сарказм(.*?)\'', s)
print(m)


#help(Twitter)
