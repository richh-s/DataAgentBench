code = """import json
from pathlib import Path

records = json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text())
syms = [r['Symbol'] for r in records]
# unique preserve order
seen=set(); syms_u=[]
for s in syms:
    if s not in seen:
        seen.add(s); syms_u.append(s)

all_tables = set(json.loads(Path(var_call_UHf6AKuOZMUNM7MqQgpMEfM2).read_text()))
missing_in_all = [s for s in syms_u if s not in all_tables]

print('__RESULT__:')
print(json.dumps({'missing_in_all': missing_in_all, 'n_missing': len(missing_in_all)}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json', 'var_call_qmvstUsIbQmydnQOvRNocUXo': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_UHf6AKuOZMUNM7MqQgpMEfM2': 'file_storage/call_UHf6AKuOZMUNM7MqQgpMEfM2.json', 'var_call_GvaE3pwA8TWwrYbr5F9SlGVG': {'n_intersection': 86, 'n_missing': 0, 'missing': []}, 'var_call_VhAOjKWEWGBjgDhzGC1mar3H': [{'sym': 'ELSE', 'days_gt_20pct': '0'}], 'var_call_vXneqB7g1ll43FEZY0oXkTdb': {'n_symbols': 86, 'needs_quote': ['ELSE']}}

exec(code, env_args)
