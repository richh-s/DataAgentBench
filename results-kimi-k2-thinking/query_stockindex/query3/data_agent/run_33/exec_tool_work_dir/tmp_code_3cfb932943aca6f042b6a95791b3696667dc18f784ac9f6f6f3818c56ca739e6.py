code = """import json
import pandas as pd
from datetime import datetime

# Read the query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Get unique indices
unique_indices = df['Index'].unique().tolist()
print('__RESULT__:')
print(json.dumps({
    'total_unique_indices': len(unique_indices),
    'all_indices': sorted(unique_indices)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:10': {'top_5_indices': [{'Index': 'IXIC', 'Country': 'United States', 'TotalReturnPct': 378.6, 'FinalValue': 122999.33, 'TotalInvested': 25700, 'Months': 257}, {'Index': '399001.SZ', 'Country': 'China', 'TotalReturnPct': 134.45, 'FinalValue': 60489.27, 'TotalInvested': 25800, 'Months': 258}, {'Index': 'GDAXI', 'Country': 'Germany', 'TotalReturnPct': 131.94, 'FinalValue': 59607.36, 'TotalInvested': 25700, 'Months': 257}, {'Index': 'TWII', 'Country': 'Taiwan', 'TotalReturnPct': 131.52, 'FinalValue': 59500.52, 'TotalInvested': 25700, 'Months': 257}, {'Index': 'NSEI', 'Country': 'India', 'TotalReturnPct': 121.47, 'FinalValue': 36542.38, 'TotalInvested': 16500, 'Months': 165}], 'total_indices_analyzed': 13}}

exec(code, env_args)
