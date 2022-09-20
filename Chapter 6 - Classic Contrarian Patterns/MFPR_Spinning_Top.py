
# Choosing the asset
pair = 0

# Time Frame
horizon = 'H1'

'''
Use body = 0.0003 for EURUSD, USDCHF, GBPUSD, USDCAD
Use body = 50 for BTCUSD
Use body = 10 for ETHUSD
Use body = 2 for XAUUSD
Use body = 5 for SP500m, UK100

Use wick = 0.0005 for EURUSD, USDCHF, GBPUSD, USDCAD
Use wick = 20 for BTCUSD
Use wick = 5 for ETHUSD
Use wick = 1 for XAUUSD
Use wick = 3 for SP500m, UK100

'''

body = 0.0003
wick = 0.0005

# Importing the asset as an array
my_data = mass_import(pair, horizon)

def signal(data, open_column, high_column, low_column, close_column, buy_column, sell_column):

    data = add_column(data, 5)    
    
    for i in range(len(data)):  
        
       try:
           
            # Bullish pattern
            if data[i, close_column] - data[i, open_column] > body and \
               data[i - 1, high_column] - data[i - 1, close_column] >= wick and \
               data[i - 1, open_column] - data[i - 1, low_column] >= wick and \
               data[i - 1, close_column] - data[i - 1, open_column] < body and \
               data[i - 1, close_column] > data[i - 1, open_column] and \
               data[i - 2, close_column] < data[i - 2, open_column] and \
               data[i - 2, open_column] - data[i - 2, close_column] > body:
                   
                     data[i + 1, buy_column] = 1 
                     
            # Bearish pattern
            elif data[i, open_column] - data[i, close_column] > body and \
                 data[i - 1, high_column] - data[i - 1, open_column] >= wick and \
                 data[i - 1, close_column] - data[i - 1, low_column] >= wick and \
                 data[i - 1, open_column] - data[i - 1, close_column] < body and \
                 data[i - 1, close_column] < data[i - 1, open_column] and \
                 data[i - 2, close_column] > data[i - 2, open_column] and \
                 data[i - 2, close_column] - data[i - 2, open_column] > body:
                     
                     data[i + 1, sell_column] = -1                      
                    
       except IndexError:
            
            pass
        
    return data

# Calling the signal function
my_data = signal(my_data, 0, 1, 2, 3, 4, 5)

# Charting the latest signals
signal_chart(my_data, 0, 4, 5, genre = 'candles', window = 100)

# Performance
my_data = performance(my_data, 0, 4, 5, 6, 7, 8)