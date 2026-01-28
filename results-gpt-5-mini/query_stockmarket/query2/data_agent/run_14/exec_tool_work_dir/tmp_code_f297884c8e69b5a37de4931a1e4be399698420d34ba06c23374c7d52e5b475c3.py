code = """import json
p = var_call_Ei7SonmzvtHgGhe1CelFJMWL
with open(p,'r') as f:
    data = json.load(f)
sql = data['sql']
# Instead of splitting the giant SQL, reconstruct from the tickers by parsing the SELECT patterns
# We'll extract tickers from the SQL using a simple parse
parts = sql.split(" UNION ALL ")
tickers = []
for part in parts:
    # format: SELECT 'TICK' AS Symbol FROM "TICK" WHERE ...
    try:
        start = part.index("SELECT '")+8
        end = part.index("' AS Symbol")
        tick = part[start:end]
        tickers.append(tick)
    except Exception:
        pass
# create chunks of 100
chunks = [tickers[i:i+100] for i in range(0,len(tickers),100)]
DQ = '"'
chunk_sqls = []
for chunk in chunks:
    parts = [f"SELECT '{t}' AS Symbol FROM {DQ}{t}{DQ} WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND {DQ}Adj Close{DQ} > 200 LIMIT 1" for t in chunk]
    chunk_sqls.append(" UNION ALL ".join(parts) + ";")
out = {'num_chunks': len(chunk_sqls), 'chunk_sqls': chunk_sqls}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_742tOB6D3hBc8NEwfWPDvAKw': 'file_storage/call_742tOB6D3hBc8NEwfWPDvAKw.json', 'var_call_1SUoYEWvXREyq9D4xOEDzXpl': 'file_storage/call_1SUoYEWvXREyq9D4xOEDzXpl.json', 'var_call_Ei7SonmzvtHgGhe1CelFJMWL': 'file_storage/call_Ei7SonmzvtHgGhe1CelFJMWL.json'}

exec(code, env_args)
