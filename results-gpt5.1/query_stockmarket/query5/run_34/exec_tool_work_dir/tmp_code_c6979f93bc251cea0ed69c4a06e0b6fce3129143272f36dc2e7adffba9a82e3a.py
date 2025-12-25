code = """import json, pandas as pd
paths = [var_call_25ssrzTWwqkPv7zTNreKdLiZ, var_call_lY3BZz0MuniDG5zuAZAivxYR, var_call_LgcPvkJuz27LgvAUAw6KrPef, var_call_a32n1q2u7w49Lpr2uTnplEiC, var_call_fPiQQzENscPNIRg3tWGrm0Zq, var_call_Cf8YrEBUccYrwPQKwviBwWyE, var_call_z3NhrJGnAwmSh3RtSnUhjsiU, var_call_biyOlcIxlx2wdhLhgLCDqFY5, var_call_V78G90Vkyn98FO6lzNoHRpWc]
frames = []
for p in paths:
    with open(p,'r') as f:
        frames.append(pd.DataFrame(json.load(f)))
all_df = pd.concat(frames, ignore_index=True)
all_df['High'] = all_df['High'].astype(float)
all_df['Low'] = all_df['Low'].astype(float)
mask = (all_df['High'] - all_df['Low']) > 0.2*all_df['Low']
counts = all_df[mask].groupby('Symbol').size().sort_values(ascending=False)
result = counts.to_dict()
import json as j
out = j.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Y6VKBWpuBLO5UEMFYEGRu28y': 'file_storage/call_Y6VKBWpuBLO5UEMFYEGRu28y.json', 'var_call_aqFejGVlsniDcjfv1ws7Py2w': 'file_storage/call_aqFejGVlsniDcjfv1ws7Py2w.json', 'var_call_PC4EiOaseYUcveJUd1bKG3BE': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_25ssrzTWwqkPv7zTNreKdLiZ': 'file_storage/call_25ssrzTWwqkPv7zTNreKdLiZ.json', 'var_call_lY3BZz0MuniDG5zuAZAivxYR': 'file_storage/call_lY3BZz0MuniDG5zuAZAivxYR.json', 'var_call_dj5owOBH5TumO8NuQDv6YzYR': [], 'var_call_LgcPvkJuz27LgvAUAw6KrPef': 'file_storage/call_LgcPvkJuz27LgvAUAw6KrPef.json', 'var_call_a32n1q2u7w49Lpr2uTnplEiC': 'file_storage/call_a32n1q2u7w49Lpr2uTnplEiC.json', 'var_call_fPiQQzENscPNIRg3tWGrm0Zq': 'file_storage/call_fPiQQzENscPNIRg3tWGrm0Zq.json', 'var_call_Cf8YrEBUccYrwPQKwviBwWyE': 'file_storage/call_Cf8YrEBUccYrwPQKwviBwWyE.json', 'var_call_z3NhrJGnAwmSh3RtSnUhjsiU': 'file_storage/call_z3NhrJGnAwmSh3RtSnUhjsiU.json', 'var_call_biyOlcIxlx2wdhLhgLCDqFY5': 'file_storage/call_biyOlcIxlx2wdhLhgLCDqFY5.json', 'var_call_V78G90Vkyn98FO6lzNoHRpWc': 'file_storage/call_V78G90Vkyn98FO6lzNoHRpWc.json'}

exec(code, env_args)
