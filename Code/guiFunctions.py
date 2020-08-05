
# guiFunctions.py 
#%%
"""Packages import"""
import sys
import easygui as g

#%%
def TagsSelection():

    text = "Please select the tag/s for the event"
    title = "Event picker tool: Event classification"
    listOfOptions = ["Large curve R","Large curve L",
                          "Sharp turn R","Sharp turn L", 
                          "Speed Bump","Road sign #1",
                          "Road sign #2","Steep descendent",
                          "Steep climb","Gallery","City",
                          "HighWay", "Traffic Jam"]
    choice = g.multchoicebox(text , title, listOfOptions)
    if choice is None:
        print ("Error: Analysis aborted")
        sys.exit()
    return choice  



def ParticipantSelection():

    text = "Please select the campaign participant"
    title = "Event picker tool: Participant selection"
    listOfOptions = ["\participant_1","\participant_2",
                          "\participant_3","\participant_4", 
                          "\participant_5","\participant_6",
                          "\participant_7","\participant_8",
                          "\participant_9","\participant_10"]
    choice = g.choicebox(text , title, listOfOptions)
    if choice is None:
        print ("Error: The user shall select one participant")
        sys.exit()
    return choice

def ZoneSelection():

    text = "Please select the zone of the path you want to explore"
    title = "Event picker tool: Map zone selection"
    listOfOptions = ["zone 1: Longitude<9.08","zone 2: Latitude<48.708",
                          "zone 3: Longitude>9.16 & Latitude>48.72",
                          "Full path"]
    choice = g.choicebox(text , title, listOfOptions)
    if choice is None:
        print ("Error: The user shall select one zone")
        sys.exit()
    return choice