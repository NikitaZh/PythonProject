__author__ = 'IrinaPavlova'
Задание: программа спрашивает у пользователя код языка и выдает ему ссылку, по которой он может скачать себе
последний дамп на этом языке(из википедии)
'''
import urllib.request as urlr
import re
import xlrd
import pandas as pd
from xlrd import open_workbook, cellname

my_dic = pd.read_excel('ISO 639-2.xlsx', header=None, index_col=1).to_dict()
language_codes = my_dic[0]
language_codes = dict((k.lower(), v.lower()) for k,v in language_codes.items())

request = input('Enter the language: ').lower()
print('We process... Please wait.')

try:
    lang_code = language_codes[str(request)]
except KeyError:
    print('Sorry, it is not a valid language name.')


page = urlr.urlopen('https://dumps.wikimedia.org/'+ lang_code + 'wiki/latest')

page_r = page.read().decode('utf-8')
page_l = page_r.split('\n')

s = re.compile('.*latest-pages-articles\.xml\.bz2')

for line in page_l:
    if s.search(line) == None:
        pass
    else:
        title = re.search('>(.*?)<', line).group(1)
        adr = 'https://dumps.wikimedia.org/'+ lang_code + 'wiki/latest/' + title
        break

urlr.urlretrieve(adr, title)




'''
Ссылка:
https://dumps.wikimedia.org/ruwiki/latest/ruwiki-latest-pages-articles.xml.bz2
'''


