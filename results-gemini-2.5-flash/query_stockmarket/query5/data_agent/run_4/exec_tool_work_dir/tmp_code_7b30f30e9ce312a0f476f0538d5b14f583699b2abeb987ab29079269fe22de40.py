code = """import pandas as pd
import json

# Load previous results
combined_results = locals()['var_function-call-17739454075792178903']

# Load the trade data for APEX
with open(locals()['var_function-call-11236866066835752844'], 'r') as f:
    trade_data_apex = json.load(f)

df_apex = pd.DataFrame(trade_data_apex)

# Convert High and Low to numeric, handling potential errors
df_apex['High'] = pd.to_numeric(df_apex['High'], errors='coerce')
df_apex['Low'] = pd.to_numeric(df_apex['Low'], errors='coerce')

# Drop rows where High or Low could not be converted (NaNs)
df_apex.dropna(subset=['High', 'Low'], inplace=True)

# Calculate the condition
condition_met_apex = df_apex[((df_apex['High'] - df_apex['Low']) > (0.20 * df_apex['Low']))]

# Get the count of days for APEX
count_apex = len(condition_met_apex)

combined_results["APEX"] = count_apex

print('__RESULT__:')
print(json.dumps(combined_results))"""

env_args = {'var_function-call-8084294124488648582': 'file_storage/function-call-8084294124488648582.json', 'var_function-call-14333136882994226211': 'file_storage/function-call-14333136882994226211.json', 'var_function-call-14681841645696408339': 'file_storage/function-call-14681841645696408339.json', 'var_function-call-10898836939279060557': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP'], 'var_function-call-5775062848617990368': 'file_storage/function-call-5775062848617990368.json', 'var_function-call-14290332882040760628': {'AGMH': 13}, 'var_function-call-18110586330228921517': 'file_storage/function-call-18110586330228921517.json', 'var_function-call-6461527100016119033': {'AGMH': 13, 'ALACU': 0}, 'var_function-call-8397212575487155319': [], 'var_function-call-15518513994007223203': {'AGMH': 13, 'ALACU': 0, 'AMHC': 0}, 'var_function-call-2808238922415498300': 'file_storage/function-call-2808238922415498300.json', 'var_function-call-17739454075792178903': {'AGMH': 13, 'ALACU': 0, 'AMHC': 0, 'ANDA': 0}, 'var_function-call-11236866066835752844': 'file_storage/function-call-11236866066835752844.json'}

exec(code, env_args)
