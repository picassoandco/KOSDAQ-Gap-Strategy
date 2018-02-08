import threading
import requests
import time
import pandas as pd
import openpyxl
import pandas as pd

price = []


class Trade:

    def __init__(self):
        pass

    def timeBuy(self):
        now = time.localtime()
        nowSec = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
        targetSec = 15.45 * 3600
        if nowSec >= targetSec:
            remainingSec = targetSec + (24 * 3600 - nowSec)
            hour = int(remainingSec / 3600)
            minute = int(remainingSec / 60 - hour * 60)
            sec = remainingSec - hour * 3600 - minute * 60

        else:
            remainingSec = targetSec - nowSec
            hour = int(remainingSec / 3600)
            minute = int(remainingSec / 60 - hour * 60)
            sec = remainingSec - hour * 3600 - minute * 60

        print("남은시간은 %d 시간 %d분 %d초 입니다" % (hour, minute, sec))
        if remainingSec == 24 * 3600 or 0:
            return True
        time.sleep(1)

        # threading.Timer(1, self.timeCheck).start()
    def timeSell(self):
        now = time.localtime()
        nowSec = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
        targetSec = 9 * 3600
        if nowSec >= targetSec:
            remainingSec = targetSec + (24 * 3600 - nowSec)
            hour = int(remainingSec / 3600)
            minute = int(remainingSec / 60 - hour * 60)
            sec = remainingSec - hour * 3600 - minute * 60

        else:
            remainingSec = targetSec - nowSec
            hour = int(remainingSec / 3600)
            minute = int(remainingSec / 60 - hour * 60)
            sec = remainingSec - hour * 3600 - minute * 60

        print("남은시간은 %d 시간 %d분 %d초 입니다" % (hour, minute, sec))
        if remainingSec == 24 * 3600 or 0:
            return True
        time.sleep(1)

    def getData(self):
        URL = 'http://localhost:8080/stock/A229200/price'
        response = requests.get(URL)
        result = response.json()
        price.insert(0, result['last'])
        if len(price) == 2:
            if price[0] < price[1]:
                print('%d 원에 시장가 매도합니다.' % (price[0]))
                return True

        elif len(price) > 2:
            del (price[2])
            if price[0] < price[1]:
                print('%d 원에 시장가 매도합니다.' % (price[0]))
                return True
        else:
            pass

        print(price)
        time.sleep(150)

        # threading.Timer(1, self.getData).start()

    def stockQunt(self):
        URL = 'http://localhost:8080/orders/complete'
        response = requests.get(URL)
        result = response.json()
        if result[-1]['orderType'] == '매수':
            return result[-1]['stockQuantity']

    def buy(self):
        print("매수요청확인")
        URL = 'http://localhost:8080/order'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            "orderType": "2",
            "accountNumber": "780516759",
            "stockType": "01",
            "stockCode": "A229200",
            "stockQuantity": 18,
            "stockPrice": 0,
            "orderNumber": 0,
            "bidAskQuote": "03"
        }
        response = requests.post(URL, json=data, headers=headers)
        result = response.json()
        print(result)

    def sell(self):
        print("매도요청확인")
        td = Trade()
        quant = td.stockQunt()
        URL = 'http://localhost:8080/order'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {
            "orderType": "1",
            "accountNumber": "780516759",
            "stockType": "01",
            "stockCode": "A229200",
            "stockQuantity": quant,
            "stockPrice": 0,
            "orderNumber": 0,
            "bidAskQuote": "03"
        }
        response = requests.post(URL, json=data, headers=headers)
        result = response.json()
        print(result)




# def pfWeight(self):
#     wb = openpyxl.load_workbook('Trade_Log.xlsx')
#     ws = wb.get_sheet_by_name("Data")
#     for c in ws.columns:
#     f.close()

def main():
    td = Trade()
    while td.timeBuy() != True:
        None
    td.buy()

def main2():
    td = Trade()
    while td.timeSell() != True:
        None
    while td.getData() != True:
        None
    td.sell()

main2()
# if td.getData() == True:





