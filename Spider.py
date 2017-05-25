"""
file: Spider.py
Spider class
author Petri Lamminaho 
File stared 25.5.2017 
file modified 25.5.2017  Class made not tested  
"""

from urllib.request import urlopen
from link_finder import LinkFinder
from Grawler_general import *

# start of class


class Spider:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file_name = ''
    crawled_file_name = ''
    queue_files_set = set()
    crawled_files_set = set()

# constructor
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file_name = Spider.project_name + '/queue.txt'
        Spider.crawled_file_name = Spider.project_name + '/crawled.txt'
        self.boot()

    @staticmethod
    def boot():
        create_projet_directory(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue_files_set = file_to_set(Spider.queue_file_name)
        Spider.crawled_files_set = file_to_set(Spider.crawled_file_name)

    @staticmethod
    def craw_page(thread_name, page_url):
        if page_url not in Spider.crawled_files_set:
            print(thread_name + ' crawling ' + page_url)
            print("Queue pages " + str(len(Spider.queue_files_set))
                  + " | Crawled pages" + str(len(Spider.crawled_files_set)))
            Spider.add_links_to_waiting_list(Spider.gather_links(page_url))
            Spider.queue_files_set.remove(page_url)
            Spider.crawled_files_set(page_url)
            Spider.update_files()

    @staticmethod
    def add_links_to_waiting_list(links):
        for url in links:
            if url in Spider.queue_files_set:
                continue
            if url in Spider.crawled_files_set:
                continue
            if Spider.domain_name not in url:
                continue

            Spider.queue_files_set.add(url)

    @staticmethod
    def gather_links(page_url):
        html_str = ""
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html':
                html_bytes = response.read()
                html_str = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_str)

        except:
            print("Error: can not find page")
            return set()
        return finder.get_links()

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_files_set, Spider.queue_file_name)
        set_to_file(Spider.crawled_files_set,Spider.crawled_file_name)
