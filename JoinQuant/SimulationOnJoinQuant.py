# 导入函数库
import jqdata
from six import StringIO

# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    log.info('开始赚钱')
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    

# def after_trading_end(context):   
    # cash = context.portfolio.cash  # 取得当前的现金量，命名为cash
    # body = read_file("hushen(2014-2015).csv")
    # hushen = pd.read_csv(StringIO(body))

    # # date = str(context.current_dt)[0:10]
    # date = context.current_dt.strftime("%Y/%m/%d")
    # a,b,c=date.split('/')
    # current_date=a+'/'+b+'/'+c
    # log.info(current_date)
    # for i in range(len(hushen)-1):
    #     if current_date==(hushen.loc[:, '﻿date']).iloc[i]:
    #         if hushen["price"][i+1]-hushen["price"][i+1]<-100:
    #             for i in g.security:
    #                 order_target(i, 0) 
    #         elif hushen["price"][i+1]-hushen["price"][i+1]>100:
    #             for i in g.security:
    #                     order_value(i, 50000) 
    
    
    
def handle_data(context,data):
    cash = context.portfolio.cash  # 取得当前的现金量，命名为cash
    # 读出当前应买股票
    body = read_file("predict_linear.csv")
    df = pd.read_csv(StringIO(body))
    code = []
    date = str(context.current_dt)[0:10]
    log.info(date)
    if date == '2014-01-02':
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2014/3/31':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2014-04-01':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2014/6/30':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2014-07-01':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2014/9/30':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
            g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2014-10-09':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2014/12/31':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2015-01-05':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2015/3/31':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2015-04-01':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2015/6/30':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2015-07-01':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2015/9/30':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    elif date == '2015-10-09':
        for i in code:
            order_target(i, 0) # 将每只上季度股票仓位调整到0，即全卖出
        code = []
        for i in range(0, len(df)):
            if df.iloc[i, 0] == '2015/12/31':
                code.append(df.iloc[i, 1])
        if len(code) > 30:
            code = code[0:30]
        g.security=code
        per_cash = cash/len(code)
        for i in code:
            order_value(i, per_cash)  # 买入股票
    
    cash = context.portfolio.cash  # 取得当前的现金量，命名为cash
    per_cash = cash/len(g.security)
     
    body = read_file("finally.csv")
    hushen = pd.read_csv(StringIO(body))
    hushen.drop('Unnamed: 0', axis=1, inplace=True)

    # date = str(context.current_dt)[0:10]
    date = context.current_dt.strftime("%Y/%m/%d")
    a,b,c=date.split('/')
    current_date=a+'/'+b+'/'+c
    for i in range(len(hushen)-1):
        if current_date==(hushen.loc[:, 'date']).iloc[i]:
            if (hushen.loc[:, 'price']).iloc[i+1]-(hushen.loc[:, 'price']).iloc[i]<-70:
                log.info("快跑")
                for i in g.security:
                    order_target(i, 0) 
            elif (hushen.loc[:, 'price']).iloc[i+1]-(hushen.loc[:, 'price']).iloc[i]>70:
                log.info("买买买")
                for i in g.security:
                        order_value(i, per_cash)         
            
            
            