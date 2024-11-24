
import os, sys
import re, csv
import pandas as pd
import shutil
import sqlite3
from sqlite3 import Error

from datetime import datetime

TFM_name = 'TFM_get_web_page'
csv_TFM_specs = '../data/raw/1.TFM_specs.csv'
csv_TFM_hosts = '../../data/raw/2.TFM_hosts.csv'
csv_TFM_nodes = '../../data/raw/nodes.csv'

folder_var_www_html = '/var/www/html'
hosts_folder_TFM_ALL = '/TFM_ALL'
folder_SERVER_CLUSTER_0 = '/SERVER_CLUSTER_0'

folder_TFM_SOURCE = '/TFM_SOURCE'
folder_TFM_DEPLOY = '../../TFM_DEPLOY'

folder_MASTER_data_LOG = '../data/cooked/LOG_nodes/'



#if __name__ == "__main__":
   #print (os.listdir (folder_TFM_DEPLOY + '/' + TFM_name + '/data/raw/'))
   #print (os.listdir(folder_MASTER_data_LOG))