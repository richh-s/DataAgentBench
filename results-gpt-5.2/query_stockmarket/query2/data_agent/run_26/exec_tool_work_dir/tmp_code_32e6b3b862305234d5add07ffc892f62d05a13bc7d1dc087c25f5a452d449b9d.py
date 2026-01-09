code = """import json, pandas as pd

# load arca ETFs
arca_path = var_call_dicekK1CadjdqBVoQN5mEwi3
with open(arca_path, 'r') as f:
    arca = json.load(f)
arca_syms = sorted({r['Symbol'] for r in arca if r.get('Symbol')})

# load available trade tables
trade_path = var_call_jSoK13w4Qjxh2skFCII7xkeM
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

# keep those with price tables
syms = [s for s in arca_syms if s in trade_tables]

# build a single UNION ALL query to get max adj close in 2015 per symbol
parts = []
for s in syms:
    # quote table name in duckdb
    parts.append(f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# chunk to avoid overly large query strings
chunk_size = 300
chunks = [" UNION ALL ".join(parts[i:i+chunk_size]) for i in range(0, len(parts), chunk_size)]

out = {
    'symbols': syms,
    'chunks': chunks,
    'n_symbols': len(syms)
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dicekK1CadjdqBVoQN5mEwi3': 'file_storage/call_dicekK1CadjdqBVoQN5mEwi3.json', 'var_call_jSoK13w4Qjxh2skFCII7xkeM': 'file_storage/call_jSoK13w4Qjxh2skFCII7xkeM.json'}

exec(code, env_args)
