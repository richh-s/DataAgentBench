code = """import json, pandas as pd
from pathlib import Path

symbols_file = Path(var_call_JT9wRKppRCFiUq7xIv0teVUO)
symbols_data = json.loads(symbols_file.read_text())
syms = [r['Symbol'] for r in symbols_data]

chunks = [syms[i:i+50] for i in range(0, len(syms), 50)]

queries = []
for ch in chunks:
    in_list = ",".join("'"+s+"'" for s in ch)
    q = f"SELECT '{','.join(ch)}' as symbols_group;"
    queries.append(q)

result = json.dumps({'symbol_chunks': chunks})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_JcN1Ou73ZKJqPLgeDsuFWaK2': 'file_storage/call_JcN1Ou73ZKJqPLgeDsuFWaK2.json', 'var_call_JT9wRKppRCFiUq7xIv0teVUO': 'file_storage/call_JT9wRKppRCFiUq7xIv0teVUO.json'}

exec(code, env_args)
