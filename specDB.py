
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime


# create primary key (stmp) for the database in sqlite3

def datenum2stmp(dn):
    return int(mdates.num2date(dn).timestamp())

def stmp2datenum(stmp):
    return mdates.date2num(datetime.fromtimestamp(stmp))

def average_1d_arr(data, n=10):
    # Truncate the array to a length that is a multiple of n
    length = len(data) - len(data) % n
    truncated_data = data[:length]

    # Reshape the truncated data into a 2D array where each row has n elements
    reshaped_data = truncated_data.reshape(-1, n)
    # Calculate the average along the rows
    averaged_data = np.mean(reshaped_data, axis=1)
    return averaged_data