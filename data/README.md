# INVEST ML

Machine learning project that predict the value of given stock for the next day.

## Data Preparation
All data already downloaded from Yahoo API (only Indonesian stock market) and separated into 3 folder

Folder Name | Data Range
--- | ---
1Y | (2016/02/01 - 2017/02/01)
3Y | (2016/02/01 - 2017/02/01)
ALL_TIME | (Start - 2017/02/01)

You also can download your own dataset from any range using `scrapper.py`

## Data Wrangling
Because the downloaded datas from the Yahoo API are still raw data. We need to wrangling it using `wranglers.py` and save it in folder generated. 
