code = """import json, pandas as pd

info_src = var_call_Km4pD3Vt20x9IJsbZQuKm7E6
if isinstance(info_src, str):
    with open(info_src, 'r') as f:
        info = json.load(f)
else:
    info = info_src

tables_src = var_call_e3WXalL5luM4t2iSV4nYQGQX
if isinstance(tables_src, str):
    with open(tables_src, 'r') as f:
        tables = json.load(f)
else:
    tables = tables_src

info_df = pd.DataFrame(info)
symbols = sorted(set(info_df['Symbol']).intersection(set(tables)))

# return list of symbols; we'll query iteratively to avoid huge UNION
print('__RESULT__:')
print(json.dumps(symbols))"""

env_args = {'var_call_Km4pD3Vt20x9IJsbZQuKm7E6': 'file_storage/call_Km4pD3Vt20x9IJsbZQuKm7E6.json', 'var_call_e3WXalL5luM4t2iSV4nYQGQX': 'file_storage/call_e3WXalL5luM4t2iSV4nYQGQX.json'}

exec(code, env_args)
