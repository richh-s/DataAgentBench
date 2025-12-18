code = """import pandas as pd
import json

# Load the NASDAQ Capital Market companies data
with open(locals()['var_function-call-8236297757999139947'], 'r') as f:
    companies_data = json.load(f)
company_symbols = companies_data['company_symbols']
company_names = companies_data['company_names']

# Load AGMH stock trade data
with open(locals()['var_function-call-17176059364584139391'], 'r') as f:
    stock_data_agmh = json.load(f)

df_agmh = pd.DataFrame(stock_data_agmh)
df_agmh['High'] = pd.to_numeric(df_agmh['High'])
df_agmh['Low'] = pd.to_numeric(df_agmh['Low'])

# Calculate the condition
df_agmh['RangeExceeds20Percent'] = (df_agmh['High'] - df_agmh['Low']) > (0.20 * df_agmh['Low'])
count_agmh = int(df_agmh['RangeExceeds20Percent'].sum()) # Convert to int

# Prepare the result for AGMH and the remaining symbols to process
processed_results = [{'Symbol': 'AGMH', 'Count': count_agmh}]
remaining_symbols = company_symbols[1:] # All symbols except the first one

print("__RESULT__:")
print(json.dumps({"processed_results": processed_results, "remaining_symbols": remaining_symbols, "company_names": company_names}))"""

env_args = {'var_function-call-283962626027930975': 'file_storage/function-call-283962626027930975.json', 'var_function-call-10251922187524704823': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_function-call-17176059364584139391': 'file_storage/function-call-17176059364584139391.json', 'var_function-call-8236297757999139947': 'file_storage/function-call-8236297757999139947.json'}

exec(code, env_args)
