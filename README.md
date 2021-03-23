# A scraper for https://www.houseofindya.com


## This repository contains scrapy spider that can scrape https://www.houseofindya.com/zyra/necklace-sets/cat for the category Necklace Sets and create .json and .csv files

# Install
```
pip install -r requirements.txt
```

# Running the crawlers/spiders

### Jewelry spider for Necklace Sets category
From the houseofindia directory run the following command:
1. csv :
```
scrapy crawl jewelry -O <filename>.csv
```
2. json:
```
scrapy crawl jewelry -O <filename>.json
```

# Output

###### Necklace Sets CSV File 
![Alt text](Output/Output-image.png?raw=true "Necklace sets csv")
