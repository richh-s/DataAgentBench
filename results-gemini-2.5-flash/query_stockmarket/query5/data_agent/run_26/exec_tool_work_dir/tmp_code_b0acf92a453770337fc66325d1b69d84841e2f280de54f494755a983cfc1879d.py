code = """import json
import pandas as pd

company_symbols_list = locals()['var_function-call-6804724789592673096']

# Initialize a dictionary to store the count of qualifying days for each company
company_qualifying_days = {}

# The previous query was for AGMH. Let's process it correctly.
agmh_data = json.loads(open(locals()['var_function-call-18430556799260566247'], 'r').read())
df = pd.DataFrame(agmh_data)
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

df['PriceRange'] = df['High'] - df['Low']
df['Exceeds20Percent'] = df['PriceRange'] > (0.20 * df['Low'])

qualifying_days_count = df['Exceeds20Percent'].sum()
company_qualifying_days['AGMH'] = int(qualifying_days_count)

print("__RESULT__:")
print(json.dumps(company_qualifying_days))"""

env_args = {'var_function-call-18240726851913256334': 'file_storage/function-call-18240726851913256334.json', 'var_function-call-6804724789592673096': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-18430556799260566247': 'file_storage/function-call-18430556799260566247.json'}

exec(code, env_args)
