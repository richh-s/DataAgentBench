code = """import json
from pathlib import Path

recs = json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text())
syms = [r['Symbol'] for r in recs]
seen=set(); syms_u=[]
for s in syms:
    if s not in seen:
        seen.add(s); syms_u.append(s)

reserved={'ELSE'}
selects=[]
for s in syms_u:
    tbl = '"' + s + '"' if s in reserved else s
    selects.append(f"SELECT '{s}' AS sym, High, Low FROM {tbl} WHERE Date >= '2019-01-01' AND Date < '2020-01-01'")

union_sql = "\nUNION ALL ".join(selects)
query = f"SELECT sym, SUM(CASE WHEN Low > 0 AND (High - Low) / Low > 0.2 THEN 1 ELSE 0 END) AS days_gt_20pct FROM (\n{union_sql}\n) t GROUP BY sym ORDER BY days_gt_20pct DESC, sym LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'len_query': len(query), 'query_preview': query[:600]}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json', 'var_call_qmvstUsIbQmydnQOvRNocUXo': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_UHf6AKuOZMUNM7MqQgpMEfM2': 'file_storage/call_UHf6AKuOZMUNM7MqQgpMEfM2.json', 'var_call_GvaE3pwA8TWwrYbr5F9SlGVG': {'n_intersection': 86, 'n_missing': 0, 'missing': []}, 'var_call_VhAOjKWEWGBjgDhzGC1mar3H': [{'sym': 'ELSE', 'days_gt_20pct': '0'}], 'var_call_vXneqB7g1ll43FEZY0oXkTdb': {'n_symbols': 86, 'needs_quote': ['ELSE']}, 'var_call_cHN0IHje9d5OpUL1NShRHTPf': {'missing_in_all': [], 'n_missing': 0}, 'var_call_Pe2kZagf02kauDjoNu9eh0Sl': [], 'var_call_lctcIB9AufRI10mD9iCXVn0i': {'has_MDCN': False, 'count_MDCN': 0}}

exec(code, env_args)
