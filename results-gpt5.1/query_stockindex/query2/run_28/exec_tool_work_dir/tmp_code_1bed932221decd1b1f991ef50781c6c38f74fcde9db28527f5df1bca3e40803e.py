code = """import json, pandas as pd
import os

# Load full 2018 data from file
path = var_call_1Ufi7jevXO0LLyHLisPtpYJY
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric types
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Define North American indices based on domain knowledge
north_american_indices = ['IXIC', 'NYA', 'GSPTSE']  # Nasdaq Composite, NYSE Composite, S&P/TSX Composite

na_df = df[df['Index'].isin(north_american_indices)].copy()

# Classify up and down days
na_df['up'] = na_df['Close'] > na_df['Open']
na_df['down'] = na_df['Close'] < na_df['Open']

summary = na_df.groupby('Index').agg(up_days=('up', 'sum'), down_days=('down', 'sum')).reset_index()

# Determine which indices had more up days than down days
summary['more_up_than_down'] = summary['up_days'] > summary['down_days']

result_indices = summary[summary['more_up_than_down']]['Index'].tolist()

result = {
    'summary': summary.to_dict(orient='records'),
    'indices_with_more_up_than_down': result_indices
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_cxsGRxGieMQ0RWrBnaNjZRPj': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_1Ufi7jevXO0LLyHLisPtpYJY': 'file_storage/call_1Ufi7jevXO0LLyHLisPtpYJY.json'}

exec(code, env_args)
