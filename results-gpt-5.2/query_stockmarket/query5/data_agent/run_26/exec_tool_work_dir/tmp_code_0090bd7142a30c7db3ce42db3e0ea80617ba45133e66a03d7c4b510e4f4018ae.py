code = """import json

# load trade tables list
src = var_call_FmgytLo2StSMnARMZlW3cnce
if isinstance(src, str):
    with open(src,'r') as f:
        trade_tables = set(json.load(f))
else:
    trade_tables = set(src)

# tickers
tickers = var_call_pr6PGyxqB37ogrY2vnSestQn['tickers']
common = [t for t in tickers if t in trade_tables]
missing = [t for t in tickers if t not in trade_tables]

print('__RESULT__:')
print(json.dumps({'common': common, 'n_common': len(common), 'missing': missing, 'n_missing': len(missing)}))"""

env_args = {'var_call_STL7teZLl2SdMjMcSmvTbo1M': 'file_storage/call_STL7teZLl2SdMjMcSmvTbo1M.json', 'var_call_pr6PGyxqB37ogrY2vnSestQn': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_FmgytLo2StSMnARMZlW3cnce': 'file_storage/call_FmgytLo2StSMnARMZlW3cnce.json'}

exec(code, env_args)
