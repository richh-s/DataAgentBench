code = """import pandas as pd
import json

# Load the data
with open(locals()['var_function-call-1009030970064699223'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# We use pd.to_datetime with errors='coerce' to handle mixed formats
# It's usually smart enough.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for 2018
df_2018 = df[df['Date'].dt.year == 2018].copy()

# Ensure numeric columns
df_2018['Open'] = pd.to_numeric(df_2018['Open'])
df_2018['Close'] = pd.to_numeric(df_2018['Close'])

# Calculate Up/Down days
results = {}
indices = df_2018['Index'].unique()

for idx in indices:
    idx_data = df_2018[df_2018['Index'] == idx]
    up_days = (idx_data['Close'] > idx_data['Open']).sum()
    down_days = (idx_data['Close'] < idx_data['Open']).sum()
    results[idx] = {'Up': int(up_days), 'Down': int(down_days)}

# Filter for North American indices with Up > Down
# Identified North American Indices: NYA, IXIC, GSPTSE
na_indices = ['NYA', 'IXIC', 'GSPTSE']
final_list = []
for idx in na_indices:
    if idx in results:
        if results[idx]['Up'] > results[idx]['Down']:
            final_list.append(idx)

# Output for debugging
print("__RESULT__:")
print(json.dumps({"results": results, "answer": final_list}))"""

env_args = {'var_function-call-17898506791791866104': ['index_info'], 'var_function-call-17898506791791866835': ['index_trade'], 'var_function-call-14258782796877357527': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-6594707714779667610': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': 'IXIC'}], 'var_function-call-14395744273078527869': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-14488013966622613953': [{'Index': 'IXIC', 'UpDays': '44.0', 'DownDays': '31.0'}, {'Index': 'GSPTSE', 'UpDays': '44.0', 'DownDays': '41.0'}, {'Index': 'NYA', 'UpDays': '37.0', 'DownDays': '42.0'}], 'var_function-call-10159749278599534661': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-1009030970064699223': 'file_storage/function-call-1009030970064699223.json'}

exec(code, env_args)
