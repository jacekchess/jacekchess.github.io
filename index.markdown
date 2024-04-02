---
layout: home
---

Big city life can be full of surprises, opportunities, and positive and negative emotions, all of which happen at an extremely fast pace. For the citizens of San Francisco, with a population just below a million, such a life is a daily routine. It is no surprise, that some of them need to decompress after a tough week in the local bar. However, some of this decompression may result in a hectic night...


In our research, we decided to look closer at the most popular party districts in San Francisco ([link](https://www.extranomical.com/san-francisco-nightlife/)) and analyze the crimes that happen there. Our goal is to find out when the party takes the out-of-law turn, where it happens, and what kind of crimes we should watch out for. The answers to these questions may help to improve safety in the "The Golden City".

<embed 
       type="text/html" 
       src="/plots/heatmap_with_time.html"
       width="1100"
       height="600"
       >

*Figure 1: Crimes related to drugs, alcohol, prostitution, gambling, and vandalism that were commited in 2017 between 18:00 and 5:00. In the hourly transition presented in the visualization, we can observe that the number of crimes is slowly decreasing in the party places, to reach significantly lower level around 5:00.*


Our spatial analysis confirms, that during the night, rush hours in the party places lead to the increase in crime numbers. The least crimeful place out of the ones we analyze turns out to be the Marina district, as it is slightly isolated from the rest of the party life. Crimes committed in the night hours reach a peak around midnight, and later slowly decrease. The party time ends at 5:00, when the crime rate comes back to the daytime levels. 


To get even more information we looked closely at the selected areas and crimes that were commited there. We then picked and showed the most interesting changes in time in crimes connected with parties. 

![Text](plots/polar.png)

*Figure 2: Crimes related to Vandalism, Prostitution, Drunkness and Driving under influence. The numbers in the plots show crimes commited per day to account for the diffenret number of days between the weekend and weekdays. Here weekend crimes are ones that are done between the 12pm on Friday and 12pm on Sunday.*

The analysis of hourly crimes commited prove that the behaviors of offenders are different during the weekend and during the weekdays. There are more crimes during the weekends and they are in some cases shifted towards evening hours. It comes without surprise that drunkness and driving under influence is more common during late weekend nights. Vandalism and prostitution however have similar hourly distribution, but are just more frequently commited during the weekends.


<embed 
       type="text/html" 
       src="/plots/bokeh_plot.html"
       width="1100"
       height="600"
       >