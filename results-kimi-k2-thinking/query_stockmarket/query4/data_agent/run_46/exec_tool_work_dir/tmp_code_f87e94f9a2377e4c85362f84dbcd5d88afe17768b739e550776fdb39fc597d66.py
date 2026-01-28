code = """import json
import pandas as pd

# Load AIN's 2017 data
ain_file = 'file_storage/functions.query_db:28.json'
with open(ain_file, 'r') as f:
    ain_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(ain_data)
# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Calculate up/down days
df['up_day'] = df['Close'] > df['Open']
df['down_day'] = df['Close'] < df['Open']

up_days = df['up_day'].sum()
down_days = df['down_day'].sum()
total_days = len(df)

print('__RESULT__:')
print(json.dumps({
    'symbol': 'AIN',
    'company_name': 'Albany International Corporation',
    'total_trading_days': int(total_days),
    'up_days': int(up_days),
    'down_days': int(down_days),
    'up_minus_down': int(up_days - down_days)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['stockinfo'], 'var_functions.execute_python:12': {'file_path': 'file_storage/functions.query_db:0.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:14': {'total_nyse_stocks': 234, 'first_10_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_names': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}}, 'var_functions.list_db:16': 'file_storage/functions.list_db:16.json', 'var_functions.execute_python:18': {'total_nyse_stocks': 234, 'total_trade_tables': 2753, 'available_symbols': 234, 'first_10_available': ['SI', 'CHAP', 'AJRD', 'VKQ', 'RES', 'GLOB', 'UTL', 'PSXP', 'TRV', 'CVX']}, 'var_functions.execute_python:20': {'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'count': 10}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'total_symbols': 234, 'sample_data': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions'}}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
