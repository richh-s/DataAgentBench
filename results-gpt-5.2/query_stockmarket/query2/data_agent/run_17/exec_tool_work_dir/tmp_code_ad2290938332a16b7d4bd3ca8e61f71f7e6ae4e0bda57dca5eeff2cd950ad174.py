code = """import json

# load etf list
p = var_call_iOvFCGkDaV3qO2tUthxmFcC2
if isinstance(p, str):
    with open(p,'r') as f:
        etfs = json.load(f)
else:
    etfs = p

# map symbol->description
sym_desc = {r['Symbol']: r.get('company_description') for r in etfs}

# load trade tables from information_schema result
p2 = var_call_yb7NMQCKe3VpgSr6Ll3fPIXi
if isinstance(p2, str):
    with open(p2,'r') as f:
        tables = json.load(f)
else:
    tables = p2
trade_set = set([r['table_name'] for r in tables])

syms = sorted([s for s in sym_desc.keys() if s in trade_set])

# build CTE values
values_sql = ','.join(["('"+s.replace("'","''")+"')" for s in syms])

print('__RESULT__:')
print(json.dumps({'values_sql_len': len(values_sql), 'n_syms': len(syms), 'values_sql_preview': values_sql[:200]}))"""

env_args = {'var_call_iOvFCGkDaV3qO2tUthxmFcC2': 'file_storage/call_iOvFCGkDaV3qO2tUthxmFcC2.json', 'var_call_PJXWtX99zzhlp0cs6kTsGt48': 'file_storage/call_PJXWtX99zzhlp0cs6kTsGt48.json', 'var_call_RectN9RWDgCsxQrjTdI0Ybp0': {'n_syms': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_yb7NMQCKe3VpgSr6Ll3fPIXi': 'file_storage/call_yb7NMQCKe3VpgSr6Ll3fPIXi.json', 'var_call_hZy9NLepwdEqLRpFMwlmH9jt': [{'Symbol': 'AAAU'}]}

exec(code, env_args)
