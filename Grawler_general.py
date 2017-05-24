"""
     Grawler.py 
      Simple Web grawler 
      autthor: Petri Lamminaho
"""
import os

# project is website your grawling
def create_projet_directory(directory):
    if not os.path.exists(directory):
        print("Creating directory "+ directory)
        os.makedirs(directory)


create_projet_directory("jyu")
create_projet_directory("mtv3")