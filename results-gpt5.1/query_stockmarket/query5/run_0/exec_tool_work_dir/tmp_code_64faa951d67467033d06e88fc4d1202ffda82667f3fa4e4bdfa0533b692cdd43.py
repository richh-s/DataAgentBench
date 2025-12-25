code = """import json

path = var_call_hgLF9S8c9E3kiqruYn4FgM6t
with open(path, 'r') as f:
    data = json.load(f)
query = data['query']

import textwrap
short = query[:10000]

result = json.dumps({'query': query})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_z0vUN3AiZB3aOsmYx8b60Vnr': 'file_storage/call_z0vUN3AiZB3aOsmYx8b60Vnr.json', 'var_call_VpDgoA7fXkQOcSnmZFJBToDI': 'file_storage/call_VpDgoA7fXkQOcSnmZFJBToDI.json', 'var_call_vPGOtBLxkjHVzLaHmppQjjo4': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_hgLF9S8c9E3kiqruYn4FgM6t': 'file_storage/call_hgLF9S8c9E3kiqruYn4FgM6t.json'}

exec(code, env_args)
