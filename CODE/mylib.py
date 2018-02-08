import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc('font', family='Malgun Gothic',size=8, weight = 'bold')

KOSDAQ_Data = pd.ExcelFile('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', header = 2)
KOSDAQ = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', sheetnames=0, header=1)
KOSDAQ150 = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', sheetnames=1)


# 함수정의

# 승리한 경우의 전일 종가 당일 시가
def Gap_Win(데이터):
    return 데이터[데이터.시가지수 > 데이터.종가지수.shift(1)]

# 기간 내 종가베팅 승률
def Win_Rate(데이터):
    return len(Gap_Win(데이터)) / len(데이터)


# 연단위 승률
def 일간수익률(데이터,매매비용=0.015):
    return (데이터.시가지수*(1-매매비용/100) - 데이터.종가지수.shift(1)*(1+매매비용/100)) / (데이터.종가지수.shift(1)*(1+매매비용/100))

def Win_Rate_Graph(데이터):
    x = []
    y = []
    for i in range(0,18):
        start = i*261
        end = start + 261
        y = y + [Win_Rate(데이터[start:end])]
        x.append(i)
    print(x)
    print(y)
    plt.plot(x,y)
    plt.show()

def MOM(데이터):
    a = 데이터.종가지수>데이터['3일 평균']
    b = 데이터.종가지수>데이터['5일 평균']
    c = 데이터.종가지수>데이터['10일 평균']
    d = 데이터.종가지수>데이터['15일 평균']
    k = [sum(x) for x in zip(a,b,c,d)]
    return k

def 벤치마크(데이터):
    a = pd.DataFrame(데이터.종가지수 / 데이터.종가지수.shift(1))
    a.index = 데이터.날짜
    c = a.cumprod()
    return c


def 누적수익곡선(데이터,매매비용=0.015,현금비중=4):
    누적수익 = 1
    gain = 일간수익률(데이터,매매비용)*현금비중/4
    누적수익 = (1+gain).cumprod()
    누적수익.index = 데이터.날짜
    return 누적수익

def SR(포트폴리오수익률, 무위험이자):
    pf = 포트폴리오수익률
    rf = 무위험이자
    ex = pf-rf
    sr = ex.cumprod()/pf.std()
    return sr


## MDD

