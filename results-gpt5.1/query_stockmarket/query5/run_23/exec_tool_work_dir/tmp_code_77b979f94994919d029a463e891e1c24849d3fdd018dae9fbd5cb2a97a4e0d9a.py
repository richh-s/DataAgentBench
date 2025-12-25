code = """import json, pandas as pd

mapping = {
 'AGMH': var_call_xaDYCiTN4YNPfWLCLseArSbk,
 'ALACU': var_call_Bvvyp6mHQIkJTuiR2O5gh8md,
 'AMHC': var_call_hrfOxYS7fzwjemI0XwPuSO5R,
 'ANDA': var_call_0pKlpwAeJ9thwAEdArIuYsOH,
 'APEX': var_call_LsYcWv9NOgcMWV70SD6bdMEM,
 'BCLI': var_call_wbWGZkFORYTMB9Sg9dTnSjq6,
 'BHAT': var_call_3KOqfFWBealI96l9OcpQqh6x,
 'BIOC': var_call_D3PvNnQHeM0N2hVbcoY1KDv7,
 'BKYI': var_call_O7VRu8CGo3DxBM9fTs5rHEL2,
 'BLFS': var_call_BkVQtzlgeRZPzJCjHRd83Bni,
 'BOSC': var_call_x1NuluuiBIXTXkTCCIuO5BkG,
 'BOTJ': var_call_ug5EgwatJslA29TisMEvOEvH,
 'BWEN': var_call_l8EkQClH9bEVDx9QcUowz8eI,
 'CBAT': var_call_nDuxfphUWGA0FddHkyfgNFd4,
 'CCCL': var_call_lUjiUZyiS6NZpKx9pB3YvbId,
 'CDMOP': var_call_Il4ERMfX0cyQLgYPgwhIzEzh,
 'CEMI': var_call_O5no8xnId8IImG7sZ7BJ5AIJ,
 'CFBK': var_call_uzlclmP8BXKuxIG5kc9H3PPT,
 'CFFA': var_call_9gMllwg57ASxVKEedaB7F2TU,
 'CLRB': var_call_s5NazNwpXQA6fV8exHEFyCJ7
}

all_rows = []
for sym, path in mapping.items():
    with open(path) as f:
        rows = json.load(f)
    all_rows.extend(rows)

df = pd.DataFrame(all_rows)
if df.empty:
    result = []
else:
    df['High'] = df['High'].astype(float)
    df['Low'] = df['Low'].astype(float)
    rng = df['High'] - df['Low']
    cond = rng > 0.2 * df['Low']
    counts = df[cond].groupby('Symbol').size().sort_values(ascending=False)
    top5 = counts.head(5).reset_index()
    result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oVQjh9u5mLSbAixKxJMu927W': 'file_storage/call_oVQjh9u5mLSbAixKxJMu927W.json', 'var_call_Wv8ti8avHzWM8aB2sDzY4lzK': 'file_storage/call_Wv8ti8avHzWM8aB2sDzY4lzK.json', 'var_call_QBfaOBPqTON1Su2nzaqHFfPI': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_xaDYCiTN4YNPfWLCLseArSbk': 'file_storage/call_xaDYCiTN4YNPfWLCLseArSbk.json', 'var_call_Bvvyp6mHQIkJTuiR2O5gh8md': 'file_storage/call_Bvvyp6mHQIkJTuiR2O5gh8md.json', 'var_call_hrfOxYS7fzwjemI0XwPuSO5R': [], 'var_call_0pKlpwAeJ9thwAEdArIuYsOH': 'file_storage/call_0pKlpwAeJ9thwAEdArIuYsOH.json', 'var_call_LsYcWv9NOgcMWV70SD6bdMEM': 'file_storage/call_LsYcWv9NOgcMWV70SD6bdMEM.json', 'var_call_wbWGZkFORYTMB9Sg9dTnSjq6': 'file_storage/call_wbWGZkFORYTMB9Sg9dTnSjq6.json', 'var_call_3KOqfFWBealI96l9OcpQqh6x': 'file_storage/call_3KOqfFWBealI96l9OcpQqh6x.json', 'var_call_D3PvNnQHeM0N2hVbcoY1KDv7': 'file_storage/call_D3PvNnQHeM0N2hVbcoY1KDv7.json', 'var_call_O7VRu8CGo3DxBM9fTs5rHEL2': 'file_storage/call_O7VRu8CGo3DxBM9fTs5rHEL2.json', 'var_call_BkVQtzlgeRZPzJCjHRd83Bni': 'file_storage/call_BkVQtzlgeRZPzJCjHRd83Bni.json', 'var_call_x1NuluuiBIXTXkTCCIuO5BkG': 'file_storage/call_x1NuluuiBIXTXkTCCIuO5BkG.json', 'var_call_ug5EgwatJslA29TisMEvOEvH': 'file_storage/call_ug5EgwatJslA29TisMEvOEvH.json', 'var_call_l8EkQClH9bEVDx9QcUowz8eI': 'file_storage/call_l8EkQClH9bEVDx9QcUowz8eI.json', 'var_call_nDuxfphUWGA0FddHkyfgNFd4': 'file_storage/call_nDuxfphUWGA0FddHkyfgNFd4.json', 'var_call_lUjiUZyiS6NZpKx9pB3YvbId': 'file_storage/call_lUjiUZyiS6NZpKx9pB3YvbId.json', 'var_call_Il4ERMfX0cyQLgYPgwhIzEzh': 'file_storage/call_Il4ERMfX0cyQLgYPgwhIzEzh.json', 'var_call_O5no8xnId8IImG7sZ7BJ5AIJ': 'file_storage/call_O5no8xnId8IImG7sZ7BJ5AIJ.json', 'var_call_uzlclmP8BXKuxIG5kc9H3PPT': 'file_storage/call_uzlclmP8BXKuxIG5kc9H3PPT.json', 'var_call_9gMllwg57ASxVKEedaB7F2TU': 'file_storage/call_9gMllwg57ASxVKEedaB7F2TU.json', 'var_call_s5NazNwpXQA6fV8exHEFyCJ7': 'file_storage/call_s5NazNwpXQA6fV8exHEFyCJ7.json'}

exec(code, env_args)
