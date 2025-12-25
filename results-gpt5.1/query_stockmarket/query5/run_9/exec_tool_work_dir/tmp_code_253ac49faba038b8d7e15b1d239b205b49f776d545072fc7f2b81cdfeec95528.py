code = """import json, pandas as pd
syms_days = var_call_Z6ANNl1qZlLsso0MNSbvc69v
sym_list = [r['Symbol'] for r in syms_days]
info = json.load(open(var_call_SuLYyzDLn95dtXzf8RJtyegT, 'r')) if isinstance(var_call_SuLYyzDLn95dtXzf8RJtyegT, str) else var_call_SuLYyzDLn95dtXzf8RJtyegT
info_df = pd.DataFrame(info)
subset = info_df[info_df['Symbol'].isin(sym_list)][['Symbol','Company Description']]
# extract company name as first part before first period
subset['CompanyName'] = subset['Company Description'].str.split('.').str[0]
merged = subset.set_index('Symbol').loc[sym_list].reset_index()
out = [{'Symbol': row['Symbol'], 'CompanyName': row['CompanyName']} for _, row in merged.iterrows()]
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_81EOLJGEHfF155klz6RD5tvw': 'file_storage/call_81EOLJGEHfF155klz6RD5tvw.json', 'var_call_SuLYyzDLn95dtXzf8RJtyegT': 'file_storage/call_SuLYyzDLn95dtXzf8RJtyegT.json', 'var_call_OD8EWWowLPdu5j5GemGoILKJ': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_oIdRZYIfSin24cM8rIeF4ZB8': 'file_storage/call_oIdRZYIfSin24cM8rIeF4ZB8.json', 'var_call_wtRJ57FNBdGmLXpuuMTOEj03': 'file_storage/call_wtRJ57FNBdGmLXpuuMTOEj03.json', 'var_call_D5Mzk648T0zRAmCMu0zWuhr4': [], 'var_call_2UdGqOYH3yNgaTj48jekHgA5': 'file_storage/call_2UdGqOYH3yNgaTj48jekHgA5.json', 'var_call_uQSLKpKR9ncGaiFruHJQMPbn': 'file_storage/call_uQSLKpKR9ncGaiFruHJQMPbn.json', 'var_call_FddeWo9lSU0MurCk6n5f3WTE': 'file_storage/call_FddeWo9lSU0MurCk6n5f3WTE.json', 'var_call_7em2RHeWQvNeZhpo845aKWGn': 'file_storage/call_7em2RHeWQvNeZhpo845aKWGn.json', 'var_call_vBtfHL3bYCCYnSNix86iC0Tz': 'file_storage/call_vBtfHL3bYCCYnSNix86iC0Tz.json', 'var_call_1Oydql8BAxP8PQuskFP01eCS': 'file_storage/call_1Oydql8BAxP8PQuskFP01eCS.json', 'var_call_UVZuL6iOz9liSBQ4einBdDlU': 'file_storage/call_UVZuL6iOz9liSBQ4einBdDlU.json', 'var_call_Z6ANNl1qZlLsso0MNSbvc69v': [{'Symbol': 'BIOC', 'days': 21}, {'Symbol': 'BKYI', 'days': 16}, {'Symbol': 'APEX', 'days': 15}, {'Symbol': 'AGMH', 'days': 13}, {'Symbol': 'BHAT', 'days': 10}]}

exec(code, env_args)
