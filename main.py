b"""
File: main.py 
Author Petri Lammianho 


"""


import sys
import threading
from queue import Queue
from Spider import Spider
from Domain import *
from Grawler_general import *

arglist = sys.argv
if len(arglist) < 3 :
    PROJECT_NAME = input("Give project name>")
    HOMEPAGE = input("Give web page>")
    #sys.stderr.write("E: Usage " + arglist[0] + "<project name> <web page>")
    #sys.stderr.flush()
    #exit(2)

else:
    PROJECT_NAME = arglist[1]
    HOMEPAGE = arglist[2] #'http://yle.fi/'

DOMAIN_NAME = get_domain_name(HOMEPAGE)
WAITING_LIST_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_SPIDERS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()



def create_spiders():
    for _ in range(NUMBER_OF_SPIDERS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def create_jobs():
    for link in file_to_set(WAITING_LIST_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    links = file_to_set(WAITING_LIST_FILE)
    if len(links)>0:
        print(str(len(WAITING_LIST_FILE)) + ' links to waiting list')
        create_jobs()




create_spiders()
crawl()