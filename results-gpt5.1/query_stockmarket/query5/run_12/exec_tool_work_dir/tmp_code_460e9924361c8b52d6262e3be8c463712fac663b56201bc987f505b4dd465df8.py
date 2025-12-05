code = """import json, pandas as pd, os

files = {
    'AGMH': var_call_WfzsaiZtQu1wVB7JBjJArlPZ,
    'ALACU': var_call_ShrhJukfAi0lRqkyCXQRFdse,
    'ANDA': var_call_EgvibN1jpcRGrKrVScJWZK8y,
    'APEX': var_call_R21PIyPVLUNDrOVmrsVjxfRv,
}

counts = {}
for sym, path in files.items():
    with open(path, 'r') as f:
        data = json.load(f)
    if not data:
        counts[sym] = 0
        continue
    df = pd.DataFrame(data)
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])
    df = df[df['Low'] > 0]
    df['range_pct'] = (df['High'] - df['Low']) / df['Low']
    counts[sym] = int((df['range_pct'] > 0.2).sum())

result = json.dumps(counts)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_MKCZO8UyASEYTa3DHaPWtlrY': 'file_storage/call_MKCZO8UyASEYTa3DHaPWtlrY.json', 'var_call_TuvgO7WoMjeFIKIaHBCJP136': 'file_storage/call_TuvgO7WoMjeFIKIaHBCJP136.json', 'var_call_u2XPW6MSBbIVsREK7YQBJoyf': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_WfzsaiZtQu1wVB7JBjJArlPZ': 'file_storage/call_WfzsaiZtQu1wVB7JBjJArlPZ.json', 'var_call_ShrhJukfAi0lRqkyCXQRFdse': 'file_storage/call_ShrhJukfAi0lRqkyCXQRFdse.json', 'var_call_ZjHoK3dOGyc8hmbn60kzpsQl': [], 'var_call_EgvibN1jpcRGrKrVScJWZK8y': 'file_storage/call_EgvibN1jpcRGrKrVScJWZK8y.json', 'var_call_R21PIyPVLUNDrOVmrsVjxfRv': 'file_storage/call_R21PIyPVLUNDrOVmrsVjxfRv.json'}

exec(code, env_args)
