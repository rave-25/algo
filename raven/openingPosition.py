
from unicodedata import name
import pandas as pd
import streamlit as st
import openpyxl

st.sidebar.title("Search Ticker")

menu = ["Select Fund", "Management Fund Account", "Gilad Account"]
selected_option = st.sidebar.selectbox("Choose an option:", menu)


# slider_value = st.sidebar.slider("Slider:", 0, 100, 50)
df = pd.read_excel("TPSL.xlsx")
if selected_option == "Select Fund":  
  st.markdown('''# **Welcome!**
  Let's open a position

  How it works:

  1. Choose ticker name at the sidebar for us to compute the required *New Price*, *New TP* and *New SL* for us to open it again.
  2. Set the new price in market order to buy long/ short
  3. Remove [TICKER NAME] in Open Order
  4. Navigate [TICKER NAME] in Positon and set TP/SL limit that we computed
  ''')
  st.subheader("Ticker's Data")
  st.dataframe(df)
  
elif selected_option == "Management Fund Account":
  st.subheader("Details of Postion: ")
  symbols = ['BTCUSDT','ETHUSDT','BNBUSDT','XRPUSDT', 'ADAUSDT', 'MATICUSDT', 'DOTUSDT', 'AVAXUSDT', 'UNIUSDT', 'LTCUSDT', 'ATOMUSDT',
  'LINKUSDT', 'ETCUSDT', 'ALGOUSDT', 'XMRUSDT', 'NEARUSDT', 'BCHUSDT', 'FILUSDT', 'APEUSDT', 'EGLDUSDT', 'SANDUSDT', 'AAVEUSDT', 'AXSUSDT',
  'EOSUSDT','VETUSDT','CRVUSDT','MANAUSDT','ENSUSDT','GMTUSDT','SNXUSDT','FLOWUSDT','ARUSDT','XLMUSDT','APTUSDT','DYDXUSDT',
  'SUSHIUSDT','WAVESUSDT','GALAUSDT','OPUSDT','KNCUSDT','KLAYUSDT','FTMUSDT']
  ticker = st.text_input("Enter a name of Ticker: ")
  ticker = ticker.lower()
  symbols = [value.lower() for value in symbols]
  #https://www.shanelynn.ie/pandas-iloc-loc-select-rows-and-columns-dataframe/
  if ticker in symbols:
      st.write("You entered: ", ticker.upper())
      column = "symbol"
      row = df.loc[df[column] == ticker.upper()]
      st.write(row)
      target_value = row.iloc[0]['gilad amount']

  prev_amount = st.number_input("Enter an amount from open orders:", format="%f")
  if prev_amount:
    results = []
    for n in range(20):
      result = target_value*(2.23**n)
      results.append(result)
      if abs(prev_amount-result)/result <= 0.40:
        for i, item in enumerate(results):
          if i == len(results) - 1:
            steps = i;
            st.write("No. of steps:", steps)
            st.markdown(''' 
            ### New position to open:
             ''')
            new_price = prev_amount*2.23 
            st.write("New position usdt price:", new_price)
            column = "symbol"
            row = df.loc[df[column] == ticker.upper()]
            tp_prev= row.iloc[0]['tp']
            sl_prev= row.iloc[0]['sl']
            new_tp = 0.002*steps + tp_prev
            new_sl = 0.002* steps + sl_prev
            entry_price = st.number_input("Enter entry price")
            if st.button("Buy Long"):
              tp_input = entry_price*(1+new_tp)
              sl_input = entry_price*(1-new_tp)
              new = pd.DataFrame({"NEW TP": [tp_input], "NEW SL": [sl_input]})
              st.dataframe(new)
            if st.button("Sell Short"):
              tp_input = entry_price*(1-new_tp)
              sl_input = entry_price*(1+new_tp)
              new = pd.DataFrame({"NEW TP": [tp_input], "NEW SL": [sl_input]})
              st.dataframe(new)
      
elif selected_option == "Gilad Account":
  st.subheader("Details of Postion: ")
  symbols = ['BTCUSDT','ETHUSDT','BNBUSDT','XRPUSDT', 'ADAUSDT', 'MATICUSDT', 'DOTUSDT', 'AVAXUSDT', 'UNIUSDT', 'LTCUSDT', 'ATOMUSDT',
  'LINKUSDT', 'ETCUSDT', 'ALGOUSDT', 'XMRUSDT', 'NEARUSDT', 'BCHUSDT', 'FILUSDT', 'APEUSDT', 'EGLDUSDT', 'SANDUSDT', 'AAVEUSDT', 'AXSUSDT',
  'EOSUSDT','VETUSDT','CRVUSDT','MANAUSDT','ENSUSDT','GMTUSDT','SNXUSDT','FLOWUSDT','ARUSDT','XLMUSDT','APTUSDT','DYDXUSDT',
  'SUSHIUSDT','WAVESUSDT','GALAUSDT','OPUSDT','KNCUSDT','KLAYUSDT','FTMUSDT']
  ticker = st.text_input("Enter a name of Ticker: ")
  ticker = ticker.lower()
  symbols = [value.lower() for value in symbols]
  if ticker in symbols:
      st.write("You entered: ", ticker.upper())
      column = "symbol"
      row = df.loc[df[column] == ticker.upper()]
      st.write(row)
      target_value = row.iloc[0]['gilad amount']

  prev_amount = st.number_input("Enter an amount from open orders:", format="%f")
  if prev_amount:
    results = []
    for n in range(20):
      result = target_value*(2.23**n)
      results.append(result)
      if abs(prev_amount-result)/result <= 0.40:
        for i, item in enumerate(results):
          if i == len(results) - 1:
            steps = i;
            st.write("No. of steps:", steps)
            st.markdown(''' 
            ### New position to open:
             ''')
            new_price = prev_amount*2.23 
            st.write("New position usdt price:", new_price)
            column = "symbol"
            row = df.loc[df[column] == ticker.upper()]
            tp_prev= row.iloc[0]['tp']
            sl_prev= row.iloc[0]['sl']
            new_tp = 0.002*steps + tp_prev
            new_sl = 0.002* steps + sl_prev
            entry_price = st.number_input("Enter entry price: ")
            if st.button("Buy Long"):
              tp_input = entry_price*(1+new_tp)
              sl_input = entry_price*(1-new_tp)
              new = pd.DataFrame({"NEW TP": [tp_input], "NEW SL": [sl_input]})
              st.dataframe(new)
            if st.button("Sell Short"):
              tp_input = entry_price*(1-new_tp)
              sl_input = entry_price*(1+new_tp)
              new = pd.DataFrame({"NEW TP": [tp_input], "NEW SL": [sl_input]})
              st.dataframe(new)