code = """import json, pandas as pd

path = var_call_JG1SRJTfcHIaJfhWkTPymFWc
with open(path, 'r') as f:
    etf_rows = json.load(f)

tickers = [row['Symbol'] for row in etf_rows]

chunks = []
for i in range(0, len(tickers), 200):
    chunk = tickers[i:i+200]
    symlist = ", ".join([f'"{s}"' for s in chunk])
    chunks.append(f"SELECT symbol, MAX(\"Adj Close\") AS max_adj_close FROM (SELECT '{s}' AS symbol, \"Adj Close\" FROM '{s}' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31') WHERE max_adj_close > 200" for s in chunk)

print('__RESULT__:')
print(json.dumps({'dummy': True}))"""

env_args = {'var_call_JG1SRJTfcHIaJfhWkTPymFWc': 'file_storage/call_JG1SRJTfcHIaJfhWkTPymFWc.json', 'var_call_r0Dx6vSUMGj6SqnnQA52P7rD': 'file_storage/call_r0Dx6vSUMGj6SqnnQA52P7rD.json'}

exec(code, env_args)
