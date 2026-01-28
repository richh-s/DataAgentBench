code = """import json, pandas as pd

sym_path = var_call_tw1ITfOp97oQbfqVeKzARqzi
with open(sym_path,'r') as f:
    symrecs = json.load(f)
df_sym = pd.DataFrame(symrecs)

trade_path = var_call_5rrCVPu8sti9lypppss1B3Br
with open(trade_path,'r') as f:
    tabrecs = json.load(f)
df_tabs = pd.DataFrame(tabrecs)

symbols = sorted(set(df_sym['Symbol']).intersection(set(df_tabs['name'])))

parts = []
for s in symbols:
    q = 'SELECT \'{sym}\' AS Symbol, ' \
        'SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, ' \
        'SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days ' \
        'FROM "{sym}" WHERE Date >= \'2017-01-01\' AND Date < \'2018-01-01\''
    parts.append(q.format(sym=s))

union_sql = '\nUNION ALL\n'.join(parts)
final_sql = 'WITH counts AS (\n{u}\n) SELECT * FROM counts'.format(u=union_sql)

print('__RESULT__:')
print(json.dumps({'symbols_n': len(symbols), 'sql_len': len(final_sql), 'sql_preview': final_sql[:2000]}))"""

env_args = {'var_call_MIfIdCZXA2HzZYAVj8h4hV89': ['stockinfo'], 'var_call_tw1ITfOp97oQbfqVeKzARqzi': 'file_storage/call_tw1ITfOp97oQbfqVeKzARqzi.json', 'var_call_5rrCVPu8sti9lypppss1B3Br': 'file_storage/call_5rrCVPu8sti9lypppss1B3Br.json'}

exec(code, env_args)
