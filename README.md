# A Look Into Tennis Talent
Following the electric men's finals in Cincy 2023, I've read a lot of speculation regarding the future of tennis, as well as general discussions with comparisons between past and present - namely surrounding Djokovic and Alcaraz.

I like seeing things and comparisons visually - so I wrote a few scripts in Python over a few hours to scrape data regarding top players of both past and present in regards to their W/L% each year, GS finals appearances, and GS wins.

As of the time I am posting this readme, none of the scripts / data / or in general the repo itself has been packaged or modularized as well as I would like. This is probably something I will work on more in the future and expand upon, since there are some other numbers / figures I'm interested in (i.e total titles, total wins / wins by year, end of year points, etc.) - really the sky is the limit here!

Between two jobs / classes / helping "tutor" / managing my own personal projects or small freelance work, I don't have tons of time on my hand.

## Credits
Usually the standard is to put credits towards the end - but since at the end of the day a project like this is something I can only do with data provided by others (whether it be via webscraping, raw data, or an API), I feel it is a necessity to provide credit first where credit is due. All of the data that is graphed and used in this repo comes from the following:

* **[Tennis Abstract](https://www.tennisabstract.com/)**
* **[Raw Data from Tennis Abstract](https://github.com/JeffSackmann/tennis_atp)** - *Courtesy of **[JeffSackmann](https://github.com/JeffSackmann)***
 
## Included files / folders:
+ *main.py* => handles all of the logic for scraping various player pages / data on tennisabstract, super messy and will probably get around to cleaning this soon
    > __Note__ third-party packages used: BeautifulSoup, requests-html
+ *sort_and_plot.py* => handles the raw data provided from main.py for each player, then handles plotting the data accordingly
    > __Note__ third-party packages used: matplotlib
+ *rawData.json* => raw data provided by main.py, contains an array of players (objects) containing name, w/l% each year on tour, and grand slam data each year on tour
+ graphs => folder containing all of the graphs i plotted using sort_and_plot.py
