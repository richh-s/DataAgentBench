code = """import json, pandas as pd

# load stockinfo query results
if isinstance(var_call_9x43jhvltlIk3SV75Wkfhm1D, str):
    with open(var_call_9x43jhvltlIk3SV75Wkfhm1D, 'r') as f:
        info = json.load(f)
else:
    info = var_call_9x43jhvltlIk3SV75Wkfhm1D

df_info = pd.DataFrame(info)
nyse_syms = set(df_info['Symbol'].dropna().astype(str))

# load available trade tables
if isinstance(var_call_2AhcoWPmgTbeg1mwSm0bl5Iu, str):
    with open(var_call_2AhcoWPmgTbeg1mwSm0bl5Iu, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = var_call_2AhcoWPmgTbeg1mwSm0bl5Iu

trade_set = set(trade_tables)
syms = sorted(list(nyse_syms & trade_set))

chunks = []
for sym in syms:
    chunks.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM \"{sym}\" WHERE Date>='2017-01-01' AND Date<='2017-12-31'")

chunk_size = 200
chunk_queries = [" UNION ALL ".join(chunks[i:i+chunk_size]) for i in range(0, len(chunks), chunk_size)]

out = json.dumps({"n_symbols": len(syms), "n_chunks": len(chunk_queries), "chunk_queries": chunk_queries})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_2AhcoWPmgTbeg1mwSm0bl5Iu': 'file_storage/call_2AhcoWPmgTbeg1mwSm0bl5Iu.json', 'var_call_9x43jhvltlIk3SV75Wkfhm1D': 'file_storage/call_9x43jhvltlIk3SV75Wkfhm1D.json'}

exec(code, env_args)
