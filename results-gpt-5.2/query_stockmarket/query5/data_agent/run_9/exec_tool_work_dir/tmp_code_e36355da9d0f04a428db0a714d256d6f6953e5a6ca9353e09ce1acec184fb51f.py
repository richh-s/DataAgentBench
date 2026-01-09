code = """import json, pandas as pd
from pathlib import Path

p = Path(var_call_RsghL4UroeHSwUjPcoLqnafK)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
# keep distinct symbols
symbols = sorted(df['Symbol'].dropna().unique().tolist())
# chunk to avoid huge SQL IN
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]
print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'chunks': chunks[:5], 'n_chunks': len(chunks)}))"""

env_args = {'var_call_RsghL4UroeHSwUjPcoLqnafK': 'file_storage/call_RsghL4UroeHSwUjPcoLqnafK.json'}

exec(code, env_args)
