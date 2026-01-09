code = """import json

# load tickers list
obj = var_call_QfZYyFBpPBlsKm8JbdZRunEq
capital_tickers = set(obj['tickers'])

# load available tables
path = var_call_GIlC3qtu85xQNESV78Zcc4y7
with open(path, 'r', encoding='utf-8') as f:
    tables = set(json.load(f))

available = sorted(capital_tickers.intersection(tables))
missing = sorted(capital_tickers.difference(tables))

print('__RESULT__:')
print(json.dumps({'available': available, 'n_available': len(available), 'n_missing': len(missing), 'missing_sample': missing[:20]}))"""

env_args = {'var_call_H2hcxVjddyl5n2L4MVpMNrjI': 'file_storage/call_H2hcxVjddyl5n2L4MVpMNrjI.json', 'var_call_QfZYyFBpPBlsKm8JbdZRunEq': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_GIlC3qtu85xQNESV78Zcc4y7': 'file_storage/call_GIlC3qtu85xQNESV78Zcc4y7.json'}

exec(code, env_args)
