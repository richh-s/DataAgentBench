code = """import json, pandas as pd

path = var_call_KdaHpRCA2NJFnz1J07kO20uX
with open(path) as f:
    etfs = json.load(f)

df = pd.DataFrame(etfs)
syms = df['Symbol'].tolist()

chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]

queries = []
for chunk in chunks:
    in_list = ','.join([f'"{s}"' for s in chunk])
    q = f"SELECT table_name FROM information_schema.tables WHERE table_name IN ({in_list});"
    queries.append(q)

result = {'chunks': queries}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KdaHpRCA2NJFnz1J07kO20uX': 'file_storage/call_KdaHpRCA2NJFnz1J07kO20uX.json', 'var_call_mtyr7uNex6ZyhGNodqngCSIu': 'file_storage/call_mtyr7uNex6ZyhGNodqngCSIu.json'}

exec(code, env_args)
