code = """import json, pandas as pd

path = var_call_JG1SRJTfcHIaJfhWkTPymFWc
with open(path, 'r') as f:
    etf_rows = json.load(f)

tickers = [row['Symbol'] for row in etf_rows]

queries = []
for s in tickers:
    q = f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM '{s}' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31';"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'queries': queries[:50]}))"""

env_args = {'var_call_JG1SRJTfcHIaJfhWkTPymFWc': 'file_storage/call_JG1SRJTfcHIaJfhWkTPymFWc.json', 'var_call_r0Dx6vSUMGj6SqnnQA52P7rD': 'file_storage/call_r0Dx6vSUMGj6SqnnQA52P7rD.json'}

exec(code, env_args)
