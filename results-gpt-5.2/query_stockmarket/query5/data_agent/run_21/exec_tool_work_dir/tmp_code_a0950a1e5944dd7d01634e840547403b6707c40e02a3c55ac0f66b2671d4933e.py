code = """import json, pandas as pd

# load full stock list
path = var_call_JhJLtl5G4JCIM5ycQaLBGC65
with open(path, 'r') as f:
    symbols = json.load(f)
df = pd.DataFrame(symbols)
# keep unique symbols
syms = sorted(df['Symbol'].dropna().unique().tolist())

# emit list for next step
out = json.dumps({'symbols': syms, 'n': len(syms)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_JhJLtl5G4JCIM5ycQaLBGC65': 'file_storage/call_JhJLtl5G4JCIM5ycQaLBGC65.json'}

exec(code, env_args)
