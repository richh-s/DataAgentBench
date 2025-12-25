code = """import json

with open(locals()['var_function-call-9742123529145069746'], 'r') as f:
    stock_data_agmh = json.load(f)

day_count_agmh = 0
for record in stock_data_agmh:
    high = float(record['High'])
    low = float(record['Low'])
    if high > 1.20 * low:
        day_count_agmh += 1

print("__RESULT__:")
print(json.dumps({
    'symbol': 'AGMH',
    'count': day_count_agmh
}))"""

env_args = {'var_function-call-10635938268862818382': 'file_storage/function-call-10635938268862818382.json', 'var_function-call-7512712772181424858': 'file_storage/function-call-7512712772181424858.json', 'var_function-call-14575303271704160794': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7698664705107236352': 'file_storage/function-call-7698664705107236352.json', 'var_function-call-5390203662496531257': 'file_storage/function-call-5390203662496531257.json', 'var_function-call-8796463335682772801': 'file_storage/function-call-8796463335682772801.json', 'var_function-call-10882724012973181006': 'file_storage/function-call-10882724012973181006.json', 'var_function-call-9742123529145069746': 'file_storage/function-call-9742123529145069746.json', 'var_function-call-11049086404300196738': {'count': 86, 'first_five_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'last_five_symbols': ['VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'all_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_function-call-4932084830650739945': 'file_storage/function-call-4932084830650739945.json'}

exec(code, env_args)
