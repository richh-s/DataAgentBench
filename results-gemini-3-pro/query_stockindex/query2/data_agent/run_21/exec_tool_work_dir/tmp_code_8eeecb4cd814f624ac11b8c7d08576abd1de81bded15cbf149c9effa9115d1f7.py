code = """import pandas as pd
import json

# Load the data from the previous step
with open(locals()['var_function-call-300034308587137483'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate counts per index
results = {}
for index_name, group in df.groupby('Index'):
    up_days = group[group['Close'] > group['Open']].shape[0]
    down_days = group[group['Close'] < group['Open']].shape[0]
    results[index_name] = {'up': up_days, 'down': down_days}

# Filter indices with more up days than down days
more_up_indices = [idx for idx, counts in results.items() if counts['up'] > counts['down']]

print("__RESULT__:")
print(json.dumps({'indices': more_up_indices, 'counts': results}))"""

env_args = {'var_function-call-7458028202963988006': ['index_info'], 'var_function-call-7458028202963985611': ['index_trade'], 'var_function-call-14921271989771260256': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14921271989771262141': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-3554815193617154133': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-12337040612068561019': 'file_storage/function-call-12337040612068561019.json', 'var_function-call-17069154687632134843': ['IXIC'], 'var_function-call-7503463756106600599': {'GSPTSE': {'up': 37, 'down': 46}, 'IXIC': {'up': 51, 'down': 40}, 'NYA': {'up': 49, 'down': 57}}, 'var_function-call-10561216358518631910': [{'count_star()': '251'}], 'var_function-call-10561216358518629099': [{'count_star()': '106'}], 'var_function-call-1247034014981704610': [{'Date': 'January 02, 2018 at 12:00 AM'}, {'Date': 'January 03, 2018 at 12:00 AM'}, {'Date': 'January 08, 2018 at 12:00 AM'}, {'Date': '2018-01-09 00:00:00'}, {'Date': 'January 12, 2018 at 12:00 AM'}], 'var_function-call-300034308587137483': 'file_storage/function-call-300034308587137483.json'}

exec(code, env_args)
