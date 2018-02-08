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

    def timeCheck(self):
        now = time.localtime()
        nowSec = now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec
        targetSec = 15.2 * 3600
        count = 0
        while count == 0:
            if nowSec >= targetSec:
                remainingSec = targetSec + (24 * 3600 - nowSec)
                hour = int(remainingSec / 3600)
                minute = int(remainingSec / 60 - hour * 60)
                sec = remainingSec - hour * 3600 - minute * 60
                print("남은시간은 %d 시간 %d분 %d초 입니다" % (hour, minute, sec))

            else:
                remainingSec = targetSec - nowSec
                hour = int(remainingSec / 3600)
                minute = int(remainingSec / 60 - hour * 60)
                sec = remainingSec - hour * 3600 - minute * 60
                print("남은시간은 %d 시간 %d분 %d초 입니다" % (hour, minute, sec))

        if remainingSec == 24*3600 or 0:
            return True

        print("남은시간은 %d 시간 %d분 %d초 입니다" % (hour, minute, sec))
        threading.Timer(1, self.timeCheck).start()


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
        print(threading._count)
        threading.Timer(1, self.getData).start()
        return True

    def preOrder(self):
        print("매수주문을 예약합니다.")

    def sell(self):
        td = Trade()
        if td.timeCheck() == True:
            print("데이터를 수신합니다")
            # stockQuantitiy = #매도가능수량 리퀘스트?
            if td.getData() == True:
                print("매도요청확인")
                URL = 'http://localhost:8080/order'
                headers = {'Content-Type': 'application/json; charset=utf-8'}
                data = {
                    "orderType": "2",
                    "accountNumber": "780516759",
                    "stockType": "01",
                    "stockCode": "A000300",
                    "stockQuantity": 1,
                    "stockPrice": 650,
                    "orderNumber": 0,
                    "bidAskQuote": "01"
                }
                response = requests.post(URL, json=data, headers=headers)


            print(response)


td = Trade()
print(td.timeCheck())

# def pfWeight(self):
#     wb = openpyxl.load_workbook('Trade_Log.xlsx')
#     ws = wb.get_sheet_by_name("Data")
#     for c in ws.columns:
#     f.close()

if __name__=='__main__':






