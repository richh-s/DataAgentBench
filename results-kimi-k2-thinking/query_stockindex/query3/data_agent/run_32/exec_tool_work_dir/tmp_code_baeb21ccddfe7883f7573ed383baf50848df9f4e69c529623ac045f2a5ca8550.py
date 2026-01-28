code = """import json
import pandas as pd

# Load data
index_info_data = locals()['var_functions.query_db:2']
top_5_results = locals()['var_functions.execute_python:18']

index_info_df = pd.DataFrame(index_info_data)
top_5_df = pd.DataFrame(top_5_results)

# Create a mapping of index symbols to exchanges and countries
index_country_mapping = {
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'United States', 'Full_Name': 'NASDAQ Composite'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China', 'Full_Name': 'Shenzhen Component Index'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany', 'Full_Name': 'DAX Performance Index'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan', 'Full_Name': 'TAIEX (Taiwan Capitalization Weighted Stock Index)'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India', 'Full_Name': 'NIFTY 50'}
}

# Enrich top 5 results with country and exchange info
final_results = []
for _, row in top_5_df.iterrows():
    idx = row['Index']
    mapping = index_country_mapping.get(idx, {'Exchange': 'Unknown', 'Country': 'Unknown', 'Full_Name': 'Unknown'})
    
    final_results.append({
        'Index': idx,
        'Index_Name': mapping['Full_Name'],
        'Exchange': mapping['Exchange'],
        'Country': mapping['Country'],
        'Total_Return_Percent': round(row['Total_Return_Pct'], 2),
        'CAGR_Percent': round(row['CAGR'], 2),
        'Years_of_Data': round(row['Total_Years'], 1),
        'Total_Invested_USD': int(row['Total_Invested']),
        'Current_Value_USD': round(row['Current_Value'], 2)
    })

print('__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:9': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'index_info_sample': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'index_symbols': ['J203.JO', 'N225', 'GSPTSE', 'NSEI', 'GDAXI', 'IXIC', 'HSI', '000001.SS', 'SSMI', 'TWII', 'NYA', 'N100', '399001.SZ'], 'trade_data_columns': ['Index', 'Date', 'CloseUSD'], 'trade_data_row_count': 67948, 'unique_indices': ['000001.SS', '399001.SZ', 'GDAXI', 'GSPTSE', 'HSI', 'IXIC', 'J203.JO', 'N100', 'N225', 'NSEI', 'NYA', 'SSMI', 'TWII']}, 'var_functions.execute_python:18': [{'Index': 'IXIC', 'Total_Years': 21.4166666667, 'Total_Invested': 25700, 'Current_Value': 123006.9775373993, 'Total_Return_Pct': 378.6263717409, 'CAGR': 7.5847748025, 'Simple_Return_Pct': 230.0170732948, 'First_Price': 4131.149902, 'Last_Price': 13633.5, 'Months': 257}, {'Index': '399001.SZ', 'Total_Years': 21.5, 'Total_Invested': 25800, 'Current_Value': 60576.5636373844, 'Total_Return_Pct': 134.7928823154, 'CAGR': 4.0497783514, 'Simple_Return_Pct': 326.1811264636, 'First_Price': 557.80640624, 'Last_Price': 2377.2656256, 'Months': 258}, {'Index': 'GDAXI', 'Total_Years': 21.4166666667, 'Total_Invested': 25700, 'Current_Value': 59627.0927932049, 'Total_Return_Pct': 132.0120342148, 'CAGR': 4.0079744717, 'Simple_Return_Pct': 131.3129639505, 'First_Price': 8036.0792379, 'Last_Price': 18588.4930706, 'Months': 257}, {'Index': 'TWII', 'Total_Years': 21.4166666667, 'Total_Invested': 25700, 'Current_Value': 59556.042493867, 'Total_Return_Pct': 131.7355739061, 'CAGR': 4.0021844016, 'Simple_Return_Pct': 94.6056764937, 'First_Price': 353.99480468, 'Last_Price': 688.8939844, 'Months': 257}, {'Index': 'NSEI', 'Total_Years': 13.75, 'Total_Invested': 16500, 'Current_Value': 36504.443858157, 'Total_Return_Pct': 121.2390536858, 'CAGR': 5.9450957021, 'Simple_Return_Pct': 221.5399450749, 'First_Price': 45.46200195, 'Last_Price': 146.1784961, 'Months': 165}]}

exec(code, env_args)
