code = """import json
import pandas as pd

# Load data
price_data_file = locals()['var_functions.query_db:8']
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Load index info
index_info = locals()['var_functions.query_db:5']

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Data cleaning
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna()

# Filter from 2000 onwards
df = df[df['Date'] >= '2000-01-01']

# Create mapping based on exchange information
# Based on index_info and financial knowledge
index_exchange_mapping = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange', 
    '000001.SS': 'Shanghai Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'IXIC': 'NASDAQ',
    'NYA': 'New York Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'GSPTSE': 'Toronto Stock Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'N100': 'Euronext',
    'J203.JO': 'Johannesburg Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange'
}

# Create exchange to country mapping from index_info
exchange_to_country = {
    'Tokyo Stock Exchange': 'Japan',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Shanghai Stock Exchange': 'China',
    'Frankfurt Stock Exchange': 'Germany',
    'NASDAQ': 'United States',
    'New York Stock Exchange': 'United States',
    'National Stock Exchange of India': 'India',
    'Toronto Stock Exchange': 'Canada',
    'Taiwan Stock Exchange': 'Taiwan',
    'SIX Swiss Exchange': 'Switzerland',
    'Euronext': 'Euronext (multi-country)',
    'Johannesburg Stock Exchange': 'South Africa',
    'Shenzhen Stock Exchange': 'China'
}

# Create index to country mapping
index_country = {}
for index, exchange in index_exchange_mapping.items():
    index_country[index] = exchange_to_country[exchange]

print('__RESULT__:')
print(json.dumps({
    'index_country_mapping': index_country,
    'indices_count': len(index_country)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:7': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': 'IXIC'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:24': {'variables': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:7', 'var_functions.query_db:8', '__builtins__', 'json']}, 'var_functions.execute_python:28': {'status': 'success', 'message': 'Data loaded: 21342 records from 2000-01-03 00:00:00 to 2021-06-02 00:00:00', 'indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}, 'var_functions.execute_python:30': {'top_5_indices': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Invested': 25700, 'Final_Value': 123926.60191493503, 'Total_Return': 98226.60191493503, 'Return_Percentage': 382.20467671180944, 'Months_Invested': 257}, {'Index': 'NSEI', 'Country': 'India', 'Total_Invested': 16500, 'Final_Value': 38954.60209596197, 'Total_Return': 22454.60209596197, 'Return_Percentage': 136.08849755128466, 'Months_Invested': 165}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Invested': 25700, 'Final_Value': 60329.783259690324, 'Total_Return': 34629.783259690324, 'Return_Percentage': 134.7462383645538, 'Months_Invested': 257}, {'Index': '399001.SZ', 'Country': 'China', 'Total_Invested': 25800, 'Final_Value': 60489.269678002216, 'Total_Return': 34689.269678002216, 'Return_Percentage': 134.4545336356675, 'Months_Invested': 258}, {'Index': 'TWII', 'Country': 'Taiwan', 'Total_Invested': 25700, 'Final_Value': 57501.33870840872, 'Total_Return': 31801.338708408723, 'Return_Percentage': 123.74061754244639, 'Months_Invested': 257}], 'all_results': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Invested': 25700, 'Final_Value': 123926.60191493503, 'Total_Return': 98226.60191493503, 'Return_Percentage': 382.20467671180944, 'Months_Invested': 257}, {'Index': 'NSEI', 'Country': 'India', 'Total_Invested': 16500, 'Final_Value': 38954.60209596197, 'Total_Return': 22454.60209596197, 'Return_Percentage': 136.08849755128466, 'Months_Invested': 165}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Invested': 25700, 'Final_Value': 60329.783259690324, 'Total_Return': 34629.783259690324, 'Return_Percentage': 134.7462383645538, 'Months_Invested': 257}, {'Index': '399001.SZ', 'Country': 'China', 'Total_Invested': 25800, 'Final_Value': 60489.269678002216, 'Total_Return': 34689.269678002216, 'Return_Percentage': 134.4545336356675, 'Months_Invested': 258}, {'Index': 'TWII', 'Country': 'Taiwan', 'Total_Invested': 25700, 'Final_Value': 57501.33870840872, 'Total_Return': 31801.338708408723, 'Return_Percentage': 123.74061754244639, 'Months_Invested': 257}, {'Index': 'N225', 'Country': 'Japan', 'Total_Invested': 25800, 'Final_Value': 55588.57820149415, 'Total_Return': 29788.57820149415, 'Return_Percentage': 115.45960543214787, 'Months_Invested': 258}, {'Index': 'NYA', 'Country': 'United States', 'Total_Invested': 25700, 'Final_Value': 51568.570271584016, 'Total_Return': 25868.570271584016, 'Return_Percentage': 100.65591545363431, 'Months_Invested': 257}, {'Index': 'GSPTSE', 'Country': 'Canada', 'Total_Invested': 25600, 'Final_Value': 42891.76721144923, 'Total_Return': 17291.76721144923, 'Return_Percentage': 67.54596566972356, 'Months_Invested': 256}, {'Index': '000001.SS', 'Country': 'China', 'Total_Invested': 25700, 'Final_Value': 42189.26833637256, 'Total_Return': 16489.26833637256, 'Return_Percentage': 64.16057718432903, 'Months_Invested': 257}, {'Index': 'N100', 'Country': 'Euronext', 'Total_Invested': 25700, 'Final_Value': 41085.701779739735, 'Total_Return': 15385.701779739735, 'Return_Percentage': 59.86654389003788, 'Months_Invested': 257}, {'Index': 'HSI', 'Country': 'Hong Kong', 'Total_Invested': 25700, 'Final_Value': 40163.71059482965, 'Total_Return': 14463.710594829652, 'Return_Percentage': 56.27902955186636, 'Months_Invested': 257}, {'Index': 'SSMI', 'Country': 'Switzerland', 'Total_Invested': 25700, 'Final_Value': 40079.51210632446, 'Total_Return': 14379.512106324459, 'Return_Percentage': 55.95140897402513, 'Months_Invested': 257}, {'Index': 'J203.JO', 'Country': 'South Africa', 'Total_Invested': 11200, 'Final_Value': 15292.372487425535, 'Total_Return': 4092.372487425535, 'Return_Percentage': 36.539040066299414, 'Months_Invested': 112}]}}

exec(code, env_args)
