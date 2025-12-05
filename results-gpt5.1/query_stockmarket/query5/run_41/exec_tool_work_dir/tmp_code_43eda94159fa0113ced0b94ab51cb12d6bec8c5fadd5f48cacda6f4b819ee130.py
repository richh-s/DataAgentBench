code = """import json, pandas as pd, math
# load stockinfo with company names
with open(var_call_l6S6YV8up1Aj1G0Novs0qmMZ, 'r') as f:
    stockinfo_rows = json.load(f)
info_df = pd.DataFrame(stockinfo_rows)[['Symbol','Company Description']]
# helper to count days for one file path
from pathlib import Path

results = []
# mapping ticker to storage key path for first 4 tickers we queried
file_map = {
    'AGMH': var_call_QuIQvJsuhnM7uLJwGZKzZhdR,
    'ALACU': var_call_jFq7ODC7RL8BgFBK4cAXwHm1,
    'AMHC': var_call_8BtxyelnLsd01BuaHbz7ED7V,
    'ANDA': var_call_NHe4gxp4l6HZtMWNwTtAcmYT,
    'APEX': var_call_SocwiTb6fPrj0urtvpDHFnso
}
for symbol, path in file_map.items():
    if isinstance(path, str) and Path(path).suffix == '.json':
        with open(path, 'r') as f:
            rows = json.load(f)
    else:
        # if it's not a path (e.g., empty result already loaded), handle accordingly
        rows = path if isinstance(path, list) else []
    if not rows:
        count = 0
    else:
        df = pd.DataFrame(rows)
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df = df[df['Low'] > 0]
        count = ((df['High'] - df['Low'])/df['Low'] > 0.2).sum()
    results.append({'Symbol': symbol, 'days': int(count)})
res_df = pd.DataFrame(results)
res_df = res_df.merge(info_df, on='Symbol', how='left')
res_df['Company Name'] = res_df['Company Description'].str.split(' specializes').str[0].str.split(' is ').str[0]
out = res_df[['Symbol','Company Name','days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_waxBfkre9FwRVcLW4RCJmTxC': 'file_storage/call_waxBfkre9FwRVcLW4RCJmTxC.json', 'var_call_l6S6YV8up1Aj1G0Novs0qmMZ': 'file_storage/call_l6S6YV8up1Aj1G0Novs0qmMZ.json', 'var_call_8Pgh7mGk90wiOypUOVLVcNVi': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_QuIQvJsuhnM7uLJwGZKzZhdR': 'file_storage/call_QuIQvJsuhnM7uLJwGZKzZhdR.json', 'var_call_jFq7ODC7RL8BgFBK4cAXwHm1': 'file_storage/call_jFq7ODC7RL8BgFBK4cAXwHm1.json', 'var_call_8BtxyelnLsd01BuaHbz7ED7V': [], 'var_call_NHe4gxp4l6HZtMWNwTtAcmYT': 'file_storage/call_NHe4gxp4l6HZtMWNwTtAcmYT.json', 'var_call_SocwiTb6fPrj0urtvpDHFnso': 'file_storage/call_SocwiTb6fPrj0urtvpDHFnso.json'}

exec(code, env_args)
