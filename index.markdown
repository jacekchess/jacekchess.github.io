---
layout: home
---

**The City of Melbourne launched an Urban Forest Strategy in August 2012. They aim to reduce the temperature in the city by planting forty-two thousand new trees by 2032. We are checking their progress almost half way through their journey.**

Due to climate change, we observe higher temperatures every year all around the world. It is a serious threat to big cities, where apart from global warming, we observe the Urban Heat Island effect. The City of Melbourne decided to make their move before it was too late and launched the Urban Forest Strategy in August 2012. One of the goals proposed in the strategy is to create a resilient, healthy, and diverse forest that will provide shade and cooling.

To date is May 2024, over 10 years after the campaign's beginning, and almost 10 years before the campaign’s end. The last decade was full of turbulences, Covid-19 being one of the most significant ones. Our research aims to discover, how well the City of Melbourne managed to stick to their plan regarding the Urban Forest Strategy. The results may be helpful to evaluate the progress of the campaign, as well as provide guidance for the cities that would like to follow Melbourne’s path.

## Forest Diversity

One of the main threats to the urban forest that the City of Melbourne recognized is tree diseases like Dutch Elm, Myrtle Rust, or plane tree canker stain. All of them are more serious, for the forests that are dominated by one species. In the strategy from August 2012, forest diversification has a separate target, which aims to compose the urban forest of **no more than 5% of one tree species, no more than 10% of one genus, and no more than 20% of any one family**. The task is challenging, as the new trees must also have the resilience to tolerate hotter, drier conditions, and potentially also cope with major storm events. In Figure 1 we check, how well the City of Melbourne manages to progress towards diversified urban forest.

![Text](/plots/diversity.png)

*Figure 1: Fraction of tree species (top), genera (middle), and families (bottom) compared for the 2005-2021 period. The vertical lines show when the Urban Forest campaign started, and the green areas are the strategy target for 2032 - all species, genera, and families should be inside this area by that time. We can observe constant progress in all three categories since the campaign started.*

We can easily observe, that there is one dominating family/genre/species of trees, which is the Myrtaceae family with Eucalyptuses. However, the Eucalyptus dominance has been decreasing since the start of the campaign. The City of Melbourne has planted many Acacias and Bursarias for the last decade, which resulted in more diverse green live. The campaign's progress can impress with its consistency and if the council will be able to keep up the speed of planting new, non-eucalyptus trees, they should achieve their goal by 2032. However, they will need to find another tree genre then Acacia, as there are already too many of them compared to less popular genres.



## Time series 

In this section we will take a closer look at how did the number of planted trees evolved. Firstly we will see the developments on the map and later we will inspect how does the seasonality look. 

<embed 
       type="text/html" 
       src="/plots/trees_over_the_months_map.html"
       width="750"
       height="600"
>

*Figure X: In the visualization above we can see the distribution of trees planted in Melbourne over the months. The map is interactive, so you can click on the play button to see how the tree planting evolved over time. The time series plot below the map shows the number of trees planted each month. We can see that the number of trees planted has been increasing over the years. Additionally we can see that trees are quite often planted in close areas/parks/streets which is something we can expect in real life*


![Text](/plots/ts_line.png)

*Figure X: In the visualization above, we can view the seasonality in the trees being planted. The darker red colors mean months from June to August, and lighter red from April to end of October. This means that the most trees are planted during australian winter. Seasonality matches especially after 2013, where the plantings are very regular.*

## Satelite Views

In order to verify how the tree planting affected the greenery in Melbourne we decided to look at the satelite photos. It is the most simple way to compare two different points in time, see what changed in the city, whether the amount of green spaces in the city increased or decreased.

Satelite images were sourced from Google Earth Engine (later GEE) from Copernicus satelite. The clouds were filtered out with a script in GEE. The images were created  by taking the median of pixels from whole years. By doing this we are minimizing the variablity in the images which can be caused by weather and time of the year.

![Text](/plots/aerial_images.png)
 
*Figure X: Satelite view of Melbourne in the  years 2016 and 2021. The images were constructed by using median of 365 images from each year in order to minimize variability*

The easiest way to check whether the green spaces increased or decreased is to loog at RGB histograms - and in our case in the histograms of green pixels. This hovewer in this case can be misleading. Let's take a look at the image below.

![Text](/plots/green_intensity.png)

*Figure X: Image above shows the number of green pixels of certain intensity. There is significant difference at the start of area chart where the green pixels are "more intensive" in 2021*

After closer inspection and plotting the certain intensity of pixels over the map we concluded that the difference occured mostly in the water areas - probably in 2021 there is more algee in the sea and river waters near Melbourne. Therefore in the next visualization we will manually mask out the water reservoirs and make a pixel mask for the vegetation.

![Text](/plots/vegetation.png)

*Figure X: In the image above we have shown the added vegetation in the span of 5 years. The vegetation is defined as having a certain intensity of pixels (Big intensity of green and low of red in the pixels). This of course does not capture only trees but all greenery in the city (apart from water that we masked out).*

We found that the difference in vegetation rose 3.2% from 2016. This means that the citizens of Melbourne can enjoy a city that is more green. There could be of course other reasons for it apart from trees being planted, but it certainly was a part of that. 