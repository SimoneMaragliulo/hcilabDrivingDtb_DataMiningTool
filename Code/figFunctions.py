
# figFunctions.py 
#%%
"""Packages import"""
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np
import os

#%%
def AuxInfoFig(dataSlct,participant_num, dt_string):
    Time_Vect = [dt.datetime.strptime(d,'%H:%M:%S:%f')
                 for d in list(dataSlct.Time_GPS)]
    fig = plt.figure()
    ax = plt.subplot(3,1,1)
    plt.fill_between(Time_Vect, dataSlct.Altitude_GPS)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Altitude m'),plt.xlabel('Time')
    plt.title('Aux channels')
    ax.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.Altitude_GPS)-Border,
             max(dataSlct.Altitude_GPS)+Border)
    
    
    ax1 = plt.subplot(3,1,2, sharex = ax)
    plt.fill_between(Time_Vect, dataSlct.Speed_GPS)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Speed mph'),plt.xlabel('Time')
    ax1.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.Speed_GPS)-Border,
             max(dataSlct.Speed_GPS)+Border)
    
    
    ax2 = plt.subplot(3,1,3, sharex = ax1)
    plt.fill_between(Time_Vect, dataSlct.Lightning)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Ligh lumen'),plt.xlabel('Time')
    ax2.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.Lightning)-Border,
             max(dataSlct.Lightning)+Border)
    plt.show()
    
def AccelFig(dataSlct,participant_num, dt_string):
    Time_Vect = [dt.datetime.strptime(d,'%H:%M:%S:%f')
                 for d in list(dataSlct.Time_Accel)]
    fig = plt.figure()
    ax = plt.subplot(3,1,1)
    plt.plot(Time_Vect, dataSlct.AccelX)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('AccX m/s2 \nLateral'),plt.xlabel('Time')
    plt.title('Acceleration from smartphone')
    ax.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.AccelX)-Border,
             max(dataSlct.AccelX)+Border)
    
    
    ax1 = plt.subplot(3,1,2, sharex = ax)
    plt.plot(Time_Vect, dataSlct.AccelY)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('AccY m/s2 \nVertical'),plt.xlabel('Time')
    ax1.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.AccelY)-Border,
             max(dataSlct.AccelY)+Border)
    
    
    ax2 = plt.subplot(3,1,3, sharex = ax1)
    plt.plot(Time_Vect, dataSlct.AccelZ)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('AccZ m/s2 \nLongitudinal'),plt.xlabel('Time')
    ax2.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.AccelZ)-Border,
             max(dataSlct.AccelZ)+Border)
    
    plt.show()
    
    
def BioFig(dataSlct,participant_num, dt_string):
    Time_Vect = [dt.datetime.strptime(d,'%H:%M:%S:%f')
                 for d in list(dataSlct.Time_Biotrace)]
    fig = plt.figure()
    ax = plt.subplot(3,1,1)
    plt.plot(Time_Vect, dataSlct.Temp)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Body \nTemperature °C'),plt.xlabel('Time')
    plt.title('Physiological data')
    ax.yaxis.set_label_position('right')
    Border =  0.2
    plt.ylim(min(dataSlct.Temp)-Border,
             max(dataSlct.Temp)+Border)
    
    
    ax1 = plt.subplot(3,1,2, sharex = ax)
    plt.plot(Time_Vect, dataSlct.HR)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Heart \nrate bpm'),plt.xlabel('Time')
    ax1.yaxis.set_label_position('right')
    Border = 2
    plt.ylim(min(dataSlct.HR)-Border,
             max(dataSlct.HR)+Border)
    
    
    ax2 = plt.subplot(3,1,3, sharex = ax1)
    plt.plot(Time_Vect, dataSlct.SCR)
    plt.gcf().autofmt_xdate()
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Skin \nConductance µS'),plt.xlabel('Time')
    ax2.yaxis.set_label_position('right')
    Border = 1
    plt.ylim(min(dataSlct.SCR)-Border,
             max(dataSlct.SCR)+Border)
    
    plt.show()
    
    
    
def MapFig(data, dataRaw):
    """Variables init"""
    # Time_Vect_GPS = [dt.datetime.strptime(d,'%H:%M:%S:%f')
    #                  for d in list(data.Time_GPS)]
    data.drop_duplicates(subset ="Longitude_GPS", 
                         keep = 'first', inplace = True) 
    cmap = plt.cm.RdYlGn
    norm = plt.Normalize(1,4)
    onPick_vect = [0,0]
    MarkSize = 100
    MarkSize1 = 10
    MarkSize2 = 15
    Border_Lim = 0.001
    StpArr_Lim = 0.0002
    x = data.Longitude_GPS.tolist()
    y = data.Latitude_GPS.tolist()
    c = data.Altitude_GPS.tolist()
    names = np.array(data.Time_GPS.tolist())
    
    """Figure"""
    fig = plt.figure()
    ax = plt.subplot()
    plt.scatter(dataRaw.Longitude_GPS,
                dataRaw.Latitude_GPS,marker='o', color = 'lightblue')
    sc = plt.scatter(data.Longitude_GPS,
                     data.Latitude_GPS,c=c, s=MarkSize, picker=True)
    plt.ylim(min(data.Latitude_GPS)-Border_Lim,
             max(data.Latitude_GPS)+Border_Lim)
    plt.xlim(min(data.Longitude_GPS)-Border_Lim,
             max(data.Longitude_GPS)+Border_Lim)
    plt.plot(dataRaw.Longitude_GPS[data.index[0]],
             dataRaw.Latitude_GPS[data.index[0]], 'ro', markersize=MarkSize1,
             markeredgecolor = 'b',label='Start')
    plt.plot(dataRaw.Longitude_GPS[data.index[-1]],
             dataRaw.Latitude_GPS[data.index[-1]]+StpArr_Lim, 'rv', 
             markersize= MarkSize2,markeredgecolor = 'b',label='Stop')
    plt.grid(which='major', color='#CCCCCC', linestyle='--')
    plt.grid(which='minor', color='#CCCCCC', linestyle=':')
    plt.ylabel('Latitude'),plt.xlabel('Longitude')
    plt.title('GPS mapping: pick 2 points')
#    figManager = plt.get_current_fig_manager()
#    figManager.window.showMaximized()
    plt.legend(loc = 2)
    cbar = plt.colorbar(ax = ax);
    cbar.set_label('Altitude_GPS [m]')
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)
    
    def update_annot(ind):
        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "Time:{}".format(" ".join([names[n] for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch().set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)
    
    
    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()
                    
             
    def onpick3(event):
        ind = event.ind
        plt.plot(np.take(x, ind[0]), np.take(y, ind[0]), 'r*',
                 markersize= MarkSize2, markeredgecolor = 'b')
        onPick_vect[0] =  onPick_vect[1]
        onPick_vect[1] =  ind[0]
        return onPick_vect
        
        
    fig.canvas.mpl_connect('pick_event', onpick3)
    fig.canvas.mpl_connect("motion_notify_event", hover)
    plt.show()
    return onPick_vect