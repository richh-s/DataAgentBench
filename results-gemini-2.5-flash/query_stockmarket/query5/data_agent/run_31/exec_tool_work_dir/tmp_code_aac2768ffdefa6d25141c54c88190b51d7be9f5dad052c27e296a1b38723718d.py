code = """import json
import pandas as pd

# Load volatile days count from previous steps
volatile_days_count = locals()['var_function-call-15375647505187282629']

# Data for ANDA
anda_data_path = locals()['var_function-call-13471735405130793187']
with open(anda_data_path, 'r') as f:
    anda_data = json.load(f)

df_anda = pd.DataFrame(anda_data)
df_anda['High'] = pd.to_numeric(df_anda['High'])
df_anda['Low'] = pd.to_numeric(df_anda['Low'])

# Calculate intraday price range and check condition for ANDA
df_anda['Intraday_Range'] = df_anda['High'] - df_anda['Low']
df_anda['Volatile'] = df_anda['Intraday_Range'] > (0.20 * df_anda['Low'])

volatile_days_count['ANDA'] = int(df_anda['Volatile'].sum())

print('__RESULT__:')
print(json.dumps(volatile_days_count))"""

env_args = {'var_function-call-12975220063519284981': 'file_storage/function-call-12975220063519284981.json', 'var_function-call-2114712205295823325': 'file_storage/function-call-2114712205295823325.json', 'var_function-call-2856734424882258224': 'file_storage/function-call-2856734424882258224.json', 'var_function-call-18319158053812733066': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7123036960100718841': 'file_storage/function-call-7123036960100718841.json', 'var_function-call-370178781709409324': {'AGMH': 13}, 'var_function-call-4302403561453568801': 'file_storage/function-call-4302403561453568801.json', 'var_function-call-15375647505187282629': {'AGMH': 13, 'ALACU': 0}, 'var_function-call-3896441172473427910': [], 'var_function-call-13471735405130793187': 'file_storage/function-call-13471735405130793187.json'}

exec(code, env_args)
