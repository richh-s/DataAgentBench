code = """import json, pandas as pd
import os
path = var_call_COkPixobIc25waNgckCAfJpk
with open(path) as f:
    data = json.load(f)

rows = []
for r in data:
    low = float(r['Low'])
    high = float(r['High'])
    if low > 0 and (high - low) / low > 0.2:
        rows.append(r)

df = pd.DataFrame(rows)
counts = df.groupby('Symbol').size().sort_values(ascending=False).head(5)
result = counts.to_dict()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_uQPVZnU823CE2SOlAj7hnl1Z': 'file_storage/call_uQPVZnU823CE2SOlAj7hnl1Z.json', 'var_call_pM2FV6lLgafSuYB8s9TzJY44': 'file_storage/call_pM2FV6lLgafSuYB8s9TzJY44.json', 'var_call_nYPMp3xDGT6jluovHDWhW7Gv': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'var_call_COkPixobIc25waNgckCAfJpk': 'file_storage/call_COkPixobIc25waNgckCAfJpk.json'}

exec(code, env_args)
