code = """import json
import pandas as pd

# Load relevant symbols and company names
symbols_to_company_names_path = locals()['var_function-call-2114712205295823325']
with open(symbols_to_company_names_path, 'r') as f:
    symbols_to_company_names = json.load(f)

relevant_symbols = locals()['var_function-call-18319158053812733066']

# Initialize a dictionary to store volatile day counts
volatile_days_count = {}

# Data for AGMH as an example from the previous step
agmh_data_path = locals()['var_function-call-7123036960100718841']
with open(agmh_data_path, 'r') as f:
    agmh_data = json.load(f)

df = pd.DataFrame(agmh_data)
df['High'] = pd.to_numeric(df['High'])
df['Low'] = pd.to_numeric(df['Low'])

# Calculate intraday price range and check condition
df['Intraday_Range'] = df['High'] - df['Low']
df['Volatile'] = df['Intraday_Range'] > (0.20 * df['Low'])

volatile_days_count['AGMH'] = df['Volatile'].sum()

print('__RESULT__:')
print(json.dumps(volatile_days_count))"""

env_args = {'var_function-call-12975220063519284981': 'file_storage/function-call-12975220063519284981.json', 'var_function-call-2114712205295823325': 'file_storage/function-call-2114712205295823325.json', 'var_function-call-2856734424882258224': 'file_storage/function-call-2856734424882258224.json', 'var_function-call-18319158053812733066': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7123036960100718841': 'file_storage/function-call-7123036960100718841.json'}

exec(code, env_args)
