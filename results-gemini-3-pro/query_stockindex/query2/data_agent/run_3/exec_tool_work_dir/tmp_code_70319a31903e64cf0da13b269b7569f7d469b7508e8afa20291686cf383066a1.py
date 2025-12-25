code = """import json
import pandas as pd

# Load the data from the previous step
file_path = locals()['var_function-call-11185076478995352893']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Dictionary to store results
results = {}

# Process each index
indices = df['Index'].unique()

for index in indices:
    index_data = df[df['Index'] == index]
    up_days = len(index_data[index_data['Close'] > index_data['Open']])
    down_days = len(index_data[index_data['Close'] < index_data['Open']])
    
    results[index] = {
        'up_days': up_days,
        'down_days': down_days,
        'total_days': len(index_data)
    }

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-12096525047741818797': [{'cid': '0', 'name': 'Exchange', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'Currency', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-1941902004010842088': ['index_info'], 'var_function-call-6799846331580767551': ['index_trade'], 'var_function-call-3721481768615715075': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-11815488541320382343': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-12461719034831122098': 'file_storage/function-call-12461719034831122098.json', 'var_function-call-10066841718398887357': {'NYA': {'up_days': 36, 'down_days': 42}, 'IXIC': {'up_days': 44, 'down_days': 31}, 'GSPTSE': {'up_days': 44, 'down_days': 41}}, 'var_function-call-11128492963128070585': [{'Index': 'GSPTSE', 'cnt': '86'}, {'Index': 'IXIC', 'cnt': '75'}, {'Index': 'NYA', 'cnt': '79'}], 'var_function-call-14609447282840066878': [{'Index': 'GSPTSE', 'min(Date)': '2018-01-03 00:00:00', 'max(Date)': '2018-12-27 00:00:00'}, {'Index': 'IXIC', 'min(Date)': '2018-01-02 00:00:00', 'max(Date)': '2018-12-13 00:00:00'}, {'Index': 'NYA', 'min(Date)': '2018-01-09 00:00:00', 'max(Date)': '2018-12-31 00:00:00'}], 'var_function-call-11185076478995352893': 'file_storage/function-call-11185076478995352893.json'}

exec(code, env_args)
