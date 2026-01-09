code = """import json, pandas as pd
from pathlib import Path
p = Path(var_call_N3ewuvocGALxkFTjRsg7FEji)
recs = json.loads(p.read_text())
df = pd.DataFrame(recs)
syms = df['Symbol'].dropna().unique().tolist()
company = dict(zip(df['Symbol'], df['company_name']))
# chunk symbols for SQL IN clauses
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
queries = []
for ch in chunks:
    in_list = ','.join(["'%s'" % s.replace("'","''") for s in ch])
    queries.append(f"SELECT table_name AS Symbol FROM information_schema.tables WHERE table_schema='main' AND table_name IN ({in_list});")
out = {'chunks': queries, 'company': company, 'n_symbols': len(syms)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_N3ewuvocGALxkFTjRsg7FEji': 'file_storage/call_N3ewuvocGALxkFTjRsg7FEji.json'}

exec(code, env_args)
