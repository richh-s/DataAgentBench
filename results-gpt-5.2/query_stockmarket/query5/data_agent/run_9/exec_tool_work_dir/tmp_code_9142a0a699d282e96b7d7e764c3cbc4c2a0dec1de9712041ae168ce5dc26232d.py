code = """import json, pandas as pd
from pathlib import Path

info = pd.DataFrame(json.loads(Path(var_call_RsghL4UroeHSwUjPcoLqnafK).read_text()))
top = pd.DataFrame(var_call_1DJIS3SKIVwDG4dXzWqC7JOR)

df = top.merge(info, on='Symbol', how='left')
# ensure correct order already in top
name_list = df['company_name'].tolist()

print('__RESULT__:')
print(json.dumps({'names': name_list}))"""

env_args = {'var_call_RsghL4UroeHSwUjPcoLqnafK': 'file_storage/call_RsghL4UroeHSwUjPcoLqnafK.json', 'var_call_cgAd9NGNcdGgSVnLuC0reEW1': {'n_symbols': 86, 'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']], 'n_chunks': 1}, 'var_call_hafkDQXR6rEtIs35wsOfOvpJ': 'file_storage/call_hafkDQXR6rEtIs35wsOfOvpJ.json', 'var_call_2IuPSKh2AsXgrQI0liq6Xn2q': {'valid_n': 86, 'missing_n': 0, 'valid': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'missing_preview': []}, 'var_call_z5DKeBOrSwX7hxhm2pTGIiZj': {'s': "SELECT 'T' AS Symbol"}, 'var_call_u1ZAmhu81KOu7Ll8pH6TgYKx': [{'Symbol': 'AGMH', 'days_over_20pct': '13'}], 'var_call_1DJIS3SKIVwDG4dXzWqC7JOR': [{'Symbol': 'SES', 'days_over_20pct': '51'}, {'Symbol': 'GLG', 'days_over_20pct': '42'}, {'Symbol': 'TMSR', 'days_over_20pct': '40'}, {'Symbol': 'VERB', 'days_over_20pct': '38'}, {'Symbol': 'SNSS', 'days_over_20pct': '32'}]}

exec(code, env_args)
