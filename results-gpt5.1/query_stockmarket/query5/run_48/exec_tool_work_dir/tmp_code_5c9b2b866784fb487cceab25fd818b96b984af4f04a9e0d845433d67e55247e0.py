code = """import json
import itertools
# load stockinfo S-market NASDAQ symbols
path = var_call_PEMKqV0PJTYrTofy7XDchhIU
with open(path,'r') as f:
    records = json.load(f)
syms_cap = [r['Symbol'] for r in records]
# build DuckDB query to count days in 2019 with (High-Low)/Low>0.2 for each symbol
parts = []
for s in syms_cap:
    parts.append(f"SELECT '{s}' AS Symbol, COUNT(*) AS cnt FROM '{s}' WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low>0 AND (High - Low)/Low > 0.2")
union_query = " UNION ALL ".join(parts)
final_query = "SELECT Symbol, cnt FROM (" + union_query + ") ORDER BY cnt DESC LIMIT 5;"
result = json.dumps({'query': final_query})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_4kb01ff102CyxXL5vAd4eflj': 'file_storage/call_4kb01ff102CyxXL5vAd4eflj.json', 'var_call_PEMKqV0PJTYrTofy7XDchhIU': 'file_storage/call_PEMKqV0PJTYrTofy7XDchhIU.json', 'var_call_6A0MgoOAF9T4eC2OqT4uX2FG': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}

exec(code, env_args)
