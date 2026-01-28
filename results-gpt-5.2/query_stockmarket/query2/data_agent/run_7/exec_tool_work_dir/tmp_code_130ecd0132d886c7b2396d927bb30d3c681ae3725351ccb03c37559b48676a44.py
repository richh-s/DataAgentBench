code = """import json
path = var_call_kBDXU6MJ9TW2Y1JhZyEOJbWu
with open(path,'r') as f:
    d = json.load(f)
# take first 10 symbols from first batch for test
sym = d['batches'][0][:10]
selects = []
for s in sym:
    selects.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
q = " UNION ALL ".join(selects)
print('__RESULT__:')
print(json.dumps({'query': q}))"""

env_args = {'var_call_7un3cbfUYFXu1BEzO9lTedgP': ['stockinfo'], 'var_call_xPgeMOXLTvmuFt8SHsxsB5Pb': 'file_storage/call_xPgeMOXLTvmuFt8SHsxsB5Pb.json', 'var_call_IIzelB2aZqN6Arw9eX5Xcqia': 'file_storage/call_IIzelB2aZqN6Arw9eX5Xcqia.json', 'var_call_kBDXU6MJ9TW2Y1JhZyEOJbWu': 'file_storage/call_kBDXU6MJ9TW2Y1JhZyEOJbWu.json'}

exec(code, env_args)
