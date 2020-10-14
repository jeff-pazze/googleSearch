import random
import numpy as np
import os
import time
import glob
import time
import csv
import sys
from googlesearch import search

def csv_save(my_results_list):
        
        with open("googlesearch.csv" , 'a', newline = '') as saida:
          escrever = csv.writer(saida)
          escrever.writerow([my_results_list])

query = "jeferson pazze"

my_results_list = []
for i in search(query,        # The query you want to run
                tld = 'com',  # The top level domain
                lang = 'en',  # The language
                num = 100,    # Number of results per page
                start = 0,    # First result to retrieve
                stop = 10,    # Last result to retrieve
                pause = 2.0,  # Lapse between HTTP requests
               ):
    my_results_list.append(i)
    print(i)
    csv_save(i)
