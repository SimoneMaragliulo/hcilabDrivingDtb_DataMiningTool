
# auxFunctions.py 
#%%
"""Packages import"""
import numpy as np
from csv import writer

#%%
def FeatureExtraction(dataSlct):

    class Extract:
        pass

    a = Extract()

    a.AccX_max = max(dataSlct.AccelX)
    a.AccX_min = min(dataSlct.AccelX)
    a.AccX_mean = np.mean(dataSlct.AccelX)
    a.AccX_std = np.std(dataSlct.AccelX)
        
    a.AccY_max = max(dataSlct.AccelY)
    a.AccY_min = min(dataSlct.AccelY)
    a.AccY_mean = np.mean(dataSlct.AccelY)
    a.AccY_std = np.std(dataSlct.AccelY)
        
    a.AccZ_max = max(dataSlct.AccelZ)
    a.AccZ_min = min(dataSlct.AccelZ)
    a.AccZ_mean = np.mean(dataSlct.AccelZ)
    a.AccZ_std = np.std(dataSlct.AccelZ)
        
    a.Alt_max = max(dataSlct.Altitude_GPS)
    a.Alt_min = min(dataSlct.Altitude_GPS)
    a.Alt_mean = np.mean(dataSlct.Altitude_GPS)
        
    a.Lng_max = max(dataSlct.Longitude_GPS)
    a.Lng_min = min(dataSlct.Longitude_GPS)
        
    a.Lat_max = max(dataSlct.Latitude_GPS)
    a.Lat_min = min(dataSlct.Latitude_GPS)
        
    a.Spd_max = max(dataSlct.Speed_GPS)
    a.Spd_min = min(dataSlct.Speed_GPS)
    a.Spd_mean = np.mean(dataSlct.Speed_GPS)
        
    a.Lght_max = max(dataSlct.Lightning)
    a.Lght_min = min(dataSlct.Lightning)
    a.Lght_mean = np.mean(dataSlct.Lightning)
    a.Lght_med = np.median(dataSlct.Lightning)
        
    a.T_max = max(dataSlct.Temp)
    a.T_min = min(dataSlct.Temp)
    a.T_mean = np.mean(dataSlct.Temp)
        
    a.HR_max = max(dataSlct.HR)
    a.HR_min = min(dataSlct.HR)
    a.HR_mean = np.mean(dataSlct.HR)
        
    a.SCR_max = max(dataSlct.SCR)
    a.SCR_min = min(dataSlct.SCR)
    a.SCR_mean = np.mean(dataSlct.SCR)
    a.SCR_std = np.std(dataSlct.SCR)
    
    return a


def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = writer(write_obj)
        csv_writer.writerow(list_of_elem)