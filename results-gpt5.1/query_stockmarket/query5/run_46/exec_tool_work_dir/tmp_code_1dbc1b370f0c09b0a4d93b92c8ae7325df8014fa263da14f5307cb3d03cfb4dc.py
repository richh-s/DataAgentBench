code = """import json, pandas as pd, math
from pathlib import Path

syms = var_call_Ff9svcIsIPBqNVqQ0Ec08UVj
results = []

for s in syms:
    path_key = f'sym_{s}'
    # query for each symbol will be executed separately later

print('__RESULT__:')
print(json.dumps({'symbols': syms[:50]}))"""

env_args = {'var_call_8JY0zJzSnYJz34Yk9gASbp8s': 'file_storage/call_8JY0zJzSnYJz34Yk9gASbp8s.json', 'var_call_FbwxKtTur2QhdOgcgYNi4sPP': 'file_storage/call_FbwxKtTur2QhdOgcgYNi4sPP.json', 'var_call_Ff9svcIsIPBqNVqQ0Ec08UVj': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_hG00acvMNmnqGySSaLo4aMun': 'file_storage/call_hG00acvMNmnqGySSaLo4aMun.json'}

exec(code, env_args)
