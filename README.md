# scrapping-experiments

The primary goal of this project was to determine the best method
for scraping amazon for their price of a new razorblade laptop
The two of the methods used were selenium and requests

# Side Notes
When scrapping the internet for information, understanding who and 
what you are scrapping from. Many sites, such as facebook and 
other large corporation, have rules for using automated scripts. 
Check their robots.txt files and or terms of service before 
engaging in website scrapping. 

Chromedriver: you need to get the right chromedriver for your 
system. The one in the repository is specfic to my environment,
a raspberry pi.

# Code 
There are two files, each using a different library. Simply run 
them with "python {file}". The selScraper.py will create a file 
with the time and price point.

# Results

Results cannot be fully given at this time. There are pros and
cons for each of the methods. For speed and efficiency, requests
is faster whereas selenium is better for beginners 
and avoiding bot walls.

Pros for requests library
- Interacts well with APIs
- Fast

Pros for Selenium
- Easy, good for beginners
- easier to avoid bot walls/ captchas
- has built in element finders

This experiment did not come out as I planned it to be however,
it did spark my interest in how these websites worked to detect
bot-like activity. 

"To Be Continued..." 

