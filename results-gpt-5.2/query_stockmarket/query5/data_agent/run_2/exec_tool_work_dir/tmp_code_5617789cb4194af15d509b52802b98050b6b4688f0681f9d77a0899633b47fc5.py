code = """import json
from pathlib import Path

# load metadata
recs = json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text())
syms_u=[]
companies={}
seen=set()
for r in recs:
    s=r['Symbol']
    if s not in seen:
        seen.add(s)
        syms_u.append(s)
        companies[s]=r['company_name']

reserved={'ELSE'}

# build per-symbol count queries
queries=[]
for s in syms_u:
    tbl = '"'+s+'"' if s in reserved else s
    q = f"SELECT '{s}' AS sym, COUNT(*)::BIGINT AS days_gt_20pct FROM {tbl} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low)/Low > 0.2"
    queries.append(q)

final_query = "\nUNION ALL\n".join(queries) + "\nORDER BY days_gt_20pct DESC, sym\nLIMIT 5;"

print('__RESULT__:')
print(json.dumps({'len_query': len(final_query)}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json', 'var_call_qmvstUsIbQmydnQOvRNocUXo': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_UHf6AKuOZMUNM7MqQgpMEfM2': 'file_storage/call_UHf6AKuOZMUNM7MqQgpMEfM2.json', 'var_call_GvaE3pwA8TWwrYbr5F9SlGVG': {'n_intersection': 86, 'n_missing': 0, 'missing': []}, 'var_call_VhAOjKWEWGBjgDhzGC1mar3H': [{'sym': 'ELSE', 'days_gt_20pct': '0'}], 'var_call_vXneqB7g1ll43FEZY0oXkTdb': {'n_symbols': 86, 'needs_quote': ['ELSE']}, 'var_call_cHN0IHje9d5OpUL1NShRHTPf': {'missing_in_all': [], 'n_missing': 0}, 'var_call_Pe2kZagf02kauDjoNu9eh0Sl': [], 'var_call_lctcIB9AufRI10mD9iCXVn0i': {'has_MDCN': False, 'count_MDCN': 0}}

exec(code, env_args)
