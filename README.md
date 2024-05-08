# Reddit Data Scraper
## Overview
A Python script that allows you to scrape data from Reddit, process it, and save it as a CSV file. It utilizes the httpx library for making HTTP requests and pandas for handling data.

## Prerequisites
Before using this script, make sure you have the following:

- Python 3.x installed on your system
- Necessary Python packages installed (httpx, pandas, etc.). You can install them using pip:
```
pip install httpx pandas
```

### Usage
1. Clone the repository or download the script
2. Open the script in a text editor and provide the required inputs:
3. baseURL: Base URL of the Reddit API.
4. endpoint: Endpoint of the API you want to access (e.g., r/{subreddit}/, user/{username}/, etc.).
4. category: Category or filter for the data (e.g., hot, new, top, etc.).
```
python redditAPI.py
```
- The script will fetch data from Reddit based on your inputs, process it, and save it as a CSV file named results.csv in the same directory.
- Change the number of requests or other parameters in the loop to suit your data fetching needs.
- Modify the data processing logic to extract specific fields or perform additional operations on the data.
