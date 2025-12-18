code = """import json

processed_data = json.load(open(locals()['var_function-call-11550279543140068046'], 'r'))
companies_data = processed_data['companies_data']
symbols_to_process = processed_data['symbols_to_process']

apex_data = json.load(open(locals()['var_function-call-642449684565013314'], 'r'))

for trade_day in apex_data:
    high = float(trade_day['High'])
    low = float(trade_day['Low'])
    if low > 0 and (high - low) > 0.20 * low:
        companies_data['APEX']['count'] += 1

print('__RESULT__:')
print(json.dumps({'companies_data': companies_data, 'symbols_to_process': symbols_to_process}))"""

env_args = {'var_function-call-3697019534837681094': 'file_storage/function-call-3697019534837681094.json', 'var_function-call-17576780368704944672': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-2435395218391636322': 'file_storage/function-call-2435395218391636322.json', 'var_function-call-14554568466120289191': 'file_storage/function-call-14554568466120289191.json', 'var_function-call-18438686950626683294': 'file_storage/function-call-18438686950626683294.json', 'var_function-call-6961230621481136399': 'file_storage/function-call-6961230621481136399.json', 'var_function-call-1889804083985892398': 'file_storage/function-call-1889804083985892398.json', 'var_function-call-12768621162850898562': 'file_storage/function-call-12768621162850898562.json', 'var_function-call-14613412995435816686': [], 'var_function-call-15856978282471792289': 'file_storage/function-call-15856978282471792289.json', 'var_function-call-15755323397071113234': 'file_storage/function-call-15755323397071113234.json', 'var_function-call-11550279543140068046': 'file_storage/function-call-11550279543140068046.json', 'var_function-call-642449684565013314': 'file_storage/function-call-642449684565013314.json'}

exec(code, env_args)
