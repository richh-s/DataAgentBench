code = """import json, pandas as pd, os
# load full AGMH, ALACU, APEX, ANDA data
with open(var_call_ytfgYqE3KOZQE5YB5KA4sfAm) as f:
    agmh = pd.DataFrame(json.load(f))
with open(var_call_15TmSER72if6NVWatOHkbiz6) as f:
    alacu = pd.DataFrame(json.load(f))
with open(var_call_2aKFJrppBcSZNmcr7ilIZeCR) as f:
    anda = pd.DataFrame(json.load(f))
with open(var_call_5IxOnUh62b4MMi18j91cM0fd) as f:
    apex = pd.DataFrame(json.load(f))

stock_days = {}
for sym, df in [('AGMH', agmh), ('ALACU', alacu), ('ANDA', anda), ('APEX', apex)]:
    if df.empty:
        stock_days[sym] = 0
        continue
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    cond = (df['High'] - df['Low']) > 0.2 * df['Low']
    stock_days[sym] = int(cond.sum())

result = json.dumps(stock_days)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_k4caEoQj7lXVlNyqgQlt51Us': 'file_storage/call_k4caEoQj7lXVlNyqgQlt51Us.json', 'var_call_cg7OABKXDhrcOUTOmpYyeuXT': 'file_storage/call_cg7OABKXDhrcOUTOmpYyeuXT.json', 'var_call_kfgsxhEfGOCbYvbvzlxV1njq': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_ytfgYqE3KOZQE5YB5KA4sfAm': 'file_storage/call_ytfgYqE3KOZQE5YB5KA4sfAm.json', 'var_call_15TmSER72if6NVWatOHkbiz6': 'file_storage/call_15TmSER72if6NVWatOHkbiz6.json', 'var_call_27Ia1uy4hWjoN3gMtjkC9QM0': [], 'var_call_2aKFJrppBcSZNmcr7ilIZeCR': 'file_storage/call_2aKFJrppBcSZNmcr7ilIZeCR.json', 'var_call_5IxOnUh62b4MMi18j91cM0fd': 'file_storage/call_5IxOnUh62b4MMi18j91cM0fd.json'}

exec(code, env_args)
