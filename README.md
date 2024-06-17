# Indian Earthquake Visualizer

## [Demo](https://earthquake-visualizer-india.netlify.app/#4/10.27/78.35)

This map consists of major earthquakes reported in India from 1905 to 2023. The data was obtained from NCEI (NOAA National Centers for Environmental Information) website. The data is cleaned up and fixed issues with certain data from alternative sources (cited in the references). The location data is clustered using K- Means Clustering for finding the most frequent locations of earthquakes in India. For that we took 100 KM radius and clustered the number of points came under that circular region. It is found to be the most frequent earthquakes happened in Maharashtra (100 Kms around Satara region). The map points are colour coded according to the strength of quake (Richter Scale Classification) and two filters are provided for Frequency wise and Richter Classification wise.

The map was generated using QGIS (version 3.22.16-Białowieża).


References:
===========

- National Geophysical Data Center / World Data Service (NGDC/WDS): NCEI/WDS Global Significant Earthquake Database. NOAA National Centers for Environmental Information. doi:10.7289/V5TD9V7K
- Singh, Shri Krishna & Suresh, G. & Dattatrayam, R. & Shukla, H. & Martin, Stacey & Havskov, J. & Pérez-Campos, Xyoli & Iglesias, Arturo. (2013). 1960 Delhi earthquake: Epicentre, depth and magnitude. Current science. 105. 1155-1165.
- Agwul, Abong. (2014). Earthquake distribution in India from 1961 to 2010.
- ChatGPT for generating necessary python codes.

