"""
File: Grawler.py 
Simple Web grawler "General functions" 
Author: Petri Lamminaho
File stared 24th of  May 2017 

"""
import os


# Create new project.
# Project is website your crawling
def create_projet_directory(directory):
    if not os.path.exists(directory):
        print("Creating directory " + directory)
        os.makedirs(directory)


# Create new data file
def create_data_files(project_name, base_url):
    waiting_list_page = project_name + '/queue.txt'
    completed_page = project_name + '/crawled.txt'
    if not os.path.isfile(waiting_list_page):
        print("Creating new data files")
        write_file(waiting_list_page, base_url)
        write_file(completed_page, '')


# write data to file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add new line(link) to file
def append_data_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# create new empty file same name that old file
def empty_file_content(path):
    with open(path, 'w'):
        pass


# save file contents to set
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ' '))
    return result


# convert and save set to file
def set_to_file(links, file):
    empty_file_content(file)
    for link in sorted(links):
        append_data_to_file(file, link)




# test
# create_projet_directory("jyu")
# create_projet_directory("mtv3")
# create_data_files('jyu', 'jyu.fi')
