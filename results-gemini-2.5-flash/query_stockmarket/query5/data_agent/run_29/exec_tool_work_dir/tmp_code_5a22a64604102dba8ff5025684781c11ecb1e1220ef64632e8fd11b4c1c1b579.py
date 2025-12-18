code = """import json
import pandas as pd

# Load company descriptions (from var_function-call-11911564824207130467)
with open(locals()['var_function-call-11911564824207130467'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)
company_descriptions = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}
symbols = [company['Symbol'] for company in nasdaq_capital_market_companies]

# Initialize or load cumulative results from previous steps
# For the first pass, let's assume this is the starting point for cumulative results
# In subsequent steps, this will be loaded from a previous execute_python output

cumulative_results = {'AGMH': 13} # From var_function-call-12707853397130395981

# Process ALACU data (from var_function-call-13279977228652488357)
with open(locals()['var_function-call-13279977228652488357'], 'r') as f:
    alacu_data = json.load(f)

df_alacu = pd.DataFrame(alacu_data)
df_alacu['High'] = pd.to_numeric(df_alacu['High'])
df_alacu['Low'] = pd.to_numeric(df_alacu['Low'])

df_alacu['IntradayRange'] = df_alacu['High'] - df_alacu['Low']
df_alacu['ConditionMet'] = df_alacu['IntradayRange'] > (0.20 * df_alacu['Low'])
alacu_count = df_alacu['ConditionMet'].sum()

cumulative_results['ALACU'] = int(alacu_count)

print('__RESULT__:')
print(json.dumps(cumulative_results))"""

env_args = {'var_function-call-11911564824207130467': 'file_storage/function-call-11911564824207130467.json', 'var_function-call-5942018615630211563': {'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'company_descriptions_len': 86}, 'var_function-call-275375806334431831': 'file_storage/function-call-275375806334431831.json', 'var_function-call-12707853397130395981': {'AGMH': 13}, 'var_function-call-13279977228652488357': 'file_storage/function-call-13279977228652488357.json'}

exec(code, env_args)
