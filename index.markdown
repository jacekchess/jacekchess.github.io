---
layout: home
---

Big city life can be full of surprises, opportunities, and positive and negative emotions, all of which happen at an extremely fast pace. For the citizens of San Francisco, with a population just below a million, such a life is a daily routine. It is no surprise, that some of them need to decompress after a tough week in the local bar. However, some of this decompression may result in a hectic night...

<div style="background-color: #f0f0f0; border: 1px solid #dcdcdc; border-radius: 5px; padding: 10px;">
<b>About the dataset</b>
<br>
The City and County of San Francisco provides a bunch of datasets enabling us to get insights into the city life, among others an extensive historical record of reported incidents to the San Francisco Police Department (SFPD) from 2003 to May 2018 [\[1\]](#References). This dataset encompasses a wide range of criminal incidents, including but not limited to thefts, assaults, burglaries, robberies, vandalism, drug offenses, and other public safety-related incidents.
<br>
This dataset serves as a valuable resource for various stakeholders, including law enforcement agencies, researchers, policymakers, urban planners, and the general public. It can be utilized for crime analysis, research, policy development, community engagement, and public safety planning initiatives aimed at improving the overall well-being and safety of residents in San Francisco.
</div>

In our research, we decided to look closer at the most popular party districts in San Francisco [\[2\]](#References) and analyze the crimes that happen there. Our goal is to find out when the party takes the out-of-law turn, where it happens, and what kind of crimes we should watch out for. The answers to these questions may help to improve safety in the "The Golden City".

### **Are parties crime triggers?** 

<embed 
       type="text/html" 
       src="/plots/heatmap_with_time.html"
       width="750"
       height="600"
       >

*Figure 1: Crimes related to drugs, alcohol, prostitution, gambling, and vandalism that were commited in 2017 between 18:00 and 5:00. In the hourly transition presented in the visualization, we can observe that the number of crimes is slowly decreasing in the party places, to reach significantly lower level around 5:00.*

Our spatial analysis confirms, that during the night, rush hours in the party places lead to the increase in crime numbers. The least crimeful place out of the ones we analyze turns out to be the Marina district, as it is slightly isolated from the rest of the party life. Crimes committed in the night hours reach a peak around midnight, and later slowly decrease. The party time ends at 5:00, when the crime rate comes back to the daytime levels. 

### **Which areas are the most crime-prone?**

The analysis presented in Figure 1 does not provide any quantitive measure of how many crimes are committed around the party locations. We observed that the Marina District seems to have fewer crimes, but it was difficult to find the most dangerous place. In the time series analysis presented in Figure 2, we investigate how the number of crimes changed in the party locations, to find out, which is historically infamous for being the crimeful one.

<embed 
       type="text/html" 
       src="/plots/bokeh_plot.html"
       width="750"
       height="500"
       >

*Figure 2: Number of crimes related to drugs, alcohol, prostitution, gambling, and vandalism committed from 2003 to 2018 in popular party destinations around the San Francisco city.*

Figure 2 reveals, that the San Francisco Police Department managed to achieve a significant decrease in the number of crimes committed around party locations. The number of crimes is over twice as low in 2018 compared to the 2008 status. This achievement would not be possible without improving safety around the most dangerous party place - centrally located Theater District. The number of crimes committed around that area is still the highest, but it is only a fraction of what we observed a decade before.

### **Are weekends more dangerous?** 

In order to get more insight into the nightlife hubs in San Francisco and their potential impact on the crime occurrences, we looked closely at the selected areas and crimes that were commited there. We then picked and investigated the most interesting changes in time in crimes connected with parties. 

![Text](plots/polar.png)

*Figure 3: Crimes related to vandalism, prostitution, drunkenness and driving under influence. The numbers in the plots show crimes committed per day to account for the different number of days between the weekend and weekdays. The weekend crimes are defined here as these occurring between the 12pm on Friday and 12pm on Sunday.*

The analysis of hourly crimes commited prove that the behaviors of offenders are different during the weekend and during the weekdays. There are more crimes during the weekends and they are in some cases shifted towards evening hours. It comes without surprise that drunkenness and driving under influence are more common during late weekend nights. Vandalism and prostitution, however, have similar hourly distribution, but are just more frequently committed during the weekends.

### **Conclusions**

Nightlife in San Francisco appears to be very vivid. It spans across half of the city, so there are plenty options to spend a night out. If you are looking for a quiet place, where you can spend fun time without risking getting into trouble, we would recommend checking Marina District and Polk Street. On the other hand, Theater District might be the place you would rather avoid, even though it is much safer then it used to be. Additionaly, avoiding crowds may be a good tactic to ensure safety - going out during weekdays and avoiding rush hours (23:00 - 01:00).

### **References**

1. SF Police Department Incident Reports: Historical 2003 to May 2018, [https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry/](https://data.sfgov.org/Public-Safety/Police-Department-Incident-Reports-Historical-2003/tmnf-yvry/)
2. San Francisco Nightlife, [https://www.extranomical.com/san-francisco-nightlife/](https://www.extranomical.com/san-francisco-nightlife/)

### **Contributions**

Part 1: Jacek Wiśniewski (s222678)

Part 2: Agata Makarewicz (s201773)

Part 3: Jakub Wiśniewski (s230212)