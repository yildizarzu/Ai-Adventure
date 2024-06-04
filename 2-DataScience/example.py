try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from statsmodels.tsa.arima.model import ARIMA
    from pandas_datareader import data as pdr
    import yfinance as yf
    
    # Yahoo Finance üzerinden hisse senedi verilerini almak için yfinance'in kullanılması
    yf.pdr_override()
    
    # Belirli bir hisse senedinin verilerini almak
    start_date = '2000-01-01'
    end_date = '2024-01-01'
    symbol = 'AAPL'  # Apple hisse senedi örneği
    data = pdr.get_data_yahoo(symbol, start=start_date, end=end_date)
    
    # Hisse senedi kapanış fiyatlarının alınması
    closing_prices = data['Close']
    
    # Zaman serisi verisinin görselleştirilmesi
    plt.figure(figsize=(10, 6))
    closing_prices.plot()
    plt.title(f'{symbol} Hisse Senedi Kapanış Fiyatları')
    plt.xlabel('Tarih')
    plt.ylabel('Kapanış Fiyatı ($)')
    plt.grid(True)
    plt.show()
    
    # ARIMA modelini uygulama
    model = ARIMA(closing_prices, order=(1, 1, 1))  # Örnek olarak ARIMA(1,1,1)
    results = model.fit()
    
    # Tahmin yapma
    forecast_steps = 10  # 10 adım için tahmin yapma
    forecast = results.forecast(steps=forecast_steps)
    
    # Tahmin edilen değerlerin görselleştirilmesi
    plt.figure(figsize=(10, 6))
    closing_prices.plot(label='Gerçek Kapanış Fiyatları')
    plt.plot(pd.date_range(end_date, periods=forecast_steps + 1)[1:], forecast, label='Tahmin Kapanış Fiyatları', linestyle='--')
    plt.title(f'{symbol} Hisse Senedi Kapanış Fiyatı Tahmini')
    plt.xlabel('Tarih')
    plt.ylabel('Kapanış Fiyatı ($)')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

except Exception as e:
    print(str(e))