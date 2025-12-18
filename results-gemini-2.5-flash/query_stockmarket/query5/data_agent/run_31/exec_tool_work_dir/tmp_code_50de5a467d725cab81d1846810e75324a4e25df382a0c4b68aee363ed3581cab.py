code = """import json
import pandas as pd

# Load volatile days count from previous steps
volatile_days_count = locals()['var_function-call-12152989805936117292']

# Data for BCLI
bcli_data_path = locals()['var_function-call-337234948513646432']
with open(bcli_data_path, 'r') as f:
    bcli_data = json.load(f)

df_bcli = pd.DataFrame(bcli_data)
df_bcli['High'] = pd.to_numeric(df_bcli['High'])
df_bcli['Low'] = pd.to_numeric(df_bcli['Low'])

# Calculate intraday price range and check condition for BCLI
df_bcli['Intraday_Range'] = df_bcli['High'] - df_bcli['Low']
df_bcli['Volatile'] = df_bcli['Intraday_Range'] > (0.20 * df_bcli['Low'])

volatile_days_count['BCLI'] = int(df_bcli['Volatile'].sum())

print('__RESULT__:')
print(json.dumps(volatile_days_count))"""

env_args = {'var_function-call-12975220063519284981': 'file_storage/function-call-12975220063519284981.json', 'var_function-call-2114712205295823325': 'file_storage/function-call-2114712205295823325.json', 'var_function-call-2856734424882258224': 'file_storage/function-call-2856734424882258224.json', 'var_function-call-18319158053812733066': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7123036960100718841': 'file_storage/function-call-7123036960100718841.json', 'var_function-call-370178781709409324': {'AGMH': 13}, 'var_function-call-4302403561453568801': 'file_storage/function-call-4302403561453568801.json', 'var_function-call-15375647505187282629': {'AGMH': 13, 'ALACU': 0}, 'var_function-call-3896441172473427910': [], 'var_function-call-13471735405130793187': 'file_storage/function-call-13471735405130793187.json', 'var_function-call-14548557852466081826': {'AGMH': 13, 'ALACU': 0, 'ANDA': 0}, 'var_function-call-15336065438881484871': 'file_storage/function-call-15336065438881484871.json', 'var_function-call-12152989805936117292': {'AGMH': 13, 'ALACU': 0, 'ANDA': 0, 'APEX': 15}, 'var_function-call-337234948513646432': 'file_storage/function-call-337234948513646432.json'}

exec(code, env_args)
