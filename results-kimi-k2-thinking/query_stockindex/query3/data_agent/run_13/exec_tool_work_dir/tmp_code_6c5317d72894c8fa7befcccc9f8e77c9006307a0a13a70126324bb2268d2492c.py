code = """import json

# Get the info data
info_data = locals()['var_functions.query_db:16']

# Map indices to countries based on the info data and geographic knowledge
# Also check which indices are in the info data

# Create a mapping dict
exchange_mapping = {
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'GSPTSE': 'Toronto Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    'IXIC': 'NASDAQ',
    'J203.JO': 'Johannesburg Stock Exchange',
    'N100': 'Euronext',
    'N225': 'Tokyo Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'NYA': 'New York Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange'
}

# Countries for each exchange
country_mapping = {
    'NASDAQ': 'United States',
    'Shanghai Stock Exchange': 'China',
    'Shenzhen Stock Exchange': 'China',
    'Frankfurt Stock Exchange': 'Germany',
    'Toronto Stock Exchange': 'Canada',
    'Hong Kong Stock Exchange': 'Hong Kong',
    'Johannesburg Stock Exchange': 'South Africa',
    'Euronext': 'Europe (Multi-country)',
    'Tokyo Stock Exchange': 'Japan',
    'National Stock Exchange of India': 'India',
    'New York Stock Exchange': 'United States',
    'SIX Swiss Exchange': 'Switzerland',
    'Taiwan Stock Exchange': 'Taiwan'
}

# Top 5 from our analysis
top_5_indices = [
    {'Index': 'IXIC', 'Total_Return_Pct': 378.59663101868665},
    {'Index': '399001.SZ', 'Total_Return_Pct': 134.4545336356675},
    {'Index': 'GDAXI', 'Total_Return_Pct': 131.93527211722628},
    {'Index': 'TWII', 'Total_Return_Pct': 131.51952869880725},
    {'Index': 'NSEI', 'Total_Return_Pct': 121.46893972422355}
]

# Add exchange and country info
results_with_countries = []
for item in top_5_indices:
    index_symbol = item['Index']
    exchange = exchange_mapping.get(index_symbol, 'Unknown Exchange')
    country = country_mapping.get(exchange, 'Unknown Country')
    
    results_with_countries.append({
        'Index': index_symbol,
        'Exchange': exchange,
        'Country': country,
        'Total_Return_Pct': round(item['Total_Return_Pct'], 2)
    })

print('__RESULT__:')
print(json.dumps(results_with_countries, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:9': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:20': {'trade_indices': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'info_data': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}, 'var_functions.execute_python:26': {'type': "<class 'str'>", 'is_list': False, 'is_string': True, 'value': 'file_storage/functions.query_db:8.json'}, 'var_functions.execute_python:30': [{'Index': 'IXIC', 'Total_Return_Pct': 378.59663101868665, 'Start_Date': '2000-01-06 00:00:00', 'End_Date': '2021-05-04 00:00:00', 'Months_of_Data': 257}, {'Index': '399001.SZ', 'Total_Return_Pct': 134.4545336356675, 'Start_Date': '2000-01-05 00:00:00', 'End_Date': '2021-06-02 00:00:00', 'Months_of_Data': 258}, {'Index': 'GDAXI', 'Total_Return_Pct': 131.93527211722628, 'Start_Date': '2000-01-05 00:00:00', 'End_Date': '2021-05-03 00:00:00', 'Months_of_Data': 257}, {'Index': 'TWII', 'Total_Return_Pct': 131.51952869880725, 'Start_Date': '2000-01-17 00:00:00', 'End_Date': '2021-05-03 00:00:00', 'Months_of_Data': 257}, {'Index': 'NSEI', 'Total_Return_Pct': 121.46893972422355, 'Start_Date': '2007-09-25 00:00:00', 'End_Date': '2021-05-05 00:00:00', 'Months_of_Data': 165}]}

exec(code, env_args)
