code = """import json
import pandas as pd

# Get the file path from the stored result
# The key should be in the format var_{tool_id}
file_path = locals().get('var_functions.query_db:8')

# If it's not a locals, check for a string variable
if not file_path:
    # The variable might be assigned differently, let's list available variables
    available_vars = [v for v in locals().keys() if 'query_db' in str(v)]
    print('debug: available vars with query_db:', available_vars)

# Read the query result from the file
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Open and Close to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Create a flag for up days (Close > Open) and down days (Close < Open)
df['is_up_day'] = df['Close'] > df['Open']
df['is_down_day'] = df['Close'] < df['Open']

# Group by index and count up vs down days
summary = df.groupby('Index').agg({
    'is_up_day': 'sum',
    'is_down_day': 'sum'
}).reset_index()

# Calculate the difference
summary['day_difference'] = summary['is_up_day'] - summary['is_down_day']

result = summary.to_dict('records')

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:3': ['index_trade'], 'var_functions.query_db:7': [{'Index': 'GDAXI', 'day_count': '98'}, {'Index': 'SSMI', 'day_count': '93'}, {'Index': 'GSPTSE', 'day_count': '86'}, {'Index': 'HSI', 'day_count': '85'}, {'Index': '000001.SS', 'day_count': '84'}, {'Index': 'J203.JO', 'day_count': '81'}, {'Index': 'NSEI', 'day_count': '78'}, {'Index': 'NYA', 'day_count': '78'}, {'Index': 'TWII', 'day_count': '78'}, {'Index': '399001.SZ', 'day_count': '76'}, {'Index': 'IXIC', 'day_count': '75'}, {'Index': 'N225', 'day_count': '74'}, {'Index': 'N100', 'day_count': '67'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
