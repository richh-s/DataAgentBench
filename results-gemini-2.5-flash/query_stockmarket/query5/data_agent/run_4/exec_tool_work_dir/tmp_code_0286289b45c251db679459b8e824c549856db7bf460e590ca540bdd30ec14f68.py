code = """import pandas as pd
import json

# Load the trade data for AGMH
with open(locals()['var_function-call-5775062848617990368'], 'r') as f:
    trade_data_agmh = json.load(f)

df_agmh = pd.DataFrame(trade_data_agmh)

# Convert High and Low to numeric, handling potential errors
df_agmh['High'] = pd.to_numeric(df_agmh['High'], errors='coerce')
df_agmh['Low'] = pd.to_numeric(df_agmh['Low'], errors='coerce')

# Drop rows where High or Low could not be converted (NaNs)
df_agmh.dropna(subset=['High', 'Low'], inplace=True)

# Calculate the condition
condition_met_agmh = df_agmh[((df_agmh['High'] - df_agmh['Low']) > (0.20 * df_agmh['Low']))]

# Get the count of days for AGMH
count_agmh = len(condition_met_agmh)

print('__RESULT__:')
print(json.dumps({"AGMH": count_agmh}))"""

env_args = {'var_function-call-8084294124488648582': 'file_storage/function-call-8084294124488648582.json', 'var_function-call-14333136882994226211': 'file_storage/function-call-14333136882994226211.json', 'var_function-call-14681841645696408339': 'file_storage/function-call-14681841645696408339.json', 'var_function-call-10898836939279060557': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'var_function-call-5775062848617990368': 'file_storage/function-call-5775062848617990368.json'}

exec(code, env_args)
