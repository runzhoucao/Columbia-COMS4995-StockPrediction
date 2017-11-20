# Columbia-COMS4995-StockPrediction

## stock_pred.py
This code works for the condition where **only stock information** is available.

## stock_pred_sent.py
This code works for the condition where **both stock information and sentiment information** are available.

## stock_pred_sent_new_norm.py
This code is exactly the same as stock_pred_sent.py, except it adds in z-score normalization for sentiment information.

## stock_pred_ipython_version.ipynb
This is simply an ipython version code with better visualization.

## stock_price.xlsx
This file contains the stock price of 6 chinese stocks.

## stock_with_sentiment.xlsx
This file contains the stock price **and** sentiment information of 6 chinese stocks.

The data in stock_price.xlsx and stock_with_sentiment.xlsx comes from  
[Stock Volatility Prediction Using Recurrent Neural Networks with Sentiment Analysis](https://arxiv.org/abs/1705.02447) by Yifan Liu, Zengchang Qin, Pengyu Li, Tao Wan

## raw output folders
* result_10_holdout: generated with stock_pred.py and stock_pred_sent.py with 10% data as testdata
* result_20_holdout: generated with stock_pred.py and stock_pred_sent.py with 20% data as testdata
* result_10_holdout_new_norm: generated with stock_pred.py and stock_pred_sent_new_norm.py with 10% data as testdata
* result_20_holdout: generated with stock_pred.py and stock_pred_sent_new_norm.py with 20% data as testdata

## result.xlsx
This file contains the accuracy of our model under different circumstances.
