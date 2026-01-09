code = """import json
from pathlib import Path

# reload correct symbol list
recs = json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text())
syms=set(r['Symbol'] for r in recs)
check = ['MTP','OCC','OBLN','OFS','OESX','MESA','MDCN']

print('__RESULT__:')
print(json.dumps({c: (c in syms) for c in check}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json', 'var_call_qmvstUsIbQmydnQOvRNocUXo': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_UHf6AKuOZMUNM7MqQgpMEfM2': 'file_storage/call_UHf6AKuOZMUNM7MqQgpMEfM2.json', 'var_call_GvaE3pwA8TWwrYbr5F9SlGVG': {'n_intersection': 86, 'n_missing': 0, 'missing': []}, 'var_call_VhAOjKWEWGBjgDhzGC1mar3H': [{'sym': 'ELSE', 'days_gt_20pct': '0'}], 'var_call_vXneqB7g1ll43FEZY0oXkTdb': {'n_symbols': 86, 'needs_quote': ['ELSE']}, 'var_call_cHN0IHje9d5OpUL1NShRHTPf': {'missing_in_all': [], 'n_missing': 0}, 'var_call_Pe2kZagf02kauDjoNu9eh0Sl': [], 'var_call_lctcIB9AufRI10mD9iCXVn0i': {'has_MDCN': False, 'count_MDCN': 0}, 'var_call_5TXPYf0LLwkDEpB3SSeO6vWl': [], 'var_call_erVCzcwlYhuxfNcIXYPECkgf': {'has_MESA': False}, 'var_call_j0kIotXMZ1gduKkam7F8eHy5': {'MESA': False, 'MDCN': False, 'MTP': False, 'OCC': False, 'OBLN': False, 'OFS': False, 'OESX': False}}

exec(code, env_args)
