import tvscreener as tvs
#from tvscreener import SymbolType
from tvscreener import StockScreener, StockField, FilterOperator
import pandas as pd


def run_leverage_etf():
  #레버리지 ETP
  ss = tvs.StockScreener()
  #ss.set_symbol_types(SymbolType.ETF)
  ss.select(StockField.NAME, StockField.PRICE, StockField.CHANGE_PERCENT, StockField.DESCRIPTION, StockField.EXCHANGE, StockField.LAUNCH_DATE, StockField.SELECTION_CRITERIA,StockField.STRATEGY, StockField.LEVERAGE_RATIO)

  ss.where(StockField.LEVERAGED_FLAG == "Leveraged" )           # AND
  #ss.where(StockField.STRATEGY != "4" )           # AND

  ss.set_range(0, 1000)    # First 100 results
  ss.sort_by(StockField.LAUNCH_DATE, ascending=False)                  # Most active
  #ss.sort_by(StockField.NAME, ascending=True)                  # Most active

  df = ss.get()
  df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s', utc=True)
  df['Launch Date'] = df['Launch Date'].dt.tz_convert('America/New_York')
  df['Launch Date'] = df['Launch Date'].dt.strftime('%Y-%m-%d')
  

  with open('leverage_etf.txt', 'w', encoding='utf-8') as f:
      # to_string()을 쓰면 출력 화면 그대로 저장됩니다.
      f.write(df.to_string(index=False))
      print(f"leverage_etf 파일 생성 완료!")

def run_cryto_etf():
  ss = tvs.StockScreener()
  ss.set_symbol_types(SymbolType.ETF)
  ss.select(StockField.NAME, StockField.PRICE, StockField.CHANGE_PERCENT, StockField.DESCRIPTION, StockField.EXCHANGE, StockField.LAUNCH_DATE, StockField.SELECTION_CRITERIA,StockField.STRATEGY)

  ss.where(StockField.ASSET_CLASS == "1af0389838508d7016a9841eb6273962" )           # AND
  ss.where(StockField.LEVERAGED_FLAG == "Non-leveraged" )           # AND
  #ss.where(StockField.STRATEGY != "4" )           # AND

  ss.set_range(0, 1000)    # First 100 results
  ss.sort_by(StockField.LAUNCH_DATE, ascending=False)                  # Most active

  df = ss.get()
  df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s', utc=True)
  df['Launch Date'] = df['Launch Date'].dt.tz_convert('America/New_York')
  df['Launch Date'] = df['Launch Date'].dt.strftime('%Y-%m-%d')
  
  with open('cryto_etf.txt', 'w', encoding='utf-8') as f:
      # to_string()을 쓰면 출력 화면 그대로 저장됩니다.
      f.write(df.to_string(index=False))
      print(f"cryto_etf 파일 생성 완료!")

def run_singleStockExCoveredCall_etf():
  ss = tvs.StockScreener()
  ss.set_symbol_types(SymbolType.ETF)
  ss.select(StockField.NAME, StockField.PRICE, StockField.CHANGE_PERCENT, StockField.DESCRIPTION, StockField.EXCHANGE, StockField.LAUNCH_DATE, StockField.SELECTION_CRITERIA, StockField.STRATEGY, StockField.LEVERAGE_RATIO)

  #ss.where(StockField.PRICE > 90)           # AND
  #ss.where(StockField.CATEGORY == "27" )           # AND
  #ss.where(StockField.FOCUS == "61" )           # AND
  ss.where(StockField.ASSET_CLASS == "c05f85d35d1cd0be6ebb2af4be16e06a" )           # AND
  ss.where(StockField.SELECTION_CRITERIA == "36" )           # AND
  ss.where(StockField.STRATEGY != "4" )           # AND
  ss.set_range(0, 1000)    # First 100 results
  ss.sort_by(StockField.LAUNCH_DATE, ascending=False)                  # Most active


  df = ss.get()
  df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s', utc=True)
  df['Launch Date'] = df['Launch Date'].dt.tz_convert('America/New_York')
  df['Launch Date'] = df['Launch Date'].dt.strftime('%Y-%m-%d')

  with open('singleStockExCoveredCall_etf.txt', 'w', encoding='utf-8') as f:
      # to_string()을 쓰면 출력 화면 그대로 저장됩니다.
      f.write(df.to_string(index=False))
      print(f"singleStockExCoveredCall_etf 파일 생성 완료!")

def run_singleStockCoveredCall_etf():
  ss = tvs.StockScreener()
  ss.set_symbol_types(SymbolType.ETF)
  ss.select(StockField.NAME, StockField.PRICE, StockField.CHANGE_PERCENT, StockField.DESCRIPTION, StockField.EXCHANGE, StockField.LAUNCH_DATE, StockField.SELECTION_CRITERIA,StockField.STRATEGY)


  #ss.where(StockField.PRICE > 90)           # AND
  #ss.where(StockField.CATEGORY == "27" )           # AND
  #ss.where(StockField.FOCUS == "61" )           # AND
  ss.where(StockField.ASSET_CLASS == "c05f85d35d1cd0be6ebb2af4be16e06a" )           # AND
  ss.where(StockField.SELECTION_CRITERIA == "36" )           # AND
  ss.where(StockField.STRATEGY == "4" )           # AND
  ss.set_range(0, 1000)    # First 100 results
  ss.sort_by(StockField.LAUNCH_DATE, ascending=False)                  # Most active


  df = ss.get()
  #df['Launch Date'] = pd.to_datetime(df['Launch Date'])
  #df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s')
  #df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s', utc=True)
  #df['Launch Date'] = df['Launch Date'].dt.tz_convert('America/New_York')
  #df['Launch Date'] = df['Launch Date'].dt.strftime('%Y-%m-%d')
  df['Launch Date'] = pd.to_datetime(df['Launch Date'], unit='s', utc=True).dt.tz_convert('America/New_York').dt.strftime('%Y-%m-%d')

  with open('singleStockCoveredCall_etf.txt', 'w', encoding='utf-8') as f:
      # to_string()을 쓰면 출력 화면 그대로 저장됩니다.
      f.write(df.to_string(index=False))
      print(f"singleStockCoveredCall_etf 파일 생성 완료!")

if __name__ == "__main__":
    run_leverage_etf()
    run_cryto_etf()
    run_singleStockExCoveredCall_etf()
    run_singleStockCoveredCall_etf()
