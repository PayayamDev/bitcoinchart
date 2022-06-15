
# !pip install mplfinance

# !pip install cryptopher


from cryptopher.collect.get_binance_data import GetBinanceData
from datetime import datetime
import mplfinance as fplt

# กำหนด time frame
tf = '1h'
start_date = '1 day ago UTC'
gbd = GetBinanceData(tf, start_date)

# ดึงข้อมูลราคาเหรียญ
target_name = 'BTCUSDT'
df1 = gbd.get_data(target_name)

# ปรับชื่อคอลัมน์ และกำหนด index เพื่อใช้แสดงกราฟ
df1.columns = ['Date', 'Open', 'High', 'Low', 'Close','Volume']
df1 = df1.set_index('Date')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

# แสดงกราฟราคา
fplt.plot(
            df1,
            type='candle',
            style= 'yahoo' ,
            title= '\r\n' + dt_string  + ' ' + target_name + ' (TF 1h)',
            ylabel='Price ($)' ,
            # volume=True,
            # mav=12,
            # figscale=1.5
        )



