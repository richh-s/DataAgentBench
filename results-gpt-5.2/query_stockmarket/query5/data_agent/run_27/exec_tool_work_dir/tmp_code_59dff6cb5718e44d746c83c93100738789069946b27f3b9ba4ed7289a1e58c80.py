code = """import json, pandas as pd

dfs = []
for var in [var_call_fBHoeFhqLr1V2fUnZsrghL4H, var_call_mjTBJtPy5fpSW4XlU32LdRkV, var_call_5ZB4lIIBKfPW4iKExjwIlh4v, var_call_Vss4Hzh4Pi05IOYbIWxGeeht]:
    dfs.append(pd.DataFrame(var))
counts = pd.concat(dfs, ignore_index=True)
counts['n_days'] = counts['n_days'].astype(int)

top5 = counts.sort_values(['n_days','Symbol'], ascending=[False, True]).head(5)

# load company names
cap_path = var_call_H1EzipIeXpIxlsCS4XeHhHeF
with open(cap_path, 'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
cap_df = cap_df.rename(columns={'company_name':'Company'})
merged = top5.merge(cap_df[['Symbol','Company']], on='Symbol', how='left')
answer = merged['Company'].tolist()

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_H1EzipIeXpIxlsCS4XeHhHeF': 'file_storage/call_H1EzipIeXpIxlsCS4XeHhHeF.json', 'var_call_QvNSzJv7DaVr49HT6l7W4OSF': 'file_storage/call_QvNSzJv7DaVr49HT6l7W4OSF.json', 'var_call_rlwDd8ulTEwLmC8ih2zCyUyM': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_symbols': 86}, 'var_call_m7CZvSXbDh3NARzsC3b1whfO': [{'Symbol': 'AGMH', 'n_days': '13'}], 'var_call_BRXXbSA45huMx6g9JyPPkCtJ': [{'Symbol': 'AGMH', 'n_days': '13'}, {'Symbol': 'ALACU', 'n_days': '0'}], 'var_call_mSytEkpuBBY7FZfpLUkNm6ea': 'ok', 'var_call_fBHoeFhqLr1V2fUnZsrghL4H': [{'Symbol': 'AGMH', 'n_days': '13'}, {'Symbol': 'ALACU', 'n_days': '0'}, {'Symbol': 'AMHC', 'n_days': '0'}, {'Symbol': 'ANDA', 'n_days': '0'}, {'Symbol': 'APEX', 'n_days': '15'}, {'Symbol': 'BCLI', 'n_days': '0'}, {'Symbol': 'BHAT', 'n_days': '10'}, {'Symbol': 'BIOC', 'n_days': '21'}, {'Symbol': 'BKYI', 'n_days': '16'}, {'Symbol': 'BLFS', 'n_days': '0'}, {'Symbol': 'BOSC', 'n_days': '3'}, {'Symbol': 'BOTJ', 'n_days': '0'}, {'Symbol': 'BWEN', 'n_days': '5'}, {'Symbol': 'CBAT', 'n_days': '23'}, {'Symbol': 'CCCL', 'n_days': '13'}, {'Symbol': 'CDMOP', 'n_days': '0'}, {'Symbol': 'CEMI', 'n_days': '3'}, {'Symbol': 'CFBK', 'n_days': '0'}, {'Symbol': 'CFFA', 'n_days': '0'}, {'Symbol': 'CLRB', 'n_days': '14'}, {'Symbol': 'CORV', 'n_days': '10'}, {'Symbol': 'CPAH', 'n_days': '16'}, {'Symbol': 'CUBA', 'n_days': '0'}, {'Symbol': 'CVV', 'n_days': '0'}, {'Symbol': 'DZSI', 'n_days': '1'}, {'Symbol': 'ELSE', 'n_days': '0'}], 'var_call_mjTBJtPy5fpSW4XlU32LdRkV': [{'Symbol': 'EXPC', 'n_days': '0'}, {'Symbol': 'EYEG', 'n_days': '18'}, {'Symbol': 'FAMI', 'n_days': '23'}, {'Symbol': 'FNCB', 'n_days': '1'}, {'Symbol': 'FSBW', 'n_days': '0'}, {'Symbol': 'FTFT', 'n_days': '21'}, {'Symbol': 'GDYN', 'n_days': '0'}, {'Symbol': 'GLG', 'n_days': '42'}, {'Symbol': 'GTEC', 'n_days': '0'}, {'Symbol': 'HCCOU', 'n_days': '0'}, {'Symbol': 'HNNA', 'n_days': '0'}, {'Symbol': 'HQI', 'n_days': '2'}, {'Symbol': 'HRTX', 'n_days': '1'}, {'Symbol': 'IDEX', 'n_days': '15'}, {'Symbol': 'IGIC', 'n_days': '0'}, {'Symbol': 'IOTS', 'n_days': '1'}], 'var_call_5ZB4lIIBKfPW4iKExjwIlh4v': [{'Symbol': 'ISNS', 'n_days': '0'}, {'Symbol': 'ITI', 'n_days': '0'}, {'Symbol': 'LACQ', 'n_days': '0'}, {'Symbol': 'MBCN', 'n_days': '0'}, {'Symbol': 'MCEP', 'n_days': '14'}, {'Symbol': 'MLND', 'n_days': '3'}, {'Symbol': 'MMAC', 'n_days': '1'}, {'Symbol': 'MNPR', 'n_days': '4'}, {'Symbol': 'NVEE', 'n_days': '1'}, {'Symbol': 'NXTD', 'n_days': '15'}, {'Symbol': 'OPOF', 'n_days': '0'}, {'Symbol': 'OPTT', 'n_days': '12'}, {'Symbol': 'ORGO', 'n_days': '15'}, {'Symbol': 'OTEL', 'n_days': '1'}, {'Symbol': 'PBFS', 'n_days': '0'}, {'Symbol': 'PBTS', 'n_days': '8'}, {'Symbol': 'PCSB', 'n_days': '0'}, {'Symbol': 'PECK', 'n_days': '19'}, {'Symbol': 'PEIX', 'n_days': '12'}], 'var_call_Vss4Hzh4Pi05IOYbIWxGeeht': [{'Symbol': 'PFIE', 'n_days': '2'}, {'Symbol': 'PLIN', 'n_days': '1'}, {'Symbol': 'POPE', 'n_days': '0'}, {'Symbol': 'QRHC', 'n_days': '3'}, {'Symbol': 'SES', 'n_days': '51'}, {'Symbol': 'SHSP', 'n_days': '1'}, {'Symbol': 'SNSS', 'n_days': '32'}, {'Symbol': 'SSNT', 'n_days': '11'}, {'Symbol': 'STKS', 'n_days': '0'}, {'Symbol': 'TGLS', 'n_days': '0'}, {'Symbol': 'TMSR', 'n_days': '40'}, {'Symbol': 'VERB', 'n_days': '38'}, {'Symbol': 'VMD', 'n_days': '1'}, {'Symbol': 'VRRM', 'n_days': '0'}, {'Symbol': 'VVPR', 'n_days': '14'}, {'Symbol': 'WHLM', 'n_days': '0'}, {'Symbol': 'WHLR', 'n_days': '15'}, {'Symbol': 'XPEL', 'n_days': '4'}]}

exec(code, env_args)
