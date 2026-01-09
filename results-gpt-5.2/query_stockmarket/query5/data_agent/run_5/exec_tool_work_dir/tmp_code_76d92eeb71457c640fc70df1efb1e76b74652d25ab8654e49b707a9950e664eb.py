code = """import json
# load trade tables list
path = var_call_dKb4D8xdnncvcWNHDzkn4m3d
with open(path,'r') as f:
    tables = set(json.load(f))

tickers = var_call_AXIswJbTjUMXGe8mYYAQlqU6['tickers']
available = [t for t in tickers if t in tables]
missing = [t for t in tickers if t not in tables]
print('__RESULT__:')
print(json.dumps({'available': available, 'n_available': len(available), 'n_missing': len(missing), 'missing': missing[:20]}))"""

env_args = {'var_call_YZCMnQZ9llzwejyPLHTIQZN1': 'file_storage/call_YZCMnQZ9llzwejyPLHTIQZN1.json', 'var_call_AXIswJbTjUMXGe8mYYAQlqU6': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_dKb4D8xdnncvcWNHDzkn4m3d': 'file_storage/call_dKb4D8xdnncvcWNHDzkn4m3d.json'}

exec(code, env_args)
