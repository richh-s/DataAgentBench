code = """import json, pandas as pd

# load nyse non-etf symbols
nyse_path = var_call_Kl9WM852XoYXievB7ZKT9WmR
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_syms = set(nyse_df['Symbol'].astype(str))

# load available trade tables
trade_path = var_call_5uLgy0g3jtEOABnbcitc36CV
with open(trade_path, 'r') as f:
    tables = json.load(f)

tables_set = set(tables)
syms = sorted(list(nyse_syms.intersection(tables_set)))

# take a manageable batch size for SQL IN clause
chunks = [syms[i:i+250] for i in range(0, len(syms), 250)]

out = {
    'symbol_count': len(syms),
    'chunks': len(chunks),
    'first_chunk': chunks[0][:20] if chunks else []
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Kl9WM852XoYXievB7ZKT9WmR': 'file_storage/call_Kl9WM852XoYXievB7ZKT9WmR.json', 'var_call_5uLgy0g3jtEOABnbcitc36CV': 'file_storage/call_5uLgy0g3jtEOABnbcitc36CV.json'}

exec(code, env_args)
