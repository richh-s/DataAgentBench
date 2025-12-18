code = """import json
import pandas as pd

company_symbols_list = locals()['var_function-call-6804724789592673096']
company_qualifying_days = json.loads(locals()['var_function-call-3328176004751353536'])

# Process ALACU data
alacu_data = json.loads(open(locals()['var_function-call-14922156254793714471'], 'r').read())
df_alacu = pd.DataFrame(alacu_data)
df_alacu['High'] = pd.to_numeric(df_alacu['High'])
df_alacu['Low'] = pd.to_numeric(df_alacu['Low'])

df_alacu['PriceRange'] = df_alacu['High'] - df_alacu['Low']
df_alacu['Exceeds20Percent'] = df_alacu['PriceRange'] > (0.20 * df_alacu['Low'])

qualifying_days_count_alacu = df_alacu['Exceeds20Percent'].sum()
company_qualifying_days['ALACU'] = int(qualifying_days_count_alacu)

print("__RESULT__:")
print(json.dumps(company_qualifying_days))"""

env_args = {'var_function-call-18240726851913256334': 'file_storage/function-call-18240726851913256334.json', 'var_function-call-6804724789592673096': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-18430556799260566247': 'file_storage/function-call-18430556799260566247.json', 'var_function-call-3328176004751353536': {'AGMH': 13}, 'var_function-call-14922156254793714471': 'file_storage/function-call-14922156254793714471.json'}

exec(code, env_args)
