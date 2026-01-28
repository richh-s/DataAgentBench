code = """import json
import pandas as pd

# Read AGMH data
agmh_data = locals()['var_functions.query_db:9']
if isinstance(agmh_data, str) and agmh_data.endswith('.json'):
    with open(agmh_data, 'r') as f:
        agmh_data = json.load(f)

# Convert to DataFrame
df_agmh = pd.DataFrame(agmh_data)

# Calculate intraday range and percentage
df_agmh['Intraday_Range'] = df_agmh['High'].astype(float) - df_agmh['Low'].astype(float)
df_agmh['Range_Percent_of_Low'] = (df_agmh['Intraday_Range'] / df_agmh['Low'].astype(float)) * 100

# Count days where range > 20% of low price
volatile_days = df_agmh[df_agmh['Range_Percent_of_Low'] > 20]
volatile_count = len(volatile_days)

print(f"AGMH had {volatile_count} volatile days in 2019")
print(f"Sample volatile days:")
print(volatile_days[['Date', 'Low', 'High', 'Intraday_Range', 'Range_Percent_of_Low']].head())

print("__RESULT__:")
print(json.dumps({"ticker": "AGMH", "volatile_days": volatile_count}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
