from __future__ import division
import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import numpy as np
import pylab as pl
import csv
#------------------------------membership function------------------------------
def membership(a,num,Len):    
    Ai=[]#   Ai[i]=mid(last interval), upper bound, lower bound, mid(next bound))
    temp=[]
    mid_temp=[]
    A_temp=[]

    for i in range(num+1):
        temp.append(a+Len*i)

    for i in range(num):
        mid_temp.append((temp[i]+temp[i+1])/2)

    Ai.append([temp[0]-0.5*Len,temp[0],temp[1],mid_temp[1]])
    for i in range(num-2):
        Ai.append([mid_temp[i],temp[i+1],temp[i+2],mid_temp[i+2]])
    Ai.append([mid_temp[num-2],temp[num-1],temp[num],temp[num]+0.5*Len])
    # print(len(Ai))
    return Ai

#------------------------------jump weight si------------------------------
def weight_si(A,count_prices):    
    number3=-1
    y_r=[]
    J=[]
    S=[]
    r=[]
    count_r=0
    Num=-1
    count_i=-10
    flag=0
    count_Si=0
    Si=[]   
    
    for i in range(count_prices-1):
        r.append(A[i+1]-A[i])
    # print(r)
    # print(count_prices)
    # print(len(A))
    while number3<len(r)-1:
        count_r=0
        number3+=1  
        if r[number3] in y_r:
            continue
        else:
            Num+=1
            y_r.append(r[number3])
            J.append(r[number3])
            S.append(J)
            J=[]
            for i in range(len(r)):
                if r[number3]==r[i]:
                    count_r+=i+1
            S[Num].append(count_r)

    temp_hhh=[]
    for s in S:
        temp_hhh.append(s[0])
    temp_hhh.sort()
    for i in range(len(temp_hhh)):
        for j in range(len(S)):
            if temp_hhh[i]==S[j][0]:
                Si.append(S[j])
    # print(Si)
    # print(len(Si))
    for i in range(len(Si)):
        count_Si+=Si[i][1]

    for i in range(len(Si)):    
            Si[i].append(Si[i][1]/count_Si)
    # print(Si)
    # weight Si=[s'-m+1,....s'-1,s'0,....s'm-1]
    return Si

#------------------------------time weight wi------------------------------
def weight_wi(A):    
    A_i=[]#middle assist
    wi=[]#  wi[0]=Ai->Aj        wi[1]=frequency        wi[2]=time series   wi[3]=time weight
    y=[]#middle assist
    y_time=[]
    L=[]#middle assist
    r=[]#the difference of the A_i jump
    wi=[]#wi weight
    s={}#jump weight 
    number=-1
    number1=-1
    Num1=-1
    num_x=-1
    count_weight=0
    count_time=0

    # print(A)
    for i in range(len(A)-1):
        if i==0:
            A_i.append([31,31,31])
        elif i>0:
            A_i.append(A[i-1:i+2])
    # for i in range(len(A)-1):
    #     if 36 == A_i[i][0]:
            # print(A_i[i][1])
    # print(A_i)

    while number<len(A_i)-1:
        count=0
        number+=1  
        if A_i[number] in y:
            continue
        else:
            Num1+=1
            y.append(A_i[number])
            L.append(A_i[number])
            wi.append(L)
            L=[]
            for i in range(len(A_i)):
                if A_i[number]==A_i[i]:
                    count+=i+1                           #时间权重
            wi[Num1].append(count)
    # print(wi)

    for i in range(len(wi)):
        count_weight+=wi[i][1]

    for i in range(len(wi)):
        wi[i].append(wi[i][1]/count_weight)
    # print(wi)

    return wi

def Forcast_new(Ai,si,wi,v,cur_price,before1_price,r,best_num):
    group=[]
    group_si=[]
    Aic=np.array([0.0,0.0,0.0,0.0])
    Ais=np.array([0.0,0.0,0.0,0.0])
    temp_wi=[]
    temp_Ai=[]
    temp_Ai_si=[]
    count_wi=0
    flag=0
    # print(si)
    # for i in range(num):
    #    if cur_price<v[i][0][1] and cur_price>=v[i][0][0]: 
    #        cur_i=i+1
    #     #    print(cur_i)
    #        break)
    before1_i=np.digitize(before1_price, v)
    cur_i=np.digitize(cur_price, v)
    # print(cur_price)
    # print(wi)
    for i in range(len(wi)):
        if cur_i==wi[i][0][1]:
            flag=1
    delta=[(abs(before1_i-wi[i][0][0])+abs(cur_i-wi[i][0][1])) for i in range(len(wi))]
    # print(len(delta))
    for i in range(best_num):
        group.append(wi[delta.index(min(delta))][0][2])
        delta[delta.index(min(delta))]=100
        temp_wi.append(wi[delta.index(min(delta))][2])
    # print(group)
    # print(wi)
    # print(cur_i)
    for i in range(len(group)):
        count_wi+=temp_wi[i]
        
    for i in range(len(group)):
        temp_wi[i]=temp_wi[i]/count_wi           
    # print(group)
    # print(temp_wi)
    # print(Ai)
    for i in range(len(group)):
        temp_Ai.append(Ai[group[i]])

    for i in range(len(group)):
        cur=np.array(temp_Ai[i])
        temp_Ai[i]=cur*temp_wi[i]

    for i in range(len(group)):
        Aic+=np.array(temp_Ai[i]) 
    
    for i in range(len(si)):
        group_si.append(cur_i+si[i][0])
    

    for i in range(len(si)):
        temp_Ai_si.append(Ai[group_si[i]-1])

    for i in range(len(si)):
        cur=np.array(temp_Ai_si[i])
        temp_Ai_si[i]=cur*si[i][2]
        
    for i in range(len(si)):
        Ais+=np.array(temp_Ai_si[i])

    # print(wi)
    # print(si)
    forcast_array=r*Ais+(1-r)*Aic
    forcast_new=(forcast_array[0]+forcast_array[3])/2

    # A_S.append((Ais[0]+Ais[3])/2)
    # A_C.append((Aic[0]+Aic[3])/2)
    return forcast_new



#———————————————————————————————————————function: one day forecast based last observed data——————————————————————————————————

if __name__ == '__main__':
    NUM=0
    rolling_count=0
    forcast_list1=[]
    forcast_list2=[]
    forcast_list3=[]
    forcast_list4=[]
    forcast_list5=[]
    forcast_list6=[]
    forcast_list7=[]
    forcast_list8=[]
    rmse=0
    A_S=[]
    A_C=[]
#------------------------------------------------------------IMF1----------------------------------------------------------
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        # print(len(pd.read_csv(cayering_sale)))
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF1"]
        train_data_prices=train_data["IMF1"]
        test_data_prices=test_data["IMF1"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=9
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.008,6)
        forcast_list1.append(forcast_new)
    # fl=open('list_DJI_IMF1.txt', 'w')
    # for i in forcast_list1:
    #     fl.write(str(i))
    #     fl.write("\n")        
    print("IMF1 is over!")
#------------------------------------------------------------IMF2----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF2"]
        train_data_prices=train_data["IMF2"]
        test_data_prices=test_data["IMF2"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=2
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.019,4)
        forcast_list2.append(forcast_new)
    # fl=open('list_DJI_IMF2.txt', 'w')
    # for i in forcast_list2:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF2 is over!")

#------------------------------------------------------------IMF3----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF3"]
        train_data_prices=train_data["IMF3"]
        test_data_prices=test_data["IMF3"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=2
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.127,2)
        forcast_list3.append(forcast_new)
        rmse=rmse+(test_data_prices[480+NUM]-forcast_new)*(test_data_prices[480+NUM]-forcast_new)
    # fl=open('list_DJI_IMF3.txt', 'w')
    # for i in forcast_list3:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF3 is over!")

#------------------------------------------------------------IMF4----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF4"]
        train_data_prices=train_data["IMF4"]
        test_data_prices=test_data["IMF4"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=7
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.231,1)
        forcast_list4.append(forcast_new)
    # fl=open('list_DJI_IMF4.txt', 'w')
    # for i in forcast_list4:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF4 is over!")


#------------------------------------------------------------IMF5----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF5"]
        train_data_prices=train_data["IMF5"]
        test_data_prices=test_data["IMF5"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=1
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))
 
        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.471,1)
        forcast_list5.append(forcast_new)
    # fl=open('list_DJI_IMF5.txt', 'w')
    # for i in forcast_list5:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF5 is over!")

#------------------------------------------------------------IMF6----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF6"]
        train_data_prices=train_data["IMF6"]
        test_data_prices=test_data["IMF6"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=10
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.995117,3)
        forcast_list6.append(forcast_new)
    # fl=open('list_DJI_IMF6.txt', 'w')
    # for i in forcast_list6:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF6 is over!")


#------------------------------------------------------------IMF7----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF7"]
        train_data_prices=train_data["IMF7"]
        test_data_prices=test_data["IMF7"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=6
        a=-1000
        b=1000
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.9971,5)
        forcast_list7.append(forcast_new)
    # fl=open('list_DJI_IMF7.txt', 'w')
    # for i in forcast_list7:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF7 is over!")


#------------------------------------------------------------IMF8----------------------------------------------------------
    NUM=0
    rolling_count=0
    for i in range(246):
        cayering_sale='EMD_300(2012-2015).csv'
        train_data = pd.read_csv(cayering_sale)[0:480+rolling_count]
        test_data = pd.read_csv(cayering_sale)[480:len(pd.read_csv(cayering_sale))]
        test_before1_data_price = pd.read_csv(cayering_sale)[479:len(pd.read_csv(cayering_sale))-1]["IMF8"]
        train_data_prices=train_data["IMF8"]
        test_data_prices=test_data["IMF8"]
        count_prices=0
        for price in train_data_prices:
            count_prices+=1
        sd=np.std(train_data_prices,ddof=1)
        Len=1
        a=2000
        b=4200
        num=int((b-a)/Len)
        rolling_count+=1
            

        cur_price=test_data_prices[480+NUM]
        NUM+=1
        next_price=test_data_prices[480+NUM]
        v = np.arange(a, b, Len)
        # print(v)
        # start_time=time.time()
        A=list(np.digitize(train_data_prices, v))

        # print("1---%s seconds ---"%(time.time()-start_time))
        #call function
        Ai=membership(a,num,Len)
        # print(Ai)
        si=weight_si(A,count_prices)
        wi=weight_wi(A)
        forcast_new=Forcast_new(Ai,si,wi,v,cur_price,test_before1_data_price[478+NUM],0.999,3)
        forcast_list8.append(forcast_new)
    # fl=open('list_DJI_IMF8.txt', 'w')
    # for i in forcast_list8:
    #     fl.write(str(i))
    #     fl.write("\n")   
    print("IMF8 is over!")


    cayering_sale='hushen300.csv'
    temp_actual_price = pd.read_csv(cayering_sale)[481:727]
    actual_price=temp_actual_price["close"]
    forcast_list=[]
    rmse=0
    for i in range(246):
        forcast_price=forcast_list1[i]+forcast_list2[i]+forcast_list3[i]+forcast_list4[i]+forcast_list5[i]+forcast_list6[i]+forcast_list7[i]+forcast_list8[i]
        forcast_list.append(forcast_price)
        rmse=rmse+(actual_price[481+i]-forcast_price)*(actual_price[481+i]-forcast_price)

    csvfile = open("2014_hushen300.csv","w", newline='')
    writer = csv.writer(csvfile)
    writer.writerow(["date","price"])
    for i in range(len(forcast_list)):
        writer.writerow([temp_actual_price["date"][481+i],forcast_list[i]])
    csvfile.close


    RMSE=np.sqrt(rmse/246)
    print("the final RMSE:",RMSE)


    x=[]
    for i in range(246):
        x.append(i+1)
    
    plot1=pl.plot(x, forcast_list,color='green',label='forcasting',linewidth=1.0)
    plot2=pl.plot(x, actual_price,label='data testing',color='blue',linestyle='--')
    # plot3=pl.plot(x, train_open,color='red',label='High',linewidth=1.0)
    # plot3=pl.plot(x, A_S,color='gray',label='Ais',linewidth=1.0)
    pl.title('hushen300')
    pl.xlabel('Trading days(from January 2014 to December 20201417.)')# make axis labels
    pl.ylabel('Quotation')
    pl.legend(loc = 'best')
    plt.xticks((0,41,83,128,184,246),('Jan.','Mar.','May.','Jul.','Sep.','Nov.'),rotation=0)
    pl.show()