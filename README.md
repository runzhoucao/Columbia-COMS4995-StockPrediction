# Columbia-COMS4995-StockPrediction
In this project, our goal is to use previous period's (day t-k to day t) news sentiment and stock performance of five companies (AAPL, GOOG, AMZN, FB and MSFT) to predict their next day's (day t+1) stock performance. We first used our LSTM model to replicate a previous study using its data. The paper is [Stock Volatility Prediction Using Recurrent Neural Networks with Sentiment Analysis](https://arxiv.org/abs/1705.02447) by Yifan Liu, Zengchang Qin, Pengyu Li, Tao Wan. Then in our second step, we collected price information and news from 11-11-2012 to 11-11-2017. We used the tools listed in the SentimentAnalysis folder to extract the sentiment information, then run the scripts to obtain the performance of our model.

## Results
![alt text](https://ibb.co/bDYLEm)

## Dependencies
Environment:
- Python 2.7
- Ubuntu 16.04

Packages:
```
sudo apt-get install python-pip python-dev
sudo pip install Scrapy
sudo pip install tensorflow
sudo pip install numpy
sudo apt-get install libatlas-base-dev gfortran
sudo pip install scipy
sudo pip install -U scikit-learn
sudo pip install matplotlib
sudo pip install keras
sudo pip install pandas
```
To run sentiment analysis, a rosette key is required. You may acquire a key from https://www.rosette.com/

## Usage
# To predict with price information only
```python
python stock_pred.py <STOCK_PRICE_FILE> <SHEET_NAME>
```
* <STOCK_PRICE_FILE> is ./us_stock_data/stock_price.xlsx or ./chinese_stock_data/stock_price.xlsx
* <SHHET_NAME> is the stock you are interested in

# To predict with price information and sentiment information
``` python
python stock_pred_with_sent.py <STOCK_PRICE_WITH_SENT_FILE> <SHEET_NAME>
```
* <STOCK_PRICE_WITH_SENT_FILE> is ./us_stock_data/stock_price_with_sentiment.xlsx or ./chinese_stock_data/stock_price_with_sentiment.xlsx
* <SHHET_NAME> is the stock you are interested in

## results/
Contain results obtained on Chinese stocks and on US stocks

## NewsCrawling/
Contain a web crawler that extract url from Reuters.com and sample output

## SentimentAnalysis/
Contain tools for conducting sentiment analysis. Detailed description is included in the folder.

## chinese_stock_data/
Contain raw data of Chinese stocks. Collect from previous research [Stock Volatility Prediction Using Recurrent Neural Networks with Sentiment Analysis](https://arxiv.org/abs/1705.02447) by Yifan Liu, Zengchang Qin, Pengyu Li, Tao Wan.

## us_stock_data/
Contain raw data of US stocks.
