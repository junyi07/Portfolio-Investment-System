from numpy import *
from pandas import *
from sklearn.metrics import accuracy_score,roc_curve, auc,roc_auc_score
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.pyplot
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_gaussian_quantiles

from itertools import cycle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp
import csv
import time

def loadDataSet(fileName):  
    # body = read_file(fileName)
    # myData = read_csv(StringIO(body))
    # myData.drop('Unnamed: 0', axis=1, inplace=True)
    myData = read_csv(fileName)
    train = myData.iloc[0:5780, :]
    test = myData.iloc[5780:, :]
    # print(test.isnull().any())
    train_data=[]
    test_data=[]
    train_lable=[]
    test_lable=[]
    name = []
    date = []
    for i in range(0, len(train)):
        train_data.append(list(train.iloc[i, 0:50]))
        train_lable.append(train.iloc[i, 51])
    for i in range(0, len(test)):
        test_data.append(list(test.iloc[i, 0:50]))
        test_lable.append(test.iloc[i, 51])
        name.append(test.iloc[i, 50])
        date.append(test.iloc[i, 52])
    # print(test_data[0])
    return train_data,train_lable,test_data,test_lable,name,date


def test():

# ---------------------------------------validation---------------------------------------------------------------------------
    train_data,train_lable,test_data,test_lable,test_name,test_date=loadDataSet("final.csv")
    data_train, data_valid, label_train, label_valid =train_test_split(train_data,train_lable,test_size=0.1)
    # print(data_valid)
    A=DecisionTreeClassifier(max_depth=3, min_samples_split=2, min_samples_leaf=1)
    A.fit(train_data, train_lable)
    bdt = AdaBoostClassifier(A,algorithm="SAMME",n_estimators=100, learning_rate=0.8)
    bdt.fit(train_data, train_lable)
    valid = bdt.predict(data_valid)

    M = bdt.predict_proba(data_valid)# for validation ROC
    N = [[max(temp)] for temp in M]

    
    # print(label_valid)
    predict_validation_label=mat([[i] for i in valid])
    errArr=mat(ones((len(predict_validation_label),1)))
    valid_error=errArr[predict_validation_label!=mat(label_valid).T].sum()/len(predict_validation_label)
    # valid_error=accuracy_score(label_valid,predict_validation_label)
    # print(predict_validation_label)
    valid_auc = metrics.roc_auc_score(label_valid,predict_validation_label)#验证集上的auc值    
    print("valid_error",1-valid_error)  
    print("valid_AUC",valid_auc)
    # print("valid_Score:", bdt.score(datArr, labelArr))
# ---------------------------------------test-----------------------------------------------------------------------------------
    Z= bdt.predict(test_data)

    X = bdt.predict_proba(test_data)# for test ROC
    Y=[[min(temp)] for temp in X]

    print(A.feature_importances_)
    predict_label=[[Z[i]] for i in range(len(Z))]
    # print(predict_label)
    predict_label=mat(predict_label)
    errArr=mat(ones((len(test_lable),1)))
    test_error=errArr[predict_label!=mat(test_lable).T].sum()/len(test_lable)
    test_auc = metrics.roc_auc_score(test_lable,predict_label)#验证集上的auc值
    # length=int(len(test_lable)/8)
    # per_auc=[]
    # for i in range(8):
    #     temp_test = [test_lable[j+i*length] for j in range(length)]
    #     temp_predict = [Z[j+i*length] for j in range(length)]
    #     temp_predict=mat([[i] for i in temp_predict])
    #     per_auc.append(metrics.roc_auc_score(temp_test,mat(temp_predict)))
    # print(per_auc)
    print("error",test_error)  
    print("AUC",test_auc)
    print("Score:", bdt.score(train_data, train_lable))
# ---------------------------------------label-----------------------------------------------------------------------------------
    a=[[test_date[i],test_name[i],Z[i]] for i in range(len(Z))]
    code_lable=[x for x in a if x[2]==1]
   
# ---------------------------------------CSV-----------------------------------------------------------------------------------
    csvfile = open("predict_adaboost.csv","w", newline='')
    writer = csv.writer(csvfile)
    writer.writerow(["date","code","label"])
    for i in range(len(code_lable)):
        writer.writerow(code_lable[i])
    csvfile.close
# ---------------------------------------ROC-----------------------------------------------------------------------------------
    valid_false_rate, valid_true_rate, thresholds = roc_curve(label_valid, N)  
    valid_roc_auc = auc(valid_false_rate, valid_true_rate)  
    plt.plot(valid_true_rate, valid_false_rate, 'green',  label='Vliadation_AUC = %0.2f'% valid_roc_auc)  
    

    false_positive_rate, true_positive_rate, thresholds = roc_curve(test_lable, Y)  
    csvfile = open("ROC_ada.csv","w", newline='')
    writer = csv.writer(csvfile)
    writer.writerow(["X","Y"])
    temp=[[false_positive_rate[i],true_positive_rate[i]] for i in range(len(false_positive_rate))]
    for i in range(len(false_positive_rate)):
        writer.writerow(temp[i])
        # writer.writerow(true_positive_rate[i])
    csvfile.close



    roc_auc = auc(false_positive_rate, true_positive_rate)  
    plt.title('ROC for adaboost')  
    plt.plot(false_positive_rate, true_positive_rate, 'r',  label='Test_AUC = %0.2f'% roc_auc)  
    plt.legend(loc='lower right')  
    plt.plot([0,1],[0,1],'b--')  
    plt.xlim([0,1.2])  
    plt.ylim([0,1.2])  
    plt.ylabel('True Positive Rate')  
    plt.xlabel('False Positive Rate')  
    plt.show()  






if __name__=='__main__':
    start = time.time()
    test()
    end = time.time()
    print(str(end))
    


