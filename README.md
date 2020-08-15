# Portfolio Investment System
An intelligent portfolio investment system for Chinese stock based on machine learning and fuzzy time series.

# Indroduction
This project is an intelligent portfolio investment system for Chinese stock. Firstly, we utilized the classification score of Random Forest to select efficient stock factors, and trained and forecasted the portfolio investment based on machine learning models (Adaboost, Random Forest and SVM). Then ran our portfolio strategies on JoinQuant platform. Eventually we got a simulation return average 44% higher than the benchmark.

It's worth mentioning that I designed an efficient stop-loss strategy by forecasting stock index based on Intelligent Hybrid Weighted Fuzzy (IHWF) time series model proposed in [my published paper](https://link.springer.com/chapter/10.1007/978-3-319-95786-9_8).



# Dependencies
```
pandas = 0.21.0
numpy = 1.13.3
EMD-signal = 0.2.4
scikit-learn = 0.19.1
matplotlib = 2.1.1
pylint = 2.3.1
```
# Details
## Final Result
Implemented a simulation trade on JoinQuant platform from Janurary 2015 to December 2015 and got a simulation return average 44% higher than the benchmark.

![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/Result.png)

## Stop-loss strategy
Developed a stop-loss strategy by forecasting stock index based on IHWF(Intelligent Hybrid
Weighted Fuzzy) proposed in my published paper.

![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/stopLoss.png)

## ROC and AUC
ROC and AUC of Different Portfolios
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/ROC.png)

## Forecast for Chinese Stock
Forecast Chinese stock from Janurary 2015 to December 2015 based on IHWF model proposed in my published paper.
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/Forecast.png)

## Select stock factors by Random Forest
Select 50 stock factors that the importance scores more than 0.01 based on Radnom Forest.
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/FactSelect.png)


