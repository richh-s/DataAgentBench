code = """import json
import pandas as pd

# Load the state from the previous execute_python call
with open(locals()['var_function-call-13225210934130833174'], 'r') as f:
    previous_state = json.load(f)

remaining_companies_data = previous_state['remaining_companies_data']
processed_results = previous_state['processed_results']
current_symbol_being_processed = previous_state['current_symbol_to_query'] # This is AMHC
current_company_description = previous_state['current_company_description']

# Load the trade data for the current company being processed (AMHC)
trade_data = locals()['var_function-call-8740453131125531816']

df = pd.DataFrame(trade_data)

# Convert High and Low to numeric, handling potential errors and non-numeric values
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Drop rows where High or Low are NaN after conversion
df.dropna(subset=['High', 'Low'], inplace=True)

# Calculate the number of days where (High - Low) > 0.20 * Low
if not df.empty:
    high_volatility_days = df[((df['High'] - df['Low']) > 0.20 * df['Low'])]
    num_high_volatility_days = len(high_volatility_days)
else:
    num_high_volatility_days = 0

# Add the result for the current company to processed_results
processed_results.append({
    'Symbol': current_symbol_being_processed,
    'Company Description': current_company_description,
    'High Volatility Days': num_high_volatility_days
})

# Determine the next company to query
next_symbol_to_query = None
next_company_description = None

if remaining_companies_data:
    next_company = remaining_companies_data.pop(0) # Get the next company
    next_symbol_to_query = next_company['Symbol']
    next_company_description = next_company['Company Description']

# Prepare the next state to be passed along
next_state = {
    'current_symbol_to_query': next_symbol_to_query, # This will be the symbol for the *next* query_db call
    'current_company_description': next_company_description,
    'remaining_companies_data': remaining_companies_data,
    'processed_results': processed_results
}

print('__RESULT__:')
print(json.dumps(next_state))"""

env_args = {'var_function-call-10606879208005705623': 'file_storage/function-call-10606879208005705623.json', 'var_function-call-5006231330407324082': 'file_storage/function-call-5006231330407324082.json', 'var_function-call-12093674199534092182': 'file_storage/function-call-12093674199534092182.json', 'var_function-call-74415732055014234': 'file_storage/function-call-74415732055014234.json', 'var_function-call-12167668241041808487': 'file_storage/function-call-12167668241041808487.json', 'var_function-call-8932020572609759944': 'file_storage/function-call-8932020572609759944.json', 'var_function-call-13225210934130833174': 'file_storage/function-call-13225210934130833174.json', 'var_function-call-8740453131125531816': []}

exec(code, env_args)
