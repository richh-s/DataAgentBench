code = """import json
import pandas as pd

# Load company descriptions (from var_function-call-11911564824207130467)
with open(locals()['var_function-call-11911564824207130467'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)
company_descriptions = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}
all_symbols = [company['Symbol'] for company in nasdaq_capital_market_companies]

# Load cumulative results from previous steps
cumulative_results = locals()['var_function-call-13291233267412575243']

# Add AMHC with 0 days (from var_function-call-15045611276644467592, which was empty)
cumulative_results['AMHC'] = 0

# Process ANDA data (from var_function-call-15081348486060618800)
with open(locals()['var_function-call-15081348486060618800'], 'r') as f:
    anda_data = json.load(f)

df_anda = pd.DataFrame(anda_data)
df_anda['High'] = pd.to_numeric(df_anda['High'])
df_anda['Low'] = pd.to_numeric(df_anda['Low'])

df_anda['IntradayRange'] = df_anda['High'] - df_anda['Low']
df_anda['ConditionMet'] = df_anda['IntradayRange'] > (0.20 * df_anda['Low'])
anda_count = df_anda['ConditionMet'].sum()

cumulative_results['ANDA'] = int(anda_count)

# Now, let's identify the next symbol to process. We will get the list of all symbols,
# find which ones have already been processed, and then pick the next one.

processed_symbols = list(cumulative_results.keys())

# Find the first symbol that has not been processed yet
next_symbol_to_process = None
for symbol in all_symbols:
    if symbol not in processed_symbols:
        next_symbol_to_process = symbol
        break

print('__RESULT__:')
print(json.dumps({
    'cumulative_results': cumulative_results,
    'next_symbol_to_process': next_symbol_to_process
}))"""

env_args = {'var_function-call-11911564824207130467': 'file_storage/function-call-11911564824207130467.json', 'var_function-call-5942018615630211563': {'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'company_descriptions_len': 86}, 'var_function-call-275375806334431831': 'file_storage/function-call-275375806334431831.json', 'var_function-call-12707853397130395981': {'AGMH': 13}, 'var_function-call-13279977228652488357': 'file_storage/function-call-13279977228652488357.json', 'var_function-call-13291233267412575243': {'AGMH': 13, 'ALACU': 0}, 'var_function-call-15045611276644467592': [], 'var_function-call-15081348486060618800': 'file_storage/function-call-15081348486060618800.json'}

exec(code, env_args)
