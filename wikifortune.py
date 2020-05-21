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
           'Portal:',
           'Wikipedia talk:',
           'Draft talk:',
           'Module talk:',
           'Template talk:',
           'Portal talk:',
           'Module:']
           

    while True:
        out=((request.get(url='https://en.wikipedia.org/w/api.php', 
                params={'action':'query',
                        'format':'json',
                        'list':'random',
                        'rnlimit':'10'
                        })).json())['query']['random']
        
        for i in out:
            if not (any(k in i['title'] for k in pages)):
                return(i['title'])
            else:
                continue
            
def get_fortune(article):
    return((request.get(url='https://en.wikipedia.org/w/api.php',
                      params={'action':'query',
                              'format':'json',
                              'list':'search',
                              'srsearch':article})).json()['query']['search'][0]['snippet'])

def plaintext(html):
    
    html_start=0
    replaced={'&quot;': '"',
            '&lt;': '<',
            '&gt;': '>',
            '&amp;': '&',
            '&copy;': '©',
            '&trade;':'™',
            '&nbsp;': ' ',
            '&#??;': '??'}
       
    while True:
        for letter in range(len(html)):
            if html[letter]=='<':
                html_start=letter
            elif html[letter]=='>':
                html=html[:html_start] + html[letter+1:]
                break
        if '>' in html:
            continue
        
        for k, v in replaced.items():
            html=html.replace(k, v)
        return(html)
        
article_name=get_article()
print(plaintext(get_fortune(article_name)+'....\nMore: https://en.wikipedia.org/wiki/'+(article_name.replace(' ', '_'))))




