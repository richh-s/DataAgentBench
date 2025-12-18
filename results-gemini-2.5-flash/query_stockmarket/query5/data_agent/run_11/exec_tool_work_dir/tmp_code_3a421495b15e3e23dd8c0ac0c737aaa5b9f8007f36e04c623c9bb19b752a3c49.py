code = """import pandas as pd
import json

# Load data from the previous step
with open(locals()['var_function-call-6528465947413322979'], 'r') as f:
    previous_data = json.load(f)
processed_results = previous_data['processed_results']
remaining_symbols = previous_data['remaining_symbols']
company_names = previous_data['company_names']

# Load ALACU stock trade data
with open(locals()['var_function-call-820333277377655722'], 'r') as f:
    stock_data_alacu = json.load(f)

df_alacu = pd.DataFrame(stock_data_alacu)
df_alacu['High'] = pd.to_numeric(df_alacu['High'])
df_alacu['Low'] = pd.to_numeric(df_alacu['Low'])

# Calculate the condition for ALACU
df_alacu['RangeExceeds20Percent'] = (df_alacu['High'] - df_alacu['Low']) > (0.20 * df_alacu['Low'])
count_alacu = int(df_alacu['RangeExceeds20Percent'].sum())

# Append ALACU's result and update remaining symbols
processed_results.append({'Symbol': 'ALACU', 'Count': count_alacu})
next_remaining_symbols = remaining_symbols[1:]

print("__RESULT__:")
print(json.dumps({"processed_results": processed_results, "remaining_symbols": next_remaining_symbols, "company_names": company_names}))"""

env_args = {'var_function-call-283962626027930975': 'file_storage/function-call-283962626027930975.json', 'var_function-call-10251922187524704823': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_function-call-17176059364584139391': 'file_storage/function-call-17176059364584139391.json', 'var_function-call-8236297757999139947': 'file_storage/function-call-8236297757999139947.json', 'var_function-call-6528465947413322979': 'file_storage/function-call-6528465947413322979.json', 'var_function-call-820333277377655722': 'file_storage/function-call-820333277377655722.json'}

exec(code, env_args)
