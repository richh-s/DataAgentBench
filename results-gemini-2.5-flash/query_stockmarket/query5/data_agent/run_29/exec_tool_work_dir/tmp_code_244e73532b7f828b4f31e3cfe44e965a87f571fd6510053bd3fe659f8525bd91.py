code = """import json
import pandas as pd

# Load the company descriptions
with open(locals()['var_function-call-11911564824207130467'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)
company_descriptions = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}
symbols = [company['Symbol'] for company in nasdaq_capital_market_companies]

# Placeholder for all results, this will be accumulated across steps
# For this step, we will process data for AGMH.

# Process AGMH data
with open(locals()['var_function-call-275375806334431831'], 'r') as f:
    aghm_data = json.load(f)

df_aghm = pd.DataFrame(aghm_data)
df_aghm['High'] = pd.to_numeric(df_aghm['High'])
df_aghm['Low'] = pd.to_numeric(df_aghm['Low'])

df_aghm['IntradayRange'] = df_aghm['High'] - df_aghm['Low']
df_aghm['ConditionMet'] = df_aghm['IntradayRange'] > (0.20 * df_aghm['Low'])
aghm_count = df_aghm['ConditionMet'].sum()

# Initialize or update the overall results list
# In a real scenario, this would be passed between execute_python calls.
# For now, let's just print the result for AGMH.

print('__RESULT__:')
print(json.dumps({'AGMH': int(aghm_count)}))"""

env_args = {'var_function-call-11911564824207130467': 'file_storage/function-call-11911564824207130467.json', 'var_function-call-5942018615630211563': {'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'company_descriptions_len': 86}, 'var_function-call-275375806334431831': 'file_storage/function-call-275375806334431831.json'}

exec(code, env_args)
