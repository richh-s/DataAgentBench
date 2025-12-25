code = """import json, pandas as pd

file_path = var_call_pH9slHgiCfLZZgQFW0Kcenpz
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

north_american_indices = ['NYA', 'IXIC', 'GSPTSE']

mask_na = df['Index'].isin(north_american_indices)

df_na = df[mask_na].copy()

for col in ['Open', 'Close']:
    df_na[col] = pd.to_numeric(df_na[col], errors='coerce')

up_down_counts = df_na.groupby('Index').apply(lambda g: pd.Series({
    'up_days': (g['Close'] > g['Open']).sum(),
    'down_days': (g['Close'] < g['Open']).sum()
})).reset_index()

indices_more_up = up_down_counts[up_down_counts['up_days'] > up_down_counts['down_days']]['Index'].tolist()

result = {
    'north_american_indices_evaluated': north_american_indices,
    'up_down_counts': up_down_counts.to_dict(orient='records'),
    'indices_with_more_up_than_down': indices_more_up
}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_gsKGDQdys4UH71QaHAEbUxck': ['index_info'], 'var_call_a8kWn3vg3bIoMf3zE0gYawaW': ['index_trade'], 'var_call_RtFKBF0Vx8WFAaNXEk2fkSnA': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_U6y3uWZ1O206FBsGy17a7pbP': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_pH9slHgiCfLZZgQFW0Kcenpz': 'file_storage/call_pH9slHgiCfLZZgQFW0Kcenpz.json'}

exec(code, env_args)
