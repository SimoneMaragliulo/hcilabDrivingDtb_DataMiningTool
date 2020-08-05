# hcilabDrivingDtb_DataMiningTool
Semi-automatic, single threaded application to support data mining operations on the "Driving Dataset" from hcilab 

# Description
The passion for human machine interfaces, for the mechatronic sector and for the data analysis, together with the desire of learning about python, bring me to discover hcilab and their public datasets (https://www.hcilab.org/datasets/). In particular, the "Driving Dataset" was very appealing to me. It is part of the results achieved by a research meant to assess the drivers workload. The research focuses on recording drivers physiological data, while at the wheel and by the mean of non-obtrusive approaches (https://www.hcilab.org/research/hcilab-driving-dataset/). 

Because of its nature, the data set needs of intermediate data mining operations in order to prepare the ground for a statistical data analysis. 
The hcilabDrivingDtb_DataMiningTool aims to support the Driving Dataset users  with an interactive GUI through the data mining operations. As side objective, the tool wants to provide the user with a lightweight SW module that lends itself well to small adjustments, to add-on expansions and to integration into larger engineering tools frameworks.

The workflow can be described as follows: 

Data file selection and reading  --> Event extraction via path selection (Interactive GUI)  --> Raw signals plotting --> Raw signals basic statistical feature extraction --> Event classification via tags assignment --> New database populating with extracted features and operations metadata

The tool has been developed with Python 3.7.6
Used packages:
* numpy
* pandas
* os
* sys
* matplotlib
* easygui
* datetime
* csv
* Ad hoc built packages

# Usage instructions
Before to run: 
* Download the repository content and unzip it 
* Download the data set from https://www.hcilab.org/research/hcilab-driving-dataset/ and unzip it
* Copy ..\hcilab_driving_dataset\dataset_web folder into ..\Data folder of hcilabDrivingDtb_DataMiningTool 

How to successfully run the tool: 
* Make sure that ..\Code folder is your working directory
* Run main.py script
* Select the data campaign participant via choicebox 
* Select the subzone of which you want to visualize the map
* Select the path/events on an interactive plot with a points picking approach

![](/Images/PathSelectorInteractiveGUI.PNG) 

* Visualize raw data plots
* Classify with tags the selected path/event via mltchoicebox 
* Check the results into ../Results/EventDtb.csv
