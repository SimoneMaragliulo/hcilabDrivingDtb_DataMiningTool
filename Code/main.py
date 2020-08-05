#%%

"""Packages import"""
import os
import sys
import pandas as pd
import easygui as g
from datetime import datetime
from guiFunctions import ParticipantSelection,ZoneSelection,TagsSelection
from figFunctions import AuxInfoFig,AccelFig,BioFig, MapFig
from auxFunctions import FeatureExtraction, append_list_as_row

"""Directories init"""
dataset_dir = "..\Data\dataset_web"   

#%% 

"""User inputs"""
participant = ParticipantSelection()
zone        = ZoneSelection()                                                                                            

"""Reading from database"""
ReadingFile = os.path.join(dataset_dir                                         
                            + participant + "." + 'csv')
dataRaw = pd.read_csv(ReadingFile, sep = ';')

#%% 

"""data selection and zone delimitation via GPS coordinates"""
if (zone == "zone 1: Longitude<9.08"):
    z1_Long_Lim = 9.08
    data = dataRaw[(dataRaw.Longitude_GPS < z1_Long_Lim)]
elif(zone == "zone 2: Latitude<48.708"):
    z2_Lat_Lim = 48.708
    data = dataRaw[(dataRaw.Latitude_GPS < z2_Lat_Lim)]
elif(zone == "zone 3: Longitude>9.16 & Latitude>48.72"):
    z3_Long_Lim = 9.16   
    z3_Lat_Lim = 48.72
    data = dataRaw[(dataRaw.Longitude_GPS > z3_Long_Lim)]
    data = data[(data.Latitude_GPS > z3_Lat_Lim)]
elif(zone == "Full path"):
    data = dataRaw
else:
    print('Error: The user shall select a zone')
    sys.exit()

"""Event picking"""
onPick_vect = MapFig(data, dataRaw)

#%% 

"""Start Analysis and database populating"""

msg = "Only the last 2 selected points "+\
    "will be considered for computation."+\
    "\n\nDo you want to continue?"
choices = ["Yes","Cancel process"]
reply = g.buttonbox(msg, choices=choices)

if (reply == "Cancel process"):
    
    print('Process cancelled by user request')
    sys.exit()
    
elif (reply == "Yes"):
    
    if(onPick_vect.count(0) >= 1):
        
        print('Error: The user shall pick 2 points on the map')
        sys.exit()
        
    else: 
        
        now = datetime.now()
        participant_num = participant.partition("_")[2]
        dt_string = now.strftime("%d%m%Y_%H%M%S")
        onPick_vect.sort()
        dataSlct = dataRaw[data.index[onPick_vect[0]]:
                           data.index[onPick_vect[1]]]
            
        AuxInfoFig(dataSlct,participant_num, dt_string)
        AccelFig(dataSlct,participant_num, dt_string)
        BioFig(dataSlct,participant_num, dt_string)
        
        Ext = FeatureExtraction(dataSlct)
        Tags = TagsSelection()
        
        records = [dt_string,
                   participant_num,
                   data.index[onPick_vect[0]],
                   data.index[onPick_vect[1]],                 
                   Tags,                   
                   Ext.AccX_max,Ext.AccX_min,
                   Ext.AccX_mean,Ext.AccX_std,                   
                   Ext.AccY_max,Ext.AccY_min,
                   Ext.AccY_mean,Ext.AccY_std,                   
                   Ext.AccZ_max,Ext.AccZ_min,
                   Ext.AccZ_mean,Ext.AccZ_std,                   
                   Ext.Alt_max,Ext.Alt_min,Ext.Alt_mean,                   
                   Ext.Lat_max,Ext.Lat_min,                   
                   Ext.Lng_max,Ext.Lng_min,                   
                   Ext.Spd_max,Ext.Spd_min,Ext.Spd_mean,                   
                   Ext.Lght_max,Ext.Lght_min,
                   Ext.Lght_mean,Ext.Lght_med,                   
                   Ext.HR_max,Ext.HR_min,Ext.HR_mean,                   
                   Ext.SCR_max,Ext.SCR_min,
                   Ext.SCR_mean,Ext.SCR_std,                   
                   Ext.T_max,Ext.T_min,Ext.T_mean]
        append_list_as_row('..\Results\EventDtb.csv', records)
        
else:
    sys.exit()
    
    


    
    