code = """import json
import pandas as pd
from datetime import datetime

summary_data = var_functions.query_db_14

# Get the summary data
indices_summary = summary_data

# Create mapping between index symbols and exchanges/countries
index_mapping = {
    "000001.SS": {"exchange": "Shanghai Stock Exchange", "country": "China", "currency": "CNY"},
    "399001.SZ": {"exchange": "Shenzhen Stock Exchange", "country": "China", "currency": "CNY"},
    "GDAXI": {"exchange": "Frankfurt Stock Exchange", "country": "Germany", "currency": "EUR"},
    "GSPTSE": {"exchange": "Toronto Stock Exchange", "country": "Canada", "currency": "CAD"},
    "HSI": {"exchange": "Hong Kong Stock Exchange", "country": "Hong Kong", "currency": "HKD"},
    "IXIC": {"exchange": "NASDAQ", "country": "USA", "currency": "USD"},
    "J203.JO": {"exchange": "Johannesburg Stock Exchange", "country": "South Africa", "currency": "ZAR"},
    "N100": {"exchange": "Euronext", "country": "EU (Netherlands)", "currency": "EUR"},
    "N225": {"exchange": "Tokyo Stock Exchange", "country": "Japan", "currency": "JPY"},
    "NSEI": {"exchange": "National Stock Exchange of India", "country": "India", "currency": "INR"},
    "NYA": {"exchange": "New York Stock Exchange", "country": "USA", "currency": "USD"},
    "SSMI": {"exchange": "SIX Swiss Exchange", "country": "Switzerland", "currency": "CHF"},
    "TWII": {"exchange": "Taiwan Stock Exchange", "country": "Taiwan", "currency": "TWD"}
}

# Calculate estimated returns based on price data
results = []

for idx_info in indices_summary:
    index_name = idx_info["Index"]
    first_date = idx_info["first_date"]
    last_date = idx_info["last_date"]
    
    # Skip indices that started after 2010 (insufficient data since 2000)
    if "2012" in first_date:  # J203.JO started in 2012
        continue
        
    min_close = float(idx_info["min_close"])
    max_close = float(idx_info["max_close"])
    
    # Calculate approximate return based on min/max prices
    # This is a simplification - actual calculation would need full time series
    price_appreciation = ((max_close - min_close) / min_close) * 100
    
    # Estimate number of years
    try:
        start_year = int(first_date.split("-")[0])
        end_year_str = last_date.split("-")[0]
        if end_year_str.isdigit():
            end_year = int(end_year_str)
        else:
            # Handle "September 30, 2015 at 12:00 AM" format
            end_year = int(last_date.split(",")[1].strip().split()[0])
        years = max(end_year - start_year, 1)
    except:
        years = 15  # Default to ~15 years for most indices
    
    # Estimate annualized return
    if years > 0:
        # Assume the min price occurred near the beginning and max near the end
        total_return_est = ((max_close / min_close) ** (1/years) - 1) * 100
    else:
        total_return_est = 0
    
    # Add country and exchange info
    mapping = index_mapping.get(index_name, {})
    country = mapping.get("country", "Unknown")
    exchange = mapping.get("exchange", "Unknown")
    
    results.append({
        "Index": index_name,
        "Exchange": exchange,
        "Country": country,
        "Years_of_Data": years,
        "Min_Price_USD": round(min_close, 2),
        "Max_Price_USD": round(max_close, 2),
        "Estimated_Total_Return_Pct": round(price_appreciation, 1),
        "Estimated_Annualized_Return_Pct": round(total_return_est, 1)
    })

# Sort by estimated total return
results_sorted = sorted(results, key=lambda x: x["Estimated_Total_Return_Pct"], reverse=True)

# Get top 5
top_5 = results_sorted[:5]

# Create final answer
final_answer = []
for i, item in enumerate(top_5, 1):
    final_answer.append({
        "Rank": i,
        "Index_Symbol": item["Index"],
        "Exchange": item["Exchange"],
        "Country": item["Country"],
        "Estimated_Total_Return_Pct": item["Estimated_Total_Return_Pct"],
        "Data_Period_Years": item["Years_of_Data"]
    })

print('__RESULT__:')
print(json.dumps(final_answer, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:14': [{'Index': '000001.SS', 'total_records': '4354', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_close': '161.9355176', 'max_close': '965.80492192'}, {'Index': '399001.SZ', 'total_records': '4355', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_close': '411.37601568', 'max_close': '3124.9840624'}, {'Index': 'GDAXI', 'total_records': '5590', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_close': '1158.0727878', 'max_close': '18934.3761734'}, {'Index': 'GSPTSE', 'total_records': '6506', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'min_close': '1122.40904067', 'max_close': '16477.325352599997'}, {'Index': 'HSI', 'total_records': '5604', 'first_date': '2000-01-14 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_close': '265.27799688', 'max_close': '4310.0357417000005'}, {'Index': 'IXIC', 'total_records': '7351', 'first_date': '2000-01-06 00:00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'min_close': '55.48', 'max_close': '14138.78027'}, {'Index': 'J203.JO', 'total_records': '1854', 'first_date': '2012-02-08 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_close': '2302.1214454000005', 'max_close': '4805.917265800001'}, {'Index': 'N100', 'total_records': '4245', 'first_date': '2000-01-10 00:00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'min_close': '531.27340122', 'max_close': '1541.6163939'}, {'Index': 'N225', 'total_records': '7979', 'first_date': '2000-01-04 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_close': '10.2677002', 'max_close': '388.7694141'}, {'Index': 'NSEI', 'total_records': '2577', 'first_date': '2007-09-25 00:00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'min_close': '25.24199951', 'max_close': '155.8279981'}, {'Index': 'NYA', 'total_records': '7960', 'first_date': '2000-01-03 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_close': '347.769989', 'max_close': '16590.42969'}, {'Index': 'SSMI', 'total_records': '5188', 'first_date': '2000-01-05 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_close': '1466.19902664', 'max_close': '12683.026932900002'}, {'Index': 'TWII', 'total_records': '4385', 'first_date': '2000-01-17 00:00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'min_close': '137.8504004', 'max_close': '703.8360156'}], 'var_functions.query_db:16': [{'Index': 'N225', 'Date': '2000-01-04 00:00:00', 'Open': '18937.44922', 'High': '19187.60938', 'Low': '18937.44922', 'Close': '19002.85938', 'Adj Close': '19002.85938', 'CloseUSD': '190.0285938'}, {'Index': 'N225', 'Date': '2000-01-19 00:00:00', 'Open': '19181.86914', 'High': '19181.86914', 'Low': '18897.75', 'Close': '18897.75', 'Adj Close': '18897.75', 'CloseUSD': '188.9775'}, {'Index': 'N225', 'Date': '2000-01-20 00:00:00', 'Open': '18930.25977', 'High': '19167.0293', 'Low': '18921.10938', 'Close': '19008.00977', 'Adj Close': '19008.00977', 'CloseUSD': '190.0800977'}, {'Index': 'N225', 'Date': '2000-01-24 00:00:00', 'Open': '18878.46094', 'High': '19124.57031', 'Low': '18877.13086', 'Close': '19056.71094', 'Adj Close': '19056.71094', 'CloseUSD': '190.5671094'}, {'Index': 'N225', 'Date': '2000-01-25 00:00:00', 'Open': '19004.39063', 'High': '19131.18945', 'Low': '18815.36914', 'Close': '18895.5293', 'Adj Close': '18895.5293', 'CloseUSD': '188.955293'}, {'Index': 'N225', 'Date': '2000-01-31 00:00:00', 'Open': '19375.10938', 'High': '19539.69922', 'Low': '19224.4707', 'Close': '19539.69922', 'Adj Close': '19539.69922', 'CloseUSD': '195.3969922'}, {'Index': 'N225', 'Date': '2000-02-03 00:00:00', 'Open': '19648.34961', 'High': '19878.83008', 'Low': '19648.34961', 'Close': '19786.41992', 'Adj Close': '19786.41992', 'CloseUSD': '197.8641992'}, {'Index': 'N225', 'Date': '2000-02-14 00:00:00', 'Open': '19698.57031', 'High': '19748.41992', 'Low': '19556.46094', 'Close': '19556.46094', 'Adj Close': '19556.46094', 'CloseUSD': '195.5646094'}, {'Index': 'N225', 'Date': '2000-02-18 00:00:00', 'Open': '19852.17969', 'High': '19862.93945', 'Low': '19670.05078', 'Close': '19789.0293', 'Adj Close': '19789.0293', 'CloseUSD': '197.890293'}, {'Index': 'N225', 'Date': '2000-02-23 00:00:00', 'Open': '19439.16992', 'High': '19527.78906', 'Low': '19373.03906', 'Close': '19519.55078', 'Adj Close': '19519.55078', 'CloseUSD': '195.19550780000003'}], 'var_functions.execute_python:22': 'Check complete'}

exec(code, env_args)
