code = """import pandas as pd

# Load the query results
result = var_functions.query_db:8

# Convert to DataFrame
df = pd.DataFrame(result)

# Convert string numbers to float
df['up_days'] = df['up_days'].astype(float)
df['down_days'] = df['down_days'].astype(float)

# Find indices with more up days than down days
up_more_than_down = df[df['up_days'] > df['down_days']]

# Map index codes to names
index_names = {
    'GSPTSE': 'S&P/TSX Composite (Toronto)',
    'IXIC': 'NASDAQ Composite',
    'NYA': 'NYSE Composite'
}

# Prepare the result
result_output = []
for _, row in up_more_than_down.iterrows():
    result_output.append({
        'index': row['Index'],
        'index_name': index_names.get(row['Index'], row['Index']),
        'up_days': int(row['up_days']),
        'down_days': int(row['down_days'])
    })

print('__RESULT__:')
print(pd.DataFrame(result_output).to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': [{'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}]}

exec(code, env_args)
