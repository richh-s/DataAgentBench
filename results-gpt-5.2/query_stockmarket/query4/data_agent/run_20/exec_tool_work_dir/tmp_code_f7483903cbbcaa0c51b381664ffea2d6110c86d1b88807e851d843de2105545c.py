code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_NI0trbOoYA9FdfK8rJaJwdX1)
recs = json.loads(path.read_text())
df = pd.DataFrame(recs)
syms = sorted(df['Symbol'].dropna().unique().tolist())
# create SQL list
sql_list = ','.join(["'"+s.replace("'","''")+"'" for s in syms])
print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'sql_in_list': sql_list[:9000], 'sql_in_list_len': len(sql_list)}))"""

env_args = {'var_call_NI0trbOoYA9FdfK8rJaJwdX1': 'file_storage/call_NI0trbOoYA9FdfK8rJaJwdX1.json'}

exec(code, env_args)
