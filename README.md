# Portfolio Investment System
An intelligent portfolio investment system for Chinese stock based on machine learning and fuzzy time series.

# Indroduction
This project is an intelligent portfolio investment system for Chinese stock. Make use of Random Forest to select efficient stock factors, find the portfolio investment combined with machine learning (Adaboost, Random Forest and SVM), and get a simulation trade on JoinQuant platform with the stop-loss strategy based on fuzzy time series model.


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
implemented a simulation trade on JoinQuant platform from Janurary 2015 to December 2015 and got a simulation return average 44% higher than the benchmark.

![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/Result.png)

## Stop-loss strategy
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/stopLoss.png)

## ROC and AUC
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/ROC.png)

## Forecast for Chinese Stock
forecast Chinese stock from Janurary 2015 to December 2015 based on IHWF model proposed in my published paper.
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/Forecast.png)

## Select factors by Random Forest
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/FactSelect.png)

## EMD original signal
![image](https://github.com/Junyihe1107/Portfolio-Investment-System/blob/master/image/EMD.png)
