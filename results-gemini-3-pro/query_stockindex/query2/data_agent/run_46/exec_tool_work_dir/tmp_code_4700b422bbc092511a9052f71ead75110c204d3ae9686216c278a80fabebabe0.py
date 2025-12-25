code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15978951560470387645'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert Date to datetime, handling mixed formats
# The formats seen:
# "December 31, 1965 at 12:00 AM"
# "03 Jan 1966, 00:00"
# "1966-01-04 00:00:00"
# "January 06, 1966 at 12:00 AM"
# pd.to_datetime is usually smart enough.
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=False)

# Filter for 2018
df_2018 = df[df['Date'].dt.year == 2018].copy()

# Ensure Open and Close are floats
df_2018['Open'] = pd.to_numeric(df_2018['Open'])
df_2018['Close'] = pd.to_numeric(df_2018['Close'])

# Calculate Up/Down
# Up day: Close > Open
# Down day: Close < Open
# Tie: Ignored? Question asks "more up days than down days". Ties don't count towards either.

results = []
indices = df_2018['Index'].unique()

for idx in indices:
    idx_data = df_2018[df_2018['Index'] == idx]
    up_days = (idx_data['Close'] > idx_data['Open']).sum()
    down_days = (idx_data['Close'] < idx_data['Open']).sum()
    
    results.append({
        "Index": idx,
        "Up": int(up_days),
        "Down": int(down_days),
        "MoreUp": bool(up_days > down_days)
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7906458278193779595': ['index_info'], 'var_function-call-7906458278193780460': ['index_trade'], 'var_function-call-2153530162801775751': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-2153530162801777142': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14586654838157138862': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}], 'var_function-call-10126594470247231683': [{'Date': 'December 31, 1965 at 12:00 AM'}, {'Date': '03 Jan 1966, 00:00'}, {'Date': '1966-01-04 00:00:00'}, {'Date': '05 Jan 1966, 00:00'}, {'Date': 'January 06, 1966 at 12:00 AM'}], 'var_function-call-11588212315972381927': [{'count_star()': '37163'}], 'var_function-call-15978951560470387645': 'file_storage/function-call-15978951560470387645.json'}

exec(code, env_args)
