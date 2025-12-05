code = """import json, pandas as pd

info_file = var_call_WqcjZhoCvOus899JUXVR4snj
with open(info_file) as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

r1 = var_call_kjUjfMYpEhX8kn5ekrdGvZi5
r2 = var_call_ZXH1Gp6NtNfT8mAm8LwJ67U1

r1_df = pd.DataFrame(r1)
r2_df = pd.DataFrame(r2)
all_df = pd.concat([r1_df, r2_df], ignore_index=True)
all_df['n_days'] = all_df['n_days'].astype(int)

merged = all_df.merge(info_df, left_on='symbol', right_on='Symbol', how='left')
merged = merged.sort_values('n_days', ascending=False).head(5)

result = merged[['symbol', 'Company Description', 'n_days']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HxfL9asL0ayhMz0cskk4oPHV': 'file_storage/call_HxfL9asL0ayhMz0cskk4oPHV.json', 'var_call_WqcjZhoCvOus899JUXVR4snj': 'file_storage/call_WqcjZhoCvOus899JUXVR4snj.json', 'var_call_xOlXNMA8ThZYIi8LjM6vqCiZ': 'file_storage/call_xOlXNMA8ThZYIi8LjM6vqCiZ.json', 'var_call_kjUjfMYpEhX8kn5ekrdGvZi5': [{'symbol': 'CORV', 'n_days': '10'}, {'symbol': 'CEMI', 'n_days': '3'}, {'symbol': 'IDEX', 'n_days': '15'}, {'symbol': 'FTFT', 'n_days': '21'}, {'symbol': 'BKYI', 'n_days': '16'}, {'symbol': 'IOTS', 'n_days': '1'}, {'symbol': 'BOSC', 'n_days': '3'}, {'symbol': 'CPAH', 'n_days': '16'}, {'symbol': 'CBAT', 'n_days': '23'}, {'symbol': 'DZSI', 'n_days': '1'}, {'symbol': 'BHAT', 'n_days': '10'}, {'symbol': 'HRTX', 'n_days': '1'}, {'symbol': 'FAMI', 'n_days': '23'}, {'symbol': 'BWEN', 'n_days': '5'}, {'symbol': 'HQI', 'n_days': '2'}, {'symbol': 'EYEG', 'n_days': '18'}, {'symbol': 'FNCB', 'n_days': '1'}, {'symbol': 'CCCL', 'n_days': '13'}, {'symbol': 'AGMH', 'n_days': '13'}, {'symbol': 'MCEP', 'n_days': '14'}, {'symbol': 'CLRB', 'n_days': '14'}, {'symbol': 'APEX', 'n_days': '15'}, {'symbol': 'GLG', 'n_days': '42'}, {'symbol': 'BIOC', 'n_days': '21'}], 'var_call_ZXH1Gp6NtNfT8mAm8LwJ67U1': [{'symbol': 'NXTD', 'n_days': '15'}, {'symbol': 'SNSS', 'n_days': '32'}, {'symbol': 'MNPR', 'n_days': '4'}, {'symbol': 'PLIN', 'n_days': '1'}, {'symbol': 'WHLR', 'n_days': '15'}, {'symbol': 'SES', 'n_days': '51'}, {'symbol': 'XBIOW', 'n_days': '7'}, {'symbol': 'PEIX', 'n_days': '12'}, {'symbol': 'NVEE', 'n_days': '1'}, {'symbol': 'PBTS', 'n_days': '8'}, {'symbol': 'TMSR', 'n_days': '40'}, {'symbol': 'SHSP', 'n_days': '1'}, {'symbol': 'VERB', 'n_days': '38'}, {'symbol': 'VTIQW', 'n_days': '6'}, {'symbol': 'MLND', 'n_days': '3'}, {'symbol': 'PFIE', 'n_days': '2'}, {'symbol': 'MMAC', 'n_days': '1'}, {'symbol': 'PECK', 'n_days': '19'}, {'symbol': 'VMD', 'n_days': '1'}, {'symbol': 'QRHC', 'n_days': '3'}, {'symbol': 'VVPR', 'n_days': '14'}, {'symbol': 'ORGO', 'n_days': '15'}, {'symbol': 'XPEL', 'n_days': '4'}, {'symbol': 'OPTT', 'n_days': '12'}, {'symbol': 'OTEL', 'n_days': '1'}, {'symbol': 'SSNT', 'n_days': '11'}]}

exec(code, env_args)
