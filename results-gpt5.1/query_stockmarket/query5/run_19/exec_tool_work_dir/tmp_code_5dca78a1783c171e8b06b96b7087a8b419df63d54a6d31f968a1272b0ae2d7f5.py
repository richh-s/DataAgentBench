code = """import json, pandas as pd
import os
path = var_call_UDjKNkdTVzToPfWDbe0BSSMe
with open(path) as f:
    data = json.load(f)
rows = pd.DataFrame(data)
rows['High'] = rows['High'].astype(float)
rows['Low'] = rows['Low'].astype(float)
rows = rows[rows['Low']>0]
rows['range_ratio'] = (rows['High']-rows['Low'])/rows['Low']
counts = rows[rows['range_ratio']>0.2].groupby('Symbol').size().sort_values(ascending=False)
result = counts.head(5).to_dict()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_glTYOB3jibACn8eNGTwIGZeQ': 'file_storage/call_glTYOB3jibACn8eNGTwIGZeQ.json', 'var_call_CTYMQvDXtw1Bh42e8BN63JEV': 'file_storage/call_CTYMQvDXtw1Bh42e8BN63JEV.json', 'var_call_yxjgJ5RzCRrWGnzdCp2WNc0V': {'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']]}, 'var_call_UDjKNkdTVzToPfWDbe0BSSMe': 'file_storage/call_UDjKNkdTVzToPfWDbe0BSSMe.json'}

exec(code, env_args)
