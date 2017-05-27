"""
File: LinkFinder.py 
Author: Petri Lamminaho 
Simple class that returns links from given web page
Made 24-25 May 2017
"""

from html.parser import HTMLParser
from urllib import parse




class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self. __base_url = base_url
        self. __page_url = page_url
        self. __links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value)in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self. __base_url, value)
                    self. __links.add(url)

    def get_links(self):
        return self. __links

    def error(self, message):
        print("Error")




#test
#finder = LinkFinder()
#finder.feed('<html> <head> <title> Testing </title> </head>'
          # '<body> <h1> Parse page </h1> </body> </html>')
