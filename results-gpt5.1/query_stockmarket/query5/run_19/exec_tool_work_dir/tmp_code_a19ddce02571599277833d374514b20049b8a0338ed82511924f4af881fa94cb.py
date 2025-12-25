code = """import json, pandas as pd
meta = pd.read_json(var_call_CTYMQvDXtw1Bh42e8BN63JEV)
subset = meta[meta['Symbol'].isin(['BIOC','BKYI','APEX','AGMH','BHAT'])]
result = subset[['Symbol','Company Description']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_glTYOB3jibACn8eNGTwIGZeQ': 'file_storage/call_glTYOB3jibACn8eNGTwIGZeQ.json', 'var_call_CTYMQvDXtw1Bh42e8BN63JEV': 'file_storage/call_CTYMQvDXtw1Bh42e8BN63JEV.json', 'var_call_yxjgJ5RzCRrWGnzdCp2WNc0V': {'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']]}, 'var_call_UDjKNkdTVzToPfWDbe0BSSMe': 'file_storage/call_UDjKNkdTVzToPfWDbe0BSSMe.json', 'var_call_8RTf7INeBOb30SEOM9MwYBg8': {'BIOC': 21, 'BKYI': 16, 'APEX': 15, 'AGMH': 13, 'BHAT': 10}}

exec(code, env_args)
