import pandas as pd


columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'car name']
df = pd.read_fwf('data/auto-mpg-data.txt', header=None)
df.columns= columns
