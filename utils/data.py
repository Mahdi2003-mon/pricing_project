import yfinance as yf
yf.download("AAPL", start="2020-01-01")
 → rename Close → y, Date → ds
 → return df[["ds", "y"]]