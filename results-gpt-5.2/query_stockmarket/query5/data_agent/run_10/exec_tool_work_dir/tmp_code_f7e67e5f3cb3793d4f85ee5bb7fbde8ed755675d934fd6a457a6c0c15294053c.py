code = """import json
path = var_call_ER5VEOVIeqnubCN98QtGcoRg
with open(path,'r') as f:
    tables = set(json.load(f))
tickers = set(var_call_CoBpvddZUSoNvkGdnTFxoyeR['tickers'])
avail = sorted(list(tickers & tables))
missing = sorted(list(tickers - tables))
print('__RESULT__:')
print(json.dumps({'available': avail, 'missing': missing, 'n_available': len(avail), 'n_missing': len(missing)}))"""

env_args = {'var_call_ekORxxxLuAnrlnsBk9tLaxAt': 'file_storage/call_ekORxxxLuAnrlnsBk9tLaxAt.json', 'var_call_CoBpvddZUSoNvkGdnTFxoyeR': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_ER5VEOVIeqnubCN98QtGcoRg': 'file_storage/call_ER5VEOVIeqnubCN98QtGcoRg.json'}

exec(code, env_args)
