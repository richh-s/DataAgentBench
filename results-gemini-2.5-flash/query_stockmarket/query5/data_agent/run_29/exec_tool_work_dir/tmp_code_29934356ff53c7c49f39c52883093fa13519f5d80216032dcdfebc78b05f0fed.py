code = """import json
import pandas as pd

# Load company descriptions (from var_function-call-11911564824207130467)
with open(locals()['var_function-call-11911564824207130467'], 'r') as f:
    nasdaq_capital_market_companies = json.load(f)
company_descriptions = {company['Symbol']: company['Company Description'] for company in nasdaq_capital_market_companies}
all_symbols = [company['Symbol'] for company in nasdaq_capital_market_companies]

# Load cumulative results from previous steps
cumulative_results_previous = locals()['var_function-call-6357213891082193836']['cumulative_results']

# Process BCLI data (from var_function-call-9220443953633111065)
with open(locals()['var_function-call-9220443953633111065'], 'r') as f:
    bcli_data = json.load(f)

df_bcli = pd.DataFrame(bcli_data)
df_bcli['High'] = pd.to_numeric(df_bcli['High'])
df_bcli['Low'] = pd.to_numeric(df_bcli['Low'])

df_bcli['IntradayRange'] = df_bcli['High'] - df_bcli['Low']
df_bcli['ConditionMet'] = df_bcli['IntradayRange'] > (0.20 * df_bcli['Low'])
bcli_count = df_bcli['ConditionMet'].sum()

cumulative_results = cumulative_results_previous
cumulative_results['BCLI'] = int(bcli_count)

# Find the next symbol to process
processed_symbols = list(cumulative_results.keys())
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

env_args = {'var_function-call-11911564824207130467': 'file_storage/function-call-11911564824207130467.json', 'var_function-call-5942018615630211563': {'symbols_preview': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'company_descriptions_len': 86}, 'var_function-call-275375806334431831': 'file_storage/function-call-275375806334431831.json', 'var_function-call-12707853397130395981': {'AGMH': 13}, 'var_function-call-13279977228652488357': 'file_storage/function-call-13279977228652488357.json', 'var_function-call-13291233267412575243': {'AGMH': 13, 'ALACU': 0}, 'var_function-call-15045611276644467592': [], 'var_function-call-15081348486060618800': 'file_storage/function-call-15081348486060618800.json', 'var_function-call-13965416415603185504': {'cumulative_results': {'AGMH': 13, 'ALACU': 0, 'AMHC': 0, 'ANDA': 0}, 'next_symbol_to_process': 'APEX'}, 'var_function-call-10873948017207067572': 'file_storage/function-call-10873948017207067572.json', 'var_function-call-6357213891082193836': {'cumulative_results': {'AGMH': 13, 'ALACU': 0, 'AMHC': 0, 'ANDA': 0, 'APEX': 15}, 'next_symbol_to_process': 'BCLI'}, 'var_function-call-9220443953633111065': 'file_storage/function-call-9220443953633111065.json'}

exec(code, env_args)
