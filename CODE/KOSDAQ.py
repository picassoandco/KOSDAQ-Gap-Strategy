import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import mylib as my
matplotlib.rc('font', family='Malgun Gothic',size=8, weight = 'bold')

KOSDAQ_Data = pd.ExcelFile('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', header = 2)
KOSDAQ = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', sheetnames=0, header=1)
KOSDAQ150 = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', sheetnames=1)
국고채3년 = pd.read_excel('C:/Users/이세령/picasso/KOSDAQ-Gap-Strategy/DATA/KOSDAQ2.xlsx', sheetname=2)
코스닥인버스 = pd.read_excel('C:\Users\이세령\picasso\KOSDAQ-Gap-Strategy\DATA\KOSDAQ2.xlsx', sheetname=3, header=1)
금리 = pd.read_excel('C:\Users\이세령\picasso\KOSDAQ-Gap-Strategy\DATA\KOSDAQ2.xlsx', sheetname=4, header=1)



rf = (금리.국고5년/100)/365
rf.index = KOSDAQ.날짜
pf = my.누적수익곡선(KOSDAQ,0.015)

def 누적수익곡선(데이터,매매비용=0.015,현금비중=4):
    누적수익 = 1
    gain = my.일간수익률(데이터,매매비용)*현금비중/4
    bond = rf.values*현금비중/4
    누적수익 = (1+gain+bond).cumprod()
    누적수익.index = 데이터.날짜
    return 누적수익


a = my.벤치마크(KOSDAQ)
b = my.누적수익곡선(KOSDAQ,0.015,my.MOM(KOSDAQ))
c = 누적수익곡선(KOSDAQ,0.015,my.MOM(KOSDAQ))
d = pd.concat([a, b, c], axis=1).dropna()
d.columns = ['벤치마크(코스닥)', '현금혼합종가베팅', '국고채혼합종가베팅_5년']
d.divide(d.ix[0]).plot(figsize = (18,12))
plt.show()

최대하락 = d.국고채혼합종가베팅_5년.rolling(min_periods=1, window = 500).max()
당월하락 = d.국고채혼합종가베팅_5년/최대하락 - 1.0
최대하락폭 = 당월하락.rolling(min_periods=1, window=500).min()

당월하락.plot(subplots=True, figsize = (18,2), linestyle='dotted')
최대하락폭.plot(subplots=True, figsize = (18,2), color = 'red', linestyle='dotted')
plt.show()

#6. MDD / CAGR
투자기간 = len(d.index)/262
print("MDD : "+str(최대하락폭.min()*100)[0:5]+"%")
print("CAGR : "+str(d.국고채혼합종가베팅_5년[-1]**(1/투자기간)*100-100)[0:4]+"%")
