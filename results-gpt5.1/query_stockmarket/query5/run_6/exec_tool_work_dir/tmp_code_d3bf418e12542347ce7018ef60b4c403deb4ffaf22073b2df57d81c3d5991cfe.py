code = """import json, pandas as pd
symbols_info_path = var_call_x7QM5sru6zlaamKDxFNJ2FG8
with open(symbols_info_path, 'r') as f:
    symbols_info = json.load(f)
info_df = pd.DataFrame(symbols_info)
rankings = var_call_HHyQdZMPR9qVKxl7rDIazLHF
rank_df = pd.DataFrame(rankings)
merged = rank_df.merge(info_df, left_on='symbol', right_on='Symbol', how='left')
result = merged[['symbol','Company Description']].to_dict(orient='records')
out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mivuTFkR3FxcChzcTQL6xWlq': 'file_storage/call_mivuTFkR3FxcChzcTQL6xWlq.json', 'var_call_x7QM5sru6zlaamKDxFNJ2FG8': 'file_storage/call_x7QM5sru6zlaamKDxFNJ2FG8.json', 'var_call_i36mpKrCwygL7wHccbkB3jbd': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_HHyQdZMPR9qVKxl7rDIazLHF': [{'symbol': 'SES', 'volatile_days': '51'}, {'symbol': 'GLG', 'volatile_days': '42'}, {'symbol': 'TMSR', 'volatile_days': '40'}, {'symbol': 'VERB', 'volatile_days': '38'}, {'symbol': 'SNSS', 'volatile_days': '32'}]}

exec(code, env_args)
