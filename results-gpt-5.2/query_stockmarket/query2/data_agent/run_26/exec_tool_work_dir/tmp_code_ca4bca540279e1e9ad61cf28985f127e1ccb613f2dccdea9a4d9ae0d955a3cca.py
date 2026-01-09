code = """import json

arca_path = var_call_dicekK1CadjdqBVoQN5mEwi3
with open(arca_path, 'r') as f:
    arca = json.load(f)
arca_syms = sorted({r['Symbol'] for r in arca if r.get('Symbol')})

trade_path = var_call_jSoK13w4Qjxh2skFCII7xkeM
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

syms = [s for s in arca_syms if s in trade_tables]

parts = []
for s in syms:
    parts.append("SELECT '{sym}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))

chunk_size = 250
chunks = [" UNION ALL ".join(parts[i:i+chunk_size]) for i in range(0, len(parts), chunk_size)]

out = {'chunks': chunks, 'n_chunks': len(chunks), 'n_symbols': len(syms)}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_dicekK1CadjdqBVoQN5mEwi3': 'file_storage/call_dicekK1CadjdqBVoQN5mEwi3.json', 'var_call_jSoK13w4Qjxh2skFCII7xkeM': 'file_storage/call_jSoK13w4Qjxh2skFCII7xkeM.json'}

exec(code, env_args)
