code = """import json

# Load symbols and remove reserved-word table names that break SQL without quoting.
syms = var_call_D1TDaYMFg83HzewjuCu3SQ0T['symbols_with_trade_data']
reserved = {'ELSE'}
syms2 = [s for s in syms if s not in reserved]
print('__RESULT__:')
print(json.dumps({'symbols': syms2, 'removed': sorted(list(reserved.intersection(set(syms))))}))"""

env_args = {'var_call_5VDv5iBeOE5vhvQB62TrsIWA': 'file_storage/call_5VDv5iBeOE5vhvQB62TrsIWA.json', 'var_call_FrYDajh5fEHjmSKZ3dsDVewJ': 'file_storage/call_FrYDajh5fEHjmSKZ3dsDVewJ.json', 'var_call_D1TDaYMFg83HzewjuCu3SQ0T': {'n_cap_symbols': 86, 'n_symbols_with_trade_data': 86, 'symbols_with_trade_data': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
