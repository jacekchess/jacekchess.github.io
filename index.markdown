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

## Strategy Consistency

In this section, we will take a closer look at how the number of planted trees evolved. Firstly we will see the developments on the map and later we will inspect what the seasonality looks like. 

<iframe src="/plots/ts_map.html" width="800" height="620"></iframe>

*Figure 2: Distribution of trees planted in Melbourne over the months between December 2004 and December 2021. We can see that trees are often planted in close proximity to parks and streets.*

With spatial analysis, we managed to discover that trees are rarely planted separately. In Figure 2 we observe that during most months between December 2004 and December 2021, new trees form blob structures - creating a new park addition - or lines - as a new boulevard, walk path, or street greenery. To summarize, planting trees in Melbourne happens regularly in an organized manner.


![Text](/plots/ts_line.png)

*Figure 3: Time series of the number of trees planted each month between December 2004 and December 2021. We can see that the number of trees planted has been increasing over the years.*

In the visualization above, we can observe the seasonality in planting trees. The darker red colors mean months from June to August and lighter red from April to the end of October. This means that the majority of trees are planted during Australian winter. Seasonality matches especially after 2013, where the plantings are very regular. Increased regularity may be a result of the Urban Forest Strategy.

## Satellite Views

In order to verify how the tree planting affected the greenery in Melbourne we decided to look at the satellite photos. It is the simplest way to compare two different points in time and see what changed in the city, whether the amount of green spaces in the city increased or decreased.

Satellite images were sourced from Google Earth Engine (later GEE) from Copernicus satellite. The clouds were filtered out with a script in GEE. The images were created by taking the median of pixels from whole years. By doing this we are minimizing the variability in the images which can be caused by weather and time of the year.

![Text](/plots/aerial_images.png)

*Figure 4: Satellite view of Melbourne in the years 2016 and 2021. The images were constructed by using the median of 365 images from each year in order to minimize variability.*

The easiest way to check whether the green spaces increased or decreased is to look at RGB histograms - and in our case at the histograms of green pixels. This however in this case can be misleading. Let's take a look at the image below.

![Text](/plots/green_intensity.png)

*Figure 5: The number of green pixels of a certain intensity. There is a significant difference at the beginning of the area chart where the green pixels are "more intensive" in 2021.*

After closer inspection and plotting the certain intensity of pixels over the map, we concluded that the difference occurred mostly in the water areas - probably in 2021 there was more algae in the sea and river waters near Melbourne. Therefore in the next visualization, we will manually mask out the water reservoirs and make a pixel mask for the vegetation.

![Text](/plots/vegetation.png)

*Figure 6: Satellite image from 2021 (left), vegetation mask for the image from 2021 (middle), and difference in vegetation masks from 2021 and 2016 (right). The vegetation is defined as having a certain intensity of pixels (Big intensity of green and low of red in the pixels). This of course does not capture only trees but all greenery in the city (apart from the water that we masked out).*

We found that the difference in vegetation rose 3.2% from 2016. This means that the citizens of Melbourne can enjoy a city that is more green. There could be of course other reasons for it apart from trees being planted, but it certainly was a part of that. 

## Greenery within districts

Having witnessed the noticeable rise in greenery within the city from above, it's time to delve into the data to understand the underlying trends. Let's transition from our visual observations to a data-driven analysis to explore Melbourne's urban forest landscape further.

One of the targets set out in the Urban Forest Strategy was to increase the canopy cover of the city to 40%. Canopy cover is a measure of the physical coverage of the tree canopy over the land. It represents 
a way of expressing, as a percentage, how much of any given area is shaded by trees. Although we couldn't directly measure this metric, we monitored the number of new trees planted, providing a partial view. While this doesn't capture the entire scenario, as some trees may be removed or reach the end of their lifespan, it does offer insights into the city's progress toward its target. Notably, areas with the lowest canopy cover include Parkville (19.4%), Southbank (14.2%), and Docklands (6.4%).

<iframe src="/plots/district_interactive_map.html" width="850" height="650"></iframe>

*Figure 7: The choropleth map displays the cumulative count of trees planted in different districts of Melbourne over the period spanning from 2012 to 2021. Each district is shaded with a color gradient, representing the number of planted trees, with darker shades indicating higher counts. Hovering over the polygons, we can see the exact number of the trees as well as district name and area.*


Analyzing the map, it becomes evident that a substantial surge in tree planting occurred shortly after the initiation of the Urban Forest Strategy in 2013, notably in Parkville, where tree numbers soared to over 5000.

Over the years leading up to 2021, Southbank witnessed a remarkable growth from 68 to over 700 trees, while Docklands experienced an even more pronounced increase, from 400 to over 2900 trees. These numbers underscore the effective implementation of the strategy, particularly in areas with lower canopy cover.

Across most districts, a consistent annual planting of 50 to 1000 trees was observed. However, fewer trees were planted in inner districts like the CBD and West Melbourne, possibly due to their smaller area and dense urban infrastructure.