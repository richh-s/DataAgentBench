code = """import json, pandas as pd
best = pd.DataFrame(var_call_welOQWxEHObHsuOCkGWO2YTf)

# load all level=4 definitions
path = var_call_VCmajKGq8mSTRiiaB8WfAP6V
with open(path, 'r', encoding='utf-8') as f:
    defs = pd.DataFrame(json.load(f))

# normalize symbol by removing spaces
if not defs.empty:
    defs['symbol_norm'] = defs['symbol'].astype(str).str.replace(' ', '', regex=False)

best['symbol_norm'] = best['cpc_group_code'].astype(str).str.replace(' ', '', regex=False)
merged = best.merge(defs[['symbol_norm','titleFull']], on='symbol_norm', how='left')

# keep top (highest EMA) - all included, but titles may be missing if not present at level=4
out = merged[['cpc_group_code','titleFull','best_year','best_year_ema']].to_dict('records')
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_aSG8ybRCb4ixYiNVq3wbRnuz': ['publicationinfo'], 'var_call_3h3AEY3yILY4iZor7rW05LOe': ['cpc_definition'], 'var_call_QuYk8va0hnKk9YfK9cVqdFoX': [], 'var_call_RVrtZnIpq649ZJLOK9RTrNTv': 'file_storage/call_RVrtZnIpq649ZJLOK9RTrNTv.json', 'var_call_BPXLwcnU61nKeB0pEzHgTk8V': 'file_storage/call_BPXLwcnU61nKeB0pEzHgTk8V.json', 'var_call_zjFBClOwm2DRLmM4t3iplz5m': 'file_storage/call_zjFBClOwm2DRLmM4t3iplz5m.json', 'var_call_welOQWxEHObHsuOCkGWO2YTf': [{'cpc_group_code': 'C04B2235', 'best_year': 2015, 'best_year_ema': 32.0}, {'cpc_group_code': 'C04B35', 'best_year': 2015, 'best_year_ema': 12.0}, {'cpc_group_code': 'B29C2049', 'best_year': 2007, 'best_year_ema': 9.0}, {'cpc_group_code': 'F02D41', 'best_year': 2010, 'best_year_ema': 5.0}, {'cpc_group_code': 'B29C49', 'best_year': 2007, 'best_year_ema': 5.0}, {'cpc_group_code': 'G02B15', 'best_year': 2016, 'best_year_ema': 5.0}, {'cpc_group_code': 'G02B23', 'best_year': 2016, 'best_year_ema': 5.0}, {'cpc_group_code': 'A61B1', 'best_year': 2016, 'best_year_ema': 3.0}, {'cpc_group_code': 'F23B50', 'best_year': 2018, 'best_year_ema': 3.0}, {'cpc_group_code': 'F24B5', 'best_year': 2018, 'best_year_ema': 3.0}, {'cpc_group_code': 'F23L1', 'best_year': 2018, 'best_year_ema': 3.0}, {'cpc_group_code': 'H01L23', 'best_year': 2008, 'best_year_ema': 3.0}, {'cpc_group_code': 'F23L15', 'best_year': 2018, 'best_year_ema': 3.0}, {'cpc_group_code': 'F16H37', 'best_year': 2009, 'best_year_ema': 2.0}, {'cpc_group_code': 'C09K11', 'best_year': 2015, 'best_year_ema': 2.0}, {'cpc_group_code': 'F16H2200', 'best_year': 2009, 'best_year_ema': 2.0}, {'cpc_group_code': 'H01L2924', 'best_year': 2008, 'best_year_ema': 2.0}, {'cpc_group_code': 'G02B13', 'best_year': 2016, 'best_year_ema': 2.0}, {'cpc_group_code': 'F02M65', 'best_year': 2010, 'best_year_ema': 1.0}, {'cpc_group_code': 'E02F9', 'best_year': 2016, 'best_year_ema': 1.0}, {'cpc_group_code': 'F02D13', 'best_year': 2018, 'best_year_ema': 1.0}, {'cpc_group_code': 'C04B40', 'best_year': 2015, 'best_year_ema': 1.0}, {'cpc_group_code': 'B29C2949', 'best_year': 2007, 'best_year_ema': 1.0}, {'cpc_group_code': 'B66C23', 'best_year': 2016, 'best_year_ema': 1.0}, {'cpc_group_code': 'B63B21', 'best_year': 2014, 'best_year_ema': 1.0}, {'cpc_group_code': 'B60S9', 'best_year': 2016, 'best_year_ema': 1.0}, {'cpc_group_code': 'F02D15', 'best_year': 2018, 'best_year_ema': 1.0}, {'cpc_group_code': 'F16H3', 'best_year': 2009, 'best_year_ema': 1.0}, {'cpc_group_code': 'F23B60', 'best_year': 2018, 'best_year_ema': 1.0}, {'cpc_group_code': 'F23N1', 'best_year': 2018, 'best_year_ema': 1.0}, {'cpc_group_code': 'H01L25', 'best_year': 2008, 'best_year_ema': 1.0}, {'cpc_group_code': 'Y02E20', 'best_year': 2018, 'best_year_ema': 1.0}, {'cpc_group_code': 'Y02T10', 'best_year': 2018, 'best_year_ema': 1.0}], 'var_call_VCmajKGq8mSTRiiaB8WfAP6V': 'file_storage/call_VCmajKGq8mSTRiiaB8WfAP6V.json', 'var_call_q4FHmZMprVdpVu6WcPtBQ1ov': []}

exec(code, env_args)
