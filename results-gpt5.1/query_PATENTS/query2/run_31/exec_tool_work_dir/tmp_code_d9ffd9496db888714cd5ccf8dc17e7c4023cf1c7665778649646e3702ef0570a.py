code = """import json, pandas as pd

best = var_call_rPitCxMVhbGcFEMKK8P84Dix

# Load CPC level 4 definitions
with open(var_call_s3DqhAJjxPFAEIxAdE1Ba3Pz, 'r') as f:
    defs = json.load(f)

# Build dataframe
best_df = pd.DataFrame(best)
_defs = pd.DataFrame(defs)
_defs['symbol'] = _defs['symbol'].astype(str)

merged = best_df.merge(_defs[['symbol','titleFull']], left_on='group4', right_on='symbol', how='left')

# Find highest EMA overall
max_ema = merged['best_ema'].max()
top = merged[merged['best_ema'] == max_ema]

# Prepare result records
out = []
for _, row in top.iterrows():
    out.append({
        'CPC_group_code_level4': row['group4'],
        'titleFull': row.get('titleFull'),
        'best_year': int(row['best_year']),
        'best_exponential_moving_average_filings': row['best_ema']
    })

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_7dGfNYcAAcuxvDMSxEqR8sJz': 'file_storage/call_7dGfNYcAAcuxvDMSxEqR8sJz.json', 'var_call_s3DqhAJjxPFAEIxAdE1Ba3Pz': 'file_storage/call_s3DqhAJjxPFAEIxAdE1Ba3Pz.json', 'var_call_rPitCxMVhbGcFEMKK8P84Dix': [{'group4': 'A24', 'best_year': 2019, 'best_ema': 1}, {'group4': 'A43', 'best_year': 2019, 'best_ema': 5}, {'group4': 'A61', 'best_year': 2019, 'best_ema': 9}, {'group4': 'B23', 'best_year': 2019, 'best_ema': 1}, {'group4': 'B29', 'best_year': 2019, 'best_ema': 20}, {'group4': 'B41', 'best_year': 2019, 'best_ema': 3}, {'group4': 'B60', 'best_year': 2019, 'best_ema': 4}, {'group4': 'B63', 'best_year': 2019, 'best_ema': 1}, {'group4': 'B64', 'best_year': 2019, 'best_ema': 1}, {'group4': 'B66', 'best_year': 2019, 'best_ema': 1}, {'group4': 'C04', 'best_year': 2019, 'best_ema': 45}, {'group4': 'C09', 'best_year': 2019, 'best_ema': 2}, {'group4': 'E02', 'best_year': 2019, 'best_ema': 6}, {'group4': 'E05', 'best_year': 2019, 'best_ema': 1}, {'group4': 'E21', 'best_year': 2019, 'best_ema': 5}, {'group4': 'F01', 'best_year': 2019, 'best_ema': 4}, {'group4': 'F02', 'best_year': 2019, 'best_ema': 26}, {'group4': 'F04', 'best_year': 2019, 'best_ema': 16}, {'group4': 'F16', 'best_year': 2019, 'best_ema': 8}, {'group4': 'F23', 'best_year': 2019, 'best_ema': 11}, {'group4': 'F24', 'best_year': 2019, 'best_ema': 3}, {'group4': 'F41', 'best_year': 2019, 'best_ema': 2}, {'group4': 'F42', 'best_year': 2019, 'best_ema': 2}, {'group4': 'G01', 'best_year': 2019, 'best_ema': 1}, {'group4': 'G02', 'best_year': 2019, 'best_ema': 12}, {'group4': 'G07', 'best_year': 2019, 'best_ema': 2}, {'group4': 'G08', 'best_year': 2019, 'best_ema': 2}, {'group4': 'H01', 'best_year': 2019, 'best_ema': 16}, {'group4': 'H04', 'best_year': 2019, 'best_ema': 36}, {'group4': 'Y02', 'best_year': 2019, 'best_ema': 6}, {'group4': 'Y10', 'best_year': 2019, 'best_ema': 2}]}

exec(code, env_args)
