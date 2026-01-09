code = """import json, pandas as pd

# top symbols
top = pd.DataFrame(var_call_LtVulyIHKxseKaputNKFM1nG)
top['days'] = top['days'].astype(int)

# company names map
path = var_call_5VDv5iBeOE5vhvQB62TrsIWA
with open(path,'r') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)

out = top.merge(cap_df, left_on='symbol', right_on='symbol', how='left')
answer_lines = []
for _, r in out.iterrows():
    answer_lines.append(f"{r['company_name']}")

print('__RESULT__:')
print(json.dumps('\n'.join(answer_lines)))"""

env_args = {'var_call_5VDv5iBeOE5vhvQB62TrsIWA': 'file_storage/call_5VDv5iBeOE5vhvQB62TrsIWA.json', 'var_call_FrYDajh5fEHjmSKZ3dsDVewJ': 'file_storage/call_FrYDajh5fEHjmSKZ3dsDVewJ.json', 'var_call_D1TDaYMFg83HzewjuCu3SQ0T': {'n_cap_symbols': 86, 'n_symbols_with_trade_data': 86, 'symbols_with_trade_data': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_TTAjN0ThhRYUvknwuZaqHXoO': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'removed': ['ELSE']}, 'var_call_LtVulyIHKxseKaputNKFM1nG': [{'symbol': 'SES', 'days': '51'}, {'symbol': 'GLG', 'days': '42'}, {'symbol': 'TMSR', 'days': '40'}, {'symbol': 'VERB', 'days': '38'}, {'symbol': 'SNSS', 'days': '32'}]}

exec(code, env_args)
