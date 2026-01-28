code = """import json, pandas as pd
from pathlib import Path

# load symbols+names
recs = json.loads(Path(var_call_RsghL4UroeHSwUjPcoLqnafK).read_text())
info = pd.DataFrame(recs)
syms = set(info['Symbol'].dropna())

# load trade tables list
tables = json.loads(Path(var_call_hafkDQXR6rEtIs35wsOfOvpJ).read_text())
trade_syms = set(tables)

valid = sorted(syms.intersection(trade_syms))
missing = sorted(syms - trade_syms)

print('__RESULT__:')
print(json.dumps({'valid_n': len(valid), 'missing_n': len(missing), 'valid': valid, 'missing_preview': missing[:20]}))"""

env_args = {'var_call_RsghL4UroeHSwUjPcoLqnafK': 'file_storage/call_RsghL4UroeHSwUjPcoLqnafK.json', 'var_call_cgAd9NGNcdGgSVnLuC0reEW1': {'n_symbols': 86, 'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'n_chunks': 1}, 'var_call_hafkDQXR6rEtIs35wsOfOvpJ': 'file_storage/call_hafkDQXR6rEtIs35wsOfOvpJ.json'}

exec(code, env_args)
