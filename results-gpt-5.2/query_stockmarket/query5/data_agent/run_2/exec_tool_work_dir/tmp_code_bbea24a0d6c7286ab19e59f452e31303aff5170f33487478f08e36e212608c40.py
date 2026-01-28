code = """import json
from pathlib import Path

syms_info = set(json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text())[i]['Symbol'] for i in range(len(json.loads(Path(var_call_ffAtFs2g1l61SFV6JTZqWbzh).read_text()))))
all_tables = set(json.loads(Path(var_call_UHf6AKuOZMUNM7MqQgpMEfM2).read_text()))
syms = sorted(list(syms_info & all_tables))
missing = sorted(list(syms_info - all_tables))

print('__RESULT__:')
print(json.dumps({'n_intersection': len(syms), 'n_missing': len(missing), 'missing': missing}))"""

env_args = {'var_call_ffAtFs2g1l61SFV6JTZqWbzh': 'file_storage/call_ffAtFs2g1l61SFV6JTZqWbzh.json', 'var_call_qmvstUsIbQmydnQOvRNocUXo': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_UHf6AKuOZMUNM7MqQgpMEfM2': 'file_storage/call_UHf6AKuOZMUNM7MqQgpMEfM2.json'}

exec(code, env_args)
