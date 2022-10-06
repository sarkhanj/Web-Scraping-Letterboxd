# Web-Scraping-Letterboxd
A Scrapy app which produces a JSON file of your Letterboxd diary with all the information about the films.

To download Scrapy, you should do PIP INSTALL SCRAPY.
Then, cd to your directory where the project is located, do "scrapy crawl movie -O your_file_name_here.json".
Enter a Letterboxd username that you want to get their diary info.
Enjoy the json file!

## UPDATE:
Posters arent available anymore on Letterboxd when you disable Javascript. For that reason, the poster data will be null in the scraped data :(. If anyone knows how I can deal with this situation and get poster links back, I would appreciate your help!
A possible solution is to fetch the posters from another API, for example: https://www.themoviedb.org/documentation/api

