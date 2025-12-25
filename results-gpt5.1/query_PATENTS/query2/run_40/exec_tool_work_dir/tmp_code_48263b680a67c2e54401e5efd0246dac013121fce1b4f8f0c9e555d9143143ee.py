code = """import json, pandas as pd

# Load CPC definitions
path_def = var_call_RQMkdOxbboHOoG5OYvHvc0bt
with open(path_def, 'r') as f:
    defs = json.load(f)

def_df = pd.DataFrame(defs)

info = var_call_FFS3PGc8EL6G8FijJ4PnNIhE

rows = []
for g in info['top_groups']:
    row = def_df[def_df['symbol'] == g]
    if not row.empty:
        title = row.iloc[0]['titleFull']
    else:
        title = None
    rows.append({'cpc_group_code': g, 'titleFull': title, 'best_year': 2019, 'ema': info['max_ema']})

print("__RESULT__:")
print(json.dumps(rows))"""

env_args = {'var_call_OE8GeDdgCCxwiYDzBSPeJ0QT': 'file_storage/call_OE8GeDdgCCxwiYDzBSPeJ0QT.json', 'var_call_RQMkdOxbboHOoG5OYvHvc0bt': 'file_storage/call_RQMkdOxbboHOoG5OYvHvc0bt.json', 'var_call_l6g45AcWqgP1cd1oMSNl4IFX': [{'group4': 'A24C', 'year': 2019, 'ema': 1.0}, {'group4': 'A43B', 'year': 2019, 'ema': 5.0}, {'group4': 'A61B', 'year': 2019, 'ema': 3.0}, {'group4': 'A61F', 'year': 2019, 'ema': 6.0}, {'group4': 'B23K', 'year': 2019, 'ema': 1.0}, {'group4': 'B29C', 'year': 2019, 'ema': 19.0}, {'group4': 'B29D', 'year': 2019, 'ema': 1.0}, {'group4': 'B41F', 'year': 2019, 'ema': 3.0}, {'group4': 'B60K', 'year': 2019, 'ema': 1.0}, {'group4': 'B60R', 'year': 2019, 'ema': 1.0}, {'group4': 'B60S', 'year': 2019, 'ema': 1.0}, {'group4': 'B60W', 'year': 2019, 'ema': 1.0}, {'group4': 'B63B', 'year': 2019, 'ema': 1.0}, {'group4': 'B64D', 'year': 2019, 'ema': 1.0}, {'group4': 'B66C', 'year': 2019, 'ema': 1.0}, {'group4': 'C04B', 'year': 2019, 'ema': 45.0}, {'group4': 'C09K', 'year': 2019, 'ema': 2.0}, {'group4': 'E02F', 'year': 2019, 'ema': 6.0}, {'group4': 'E05B', 'year': 2019, 'ema': 1.0}, {'group4': 'E21B', 'year': 2019, 'ema': 5.0}, {'group4': 'F01C', 'year': 2019, 'ema': 4.0}, {'group4': 'F02D', 'year': 2019, 'ema': 8.0}, {'group4': 'F02M', 'year': 2019, 'ema': 11.0}, {'group4': 'F02N', 'year': 2019, 'ema': 7.0}, {'group4': 'F04B', 'year': 2019, 'ema': 2.0}, {'group4': 'F04C', 'year': 2019, 'ema': 14.0}, {'group4': 'F16C', 'year': 2019, 'ema': 3.0}, {'group4': 'F16H', 'year': 2019, 'ema': 5.0}, {'group4': 'F23B', 'year': 2019, 'ema': 4.0}, {'group4': 'F23L', 'year': 2019, 'ema': 6.0}, {'group4': 'F23N', 'year': 2019, 'ema': 1.0}, {'group4': 'F24B', 'year': 2019, 'ema': 3.0}, {'group4': 'F41H', 'year': 2019, 'ema': 2.0}, {'group4': 'F42B', 'year': 2019, 'ema': 2.0}, {'group4': 'G01D', 'year': 2019, 'ema': 1.0}, {'group4': 'G02B', 'year': 2019, 'ema': 12.0}, {'group4': 'G07C', 'year': 2019, 'ema': 2.0}, {'group4': 'G08B', 'year': 2019, 'ema': 2.0}, {'group4': 'H01H', 'year': 2019, 'ema': 4.0}, {'group4': 'H01L', 'year': 2019, 'ema': 6.0}, {'group4': 'H01R', 'year': 2019, 'ema': 6.0}, {'group4': 'H04L', 'year': 2019, 'ema': 14.0}, {'group4': 'H04W', 'year': 2019, 'ema': 22.0}, {'group4': 'Y02D', 'year': 2019, 'ema': 2.0}, {'group4': 'Y02E', 'year': 2019, 'ema': 1.0}, {'group4': 'Y02T', 'year': 2019, 'ema': 3.0}, {'group4': 'Y10T', 'year': 2019, 'ema': 2.0}], 'var_call_FFS3PGc8EL6G8FijJ4PnNIhE': {'max_ema': 45.0, 'top_groups': ['C04B']}}

exec(code, env_args)
