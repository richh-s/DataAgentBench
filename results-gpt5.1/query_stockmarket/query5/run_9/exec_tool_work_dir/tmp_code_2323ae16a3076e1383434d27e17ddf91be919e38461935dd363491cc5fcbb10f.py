code = """import json, pandas as pd, math
# gather all file paths from previous query_db parallel call manually
files = [
 var_call_oIdRZYIfSin24cM8rIeF4ZB8,
 var_call_wtRJ57FNBdGmLXpuuMTOEj03,
 var_call_2UdGqOYH3yNgaTj48jekHgA5,
 var_call_uQSLKpKR9ncGaiFruHJQMPbn,
 var_call_FddeWo9lSU0MurCk6n5f3WTE,
 var_call_7em2RHeWQvNeZhpo845aKWGn,
 var_call_vBtfHL3bYCCYnSNix86iC0Tz,
 var_call_1Oydql8BAxP8PQuskFP01eCS,
 var_call_UVZuL6iOz9liSBQ4einBdDlU
]
frames = []
for path in files:
    if isinstance(path, str):
        with open(path, 'r') as f:
            data = json.load(f)
    else:
        data = path
    frames.append(pd.DataFrame(data))
all_df = pd.concat(frames, ignore_index=True)
all_df['High'] = all_df['High'].astype(float)
all_df['Low'] = all_df['Low'].astype(float)
mask = all_df['Low'] > 0
all_df = all_df[mask]
all_df['range_ratio'] = (all_df['High'] - all_df['Low']) / all_df['Low']
exceed = all_df[all_df['range_ratio'] > 0.20]
counts = exceed.groupby('Symbol')['Date'].nunique().reset_index(name='days')
counts = counts.sort_values('days', ascending=False).head(5)
result = counts.to_dict(orient='records')
result_json = json.dumps(result)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_81EOLJGEHfF155klz6RD5tvw': 'file_storage/call_81EOLJGEHfF155klz6RD5tvw.json', 'var_call_SuLYyzDLn95dtXzf8RJtyegT': 'file_storage/call_SuLYyzDLn95dtXzf8RJtyegT.json', 'var_call_OD8EWWowLPdu5j5GemGoILKJ': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_oIdRZYIfSin24cM8rIeF4ZB8': 'file_storage/call_oIdRZYIfSin24cM8rIeF4ZB8.json', 'var_call_wtRJ57FNBdGmLXpuuMTOEj03': 'file_storage/call_wtRJ57FNBdGmLXpuuMTOEj03.json', 'var_call_D5Mzk648T0zRAmCMu0zWuhr4': [], 'var_call_2UdGqOYH3yNgaTj48jekHgA5': 'file_storage/call_2UdGqOYH3yNgaTj48jekHgA5.json', 'var_call_uQSLKpKR9ncGaiFruHJQMPbn': 'file_storage/call_uQSLKpKR9ncGaiFruHJQMPbn.json', 'var_call_FddeWo9lSU0MurCk6n5f3WTE': 'file_storage/call_FddeWo9lSU0MurCk6n5f3WTE.json', 'var_call_7em2RHeWQvNeZhpo845aKWGn': 'file_storage/call_7em2RHeWQvNeZhpo845aKWGn.json', 'var_call_vBtfHL3bYCCYnSNix86iC0Tz': 'file_storage/call_vBtfHL3bYCCYnSNix86iC0Tz.json', 'var_call_1Oydql8BAxP8PQuskFP01eCS': 'file_storage/call_1Oydql8BAxP8PQuskFP01eCS.json', 'var_call_UVZuL6iOz9liSBQ4einBdDlU': 'file_storage/call_UVZuL6iOz9liSBQ4einBdDlU.json'}

exec(code, env_args)
