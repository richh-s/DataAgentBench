code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_QfEHnHaqnTMGD3BoRNJfC5Uz)
records = json.loads(path.read_text())

tickers = [r['Symbol'] for r in records]

chunks = []
for t in tickers:
    chunks.append(f"SELECT '{t}' AS Symbol, Date, `Adj Close` FROM '{t}' WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND `Adj Close` > 200")

query = " UNION ALL ".join(chunks)

result = {'query': query}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QW2ABEy00Fd8ON6kot4HRoIN': 'file_storage/call_QW2ABEy00Fd8ON6kot4HRoIN.json', 'var_call_QfEHnHaqnTMGD3BoRNJfC5Uz': 'file_storage/call_QfEHnHaqnTMGD3BoRNJfC5Uz.json'}

exec(code, env_args)
