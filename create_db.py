
from specDB import average_1d_arr, datenum2stmp, stmp2datenum
import sqlite3
import astropy
# import astropy time
from astropy.time import Time
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

import os
import glob

# Define the start date and use today's date as the end date
start_date = datetime.datetime(2017, 1, 1,0,0,0)  # Start date (year, month, day)
end_date = datetime.date.today()        # Today's date as end date

time_compress_ratio = 5
fghz_get = np.linspace(1.5,17.5,17)

conn = sqlite3.connect('eovsa.db')
c = conn.cursor()

current_date = start_date
counter = 0
while current_date <= end_date:
    # Construct the file path for the current date
    date_str = current_date.strftime("%Y/%m/%d")
    file_pattern = f"/data1/eovsa/fits/synoptic/{date_str}/EOVSA_TPall_{current_date.strftime('%Y%m%d')}.fts"
    
    # Use glob to find files that match the pattern
    files = glob.glob(file_pattern)

    for fname in files:
        counter += 1
        hdulist = fits.open(fname)
        spec = hdulist[0].data
        fghz = np.array(astropy.table.Table(hdulist[1].data)['sfreq'])
        tim = astropy.table.Table(hdulist[2].data)
        tmjd= np.array(tim['mjd']) + np.array(tim['time']) / 24. / 3600 / 1000
        tim = Time(tmjd, format='mjd')
        timplt = tim.plot_date
        ntim = len(timplt)
        nfreq = len(fghz)


        # find indexID for frequency
        freq_GHz_id = []
        for i in range(0,17):
            # find closest frequency in fghz 
            freq_GHz_id.append(np.argmin(np.abs(fghz_get[i] - fghz)))

        data_insert = spec[freq_GHz_id,]

        # downsample in time
        timplt = average_1d_arr(timplt, n=time_compress_ratio)
        data_insert_small = np.zeros((17, ntim//time_compress_ratio))
        for i in range(0,17):
            data_insert_small[i,:] = average_1d_arr(data_insert[i,:], n=time_compress_ratio)

        data_insert_small[np.isnan(data_insert_small)] = -1

        # convert to stmp
        stmp = np.array([datenum2stmp(i) for i in timplt])
        
        for i in range(len(stmp)):
            # Prepare a tuple for insertion
            data_tuple = (str(stmp[i]),) + tuple(data_insert_small[:, i])
            # Insert or replace data into database
            c.execute("INSERT OR REPLACE INTO eovsa VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data_tuple)

        if counter % 100 == 0:
            print(f"Processed {counter} files, current date: {current_date.strftime('%Y-%m-%d')}")
            conn.commit()
    # Move to the next day
    current_date += datetime.timedelta(days=1)


conn.commit()
conn.close()