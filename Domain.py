"""
file: Domain.py
author: Petri Lamminaho  
Started 26.5.2017

Parse the domain from web address 
"""
from  urllib.parse import urlparse

def get_domain_name(url):
    try:
        res = get_sub_domain_name(url).split('.')
        return res[-2] + '.' + res[-1]
    except:
        return ''


def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''


# test works
# print(get_sub_domain_name("https://www.jyu.fi/yhteystiedot")) # result is: www.jyu.fi
# print(get_domain_name("http://areena.yle.fi/tv/ohjelmat/uutiset")) # domain is yle.fi
# print(get_domain_name("https://www.jyu.fi/yhteystiedot"))# domain is jyu.fi
