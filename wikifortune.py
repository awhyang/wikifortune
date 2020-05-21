#!/usr/bin/python

import requests

request=requests.Session()

def get_article():
    pages=['User talk:',
           'Talk:',
           'User:',
           'Template',
           'File:',
           'Category:',
           'Wikipedia:',
           'Category talk:',
           'Map:',
           'File talk:',
           'Draft:',
           'Portal:']
    
    while True:
        out=((request.get(url='https://en.wikipedia.org/w/api.php', 
                params={'action':'query',
                        'format':'json',
                        'list':'random',
                        'rnlimit':'10'
                        })).json())['query']['random']

            #requests a list of 10 random wikipedia pages        
        
        for i in out:
            if not (any(k in i['title'] for k in pages)):
                return(i['title'])
            else:
                continue
            
            #filters pages[i] and returns first proper article

def get_fortune(article):
    return((request.get(url='https://en.wikipedia.org/w/api.php',
                      params={'action':'query',
                              'format':'json',
                              'list':'search',
                              'srsearch':article})).json()['query']['search'][0]['snippet'])

def plaintext(html):
    
    html=html.replace('&quot;', '"').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&copy;', '©').replace('&trade;','™').replace('&nbsp;', ' ').replace('&#??;', '??')
    html_start=0

    #removes html
    while True:
        for letter in range(len(html)):
            if html[letter]=='<':
                html_start=letter
            if html[letter]=='>':
                html=html[:html_start] + html[letter+1:]
                break
        if '>' in html:
            continue
        return(html)

article_name=get_article()
print(plaintext(get_fortune(article_name)+'....\nMore: https://en.wikipedia.org/wiki/'+(article_name.replace(' ', '_'))))




