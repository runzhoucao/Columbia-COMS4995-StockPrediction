# Columbia-COMS4995-StockPrediction
In this project, our goal is to use previous period's (day t-k to day t) news sentiment and stock performance of five companies (AAPL, GOOG, AMZN, FB and MSFT) to predict their next day's (day t+1) stock performance. To get confidence in our model, we first replicate the work done Y Liu et al. but we use a LSTM model. The data is from [Stock Volatility Prediction Using Recurrent Neural Networks with Sentiment Analysis](https://arxiv.org/abs/1705.02447) by Yifan Liu, Zengchang Qin, Pengyu Li, Tao Wan. The script and preliminary result is in the folder Preliminary work. Then in our second step, we do sentiment analysis on news from 11-11-2012 to 11-11-2017. The news collection scripts and stock data scripts are in the folder data_collection. Finally we fuse the sentiment analysis result and stock data into our LSTM model, the scripts and results are in the folder stock_prediction

## Dependencies
Environment:
Python 2.7
Ubuntu 16.04

Packages:
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

To run sentiment analysis, a rosette key is required. You may acquire the key from https://www.rosette.com/

## result.xlsx
This file contains the accuracy of our model under different circumstances.

## NewsCrawling/scraper.py
This is a simple web crawler that extract url from Reuters.com

## NewsCrawling/file
This is the result of date:url pairs of Apple news

## SentimentAnalysis/bullishness.py
This is the script that extract entity-label along with its confidence and document-label with its associated confidence

## SentimentAnalysis/bullishness_in_order.py
This script rearranges the bullishness result in an increasing order of date
