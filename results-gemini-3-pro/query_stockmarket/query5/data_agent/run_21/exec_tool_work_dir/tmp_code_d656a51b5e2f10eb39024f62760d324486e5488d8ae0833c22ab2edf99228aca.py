code = """import json

with open(locals()['var_function-call-6172360428476729765'], 'r') as f:
    batches = json.load(f)

print("__RESULT__:")
print(json.dumps(batches[:5]))"""

env_args = {'var_function-call-2999058475558920348': 'file_storage/function-call-2999058475558920348.json', 'var_function-call-14692438593092107821': 'file_storage/function-call-14692438593092107821.json', 'var_function-call-9945285838579919155': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-9642806757870856452': 'file_storage/function-call-9642806757870856452.json', 'var_function-call-10050164000650215020': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + symbol +  WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + symbol +  WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as cnt FROM  + symbol +  WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as cnt FROM  + symbol +  WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low UNION ALL SELECT ", 'var_function-call-10575345276095007953': 'test', 'var_function-call-13583685081955783059': 'file_storage/function-call-13583685081955783059.json', 'var_function-call-6172360428476729765': 'file_storage/function-call-6172360428476729765.json'}

exec(code, env_args)
