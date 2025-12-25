code = """import json, pandas as pd
from pathlib import Path

symbols = json.loads(Path(var_call_3CyaGEN6NIN9CXuI9ion3FSl).read_text())
meta = pd.read_json(var_call_BQxqSkOTGPacwhwwWSXyVAD3)
nyse_stocks = set(meta['Symbol'])

symbols_nyse = [s for s in symbols if s in nyse_stocks]

chunks = []
for sym in symbols_nyse:
    chunks.append(f"SELECT '{sym}' AS Symbol, Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'")

union_query = " UNION ALL ".join(chunks) if chunks else ""

result = {
  'symbols_nyse': symbols_nyse[:50],
  'needs_query': bool(union_query),
  'query_prefix': union_query[:1000]
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3CyaGEN6NIN9CXuI9ion3FSl': 'file_storage/call_3CyaGEN6NIN9CXuI9ion3FSl.json', 'var_call_BQxqSkOTGPacwhwwWSXyVAD3': 'file_storage/call_BQxqSkOTGPacwhwwWSXyVAD3.json'}

exec(code, env_args)
