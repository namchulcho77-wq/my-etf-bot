import tvscreener as tvs
from tvscreener import SymbolType
from tvscreener import StockScreener, StockField, FilterOperator
import pandas as pd

#레버리지 ETP
ss = tvs.StockScreener()
ss.set_symbol_types(SymbolType.ETF)
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
df