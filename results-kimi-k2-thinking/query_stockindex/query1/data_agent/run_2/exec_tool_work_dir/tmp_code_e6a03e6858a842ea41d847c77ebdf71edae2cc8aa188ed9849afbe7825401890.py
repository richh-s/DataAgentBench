code = """import json
import pandas as pd

# The variable name has a colon which can be problematic
# Let's check what variables are available
all_vars = list(locals().keys())
query_vars = [v for v in all_vars if 'query_db' in v]
print('Query db variables:', query_vars)

# Try to access the data by constructing the variable name
var_name = None
for v in query_vars:
    if ':10' in v:
        var_name = v
        break

print('Variable name found:', var_name)

if var_name and var_name in locals():
    data = locals()[var_name]
    print('Data type:', type(data))
    print('Data length:', len(data) if hasattr(data, '__len__') else 'N/A')
    if isinstance(data, str) and '.json' in data:
        print('It\'s a file path')
        # It's a file path
        file_path = data
        with open(file_path, 'r') as f:
            records = json.load(f)
        print('Records loaded:', len(records))
        df = pd.DataFrame(records)
        print('DataFrame shape:', df.shape)
        print('Indices:', df['Index'].unique())
        df['Open'] = pd.to_numeric(df['Open'])
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['Volatility'] = (df['High'] - df['Low']) / df['Open']
        avg_vol = df.groupby('Index')['Volatility'].mean().sort_values(ascending=False)
        print('\nAverage volatility:')
        print(avg_vol)
        
        # Asian indices
        asian = ['000001.SS', '399001.SZ', 'HSI', 'N225', 'NSEI', 'TWII']
        asian_vol = avg_vol[avg_vol.index.isin(asian)]
        print('\nAsian volatility:')
        print(asian_vol)
        
        if not asian_vol.empty:
            highest = asian_vol.index[0]
            vol = float(asian_vol.iloc[0])
            result = {'index': highest, 'volatility': vol}
        else:
            result = {'error': 'No Asian data'}
    else:
        result = {'error': 'Data is not a file path'}
else:
    result = {'error': 'Variable not found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5869'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:16': [{'Index': 'N225', 'days': '6349'}, {'Index': 'NYA', 'days': '6265'}, {'Index': 'IXIC', 'days': '5624'}, {'Index': 'GSPTSE', 'days': '4830'}, {'Index': 'HSI', 'days': '4006'}, {'Index': 'GDAXI', 'days': '3881'}, {'Index': 'SSMI', 'days': '3559'}, {'Index': '000001.SS', 'days': '2752'}, {'Index': 'TWII', 'days': '2751'}, {'Index': '399001.SZ', 'days': '2719'}, {'Index': 'N100', 'days': '2595'}, {'Index': 'NSEI', 'days': '1610'}, {'Index': 'J203.JO', 'days': '1210'}]}

exec(code, env_args)
