import os
import pandas

project_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = project_dir + '/data/'
pandas.read_csv(data_dir + 'flights.csv')




