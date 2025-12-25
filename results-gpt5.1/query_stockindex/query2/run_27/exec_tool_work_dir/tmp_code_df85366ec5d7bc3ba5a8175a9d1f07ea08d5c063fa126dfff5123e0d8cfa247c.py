code = """import json, pandas as pd
from pathlib import Path

# Load the full 2018 trades file
path = Path(var_call_Qr3eSueyTCVmn2LCOIkF0L06)
with path.open() as f:
    data = json.load(f)

df = pd.DataFrame(data)
# ensure numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Define North American indices based on domain knowledge
na_indices = ['NYA', 'IXIC', 'GSPTSE']  # New York Stock Exchange Composite, NASDAQ Composite, S&P/TSX Composite

na_df = df[df['Index'].isin(na_indices)].copy()

# Classify up/down days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result = summary.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_yBhMrqtqj5BDwBbJQ1rbkR4G': ['index_info'], 'var_call_lXA2UskqLq7rfcm3b7qavDap': ['index_trade'], 'var_call_NDLO3EztmVuGf0TjLkSWi76g': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_E9GNuB76R2Cl0eRzsSFRmHlo': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_Qr3eSueyTCVmn2LCOIkF0L06': 'file_storage/call_Qr3eSueyTCVmn2LCOIkF0L06.json'}

exec(code, env_args)
