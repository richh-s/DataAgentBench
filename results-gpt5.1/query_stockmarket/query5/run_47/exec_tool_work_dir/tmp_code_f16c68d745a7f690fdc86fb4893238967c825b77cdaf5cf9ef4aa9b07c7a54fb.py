code = """import json, pandas as pd, os
file = var_call_eWL5D26ST0rDYSsJNnrJi3Yg
with open(file, 'r') as f:
    data = json.load(f)

import math
rows = []
for r in data:
    low = float(r['Low'])
    high = float(r['High'])
    if low <= 0 or math.isnan(low) or math.isnan(high):
        continue
    rng = high - low
    if rng > 0.2 * low:
        rows.append({'Symbol': r['Symbol'], 'Date': r['Date']})

Df = pd.DataFrame(rows)
counts = Df.groupby('Symbol').size().reset_index(name='Days')
counts_sorted = counts.sort_values('Days', ascending=False).head(5)
result = counts_sorted.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_s2uPdYaejgejFzJOxR2KtJjm': 'file_storage/call_s2uPdYaejgejFzJOxR2KtJjm.json', 'var_call_dkrKcwQT9rg1LAxzgWcAreHK': 'file_storage/call_dkrKcwQT9rg1LAxzgWcAreHK.json', 'var_call_UIhvbxgEIqIepnIVxvgXtPOU': 'file_storage/call_UIhvbxgEIqIepnIVxvgXtPOU.json', 'var_call_9cws8r3oXMPXd0pD3TZVUbIu': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_eWL5D26ST0rDYSsJNnrJi3Yg': 'file_storage/call_eWL5D26ST0rDYSsJNnrJi3Yg.json'}

exec(code, env_args)
