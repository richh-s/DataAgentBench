code = """import json
import pandas as pd

# Load the overall state from the previous step
with open(locals()['var_function-call-7828986226260441911'], 'r') as f:
    data = json.load(f)

symbol_to_company_map = data['symbol_to_company_map']
all_symbols_list = data['all_symbols_list']
volatility_counts = data['volatility_counts']
current_processing_index = data['current_processing_index']

# Get the current symbol to process
current_symbol = all_symbols_list[current_processing_index]

# Load the stock trade data for the current symbol
with open(locals()['var_function-call-8111415431269354460'], 'r') as f:
    stock_data = json.load(f)

if stock_data:
    df = pd.DataFrame(stock_data)
    df['High'] = pd.to_numeric(df['High'])
    df['Low'] = pd.to_numeric(df['Low'])

    # Calculate the price range and percentage
    df['Range'] = df['High'] - df['Low']
    df['Range_Percent_of_Low'] = (df['Range'] / df['Low']) * 100

    # Count days where the range exceeded 20% of the low price
    volatile_days_count = df[df['Range_Percent_of_Low'] > 20].shape[0]
else:
    volatile_days_count = 0 # No data, so 0 volatile days

# Update volatility_counts for the current symbol
volatility_counts[current_symbol] = volatile_days_count

# Increment the processing index
current_processing_index += 1

# Prepare the updated state for the next iteration
updated_data = {
    "symbol_to_company_map": symbol_to_company_map,
    "all_symbols_list": all_symbols_list,
    "volatility_counts": volatility_counts,
    "current_processing_index": current_processing_index
}

print("__RESULT__:")
print(json.dumps(updated_data))"""

env_args = {'var_function-call-8766194803121634073': 'file_storage/function-call-8766194803121634073.json', 'var_function-call-9793638029078928735': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_function-call-15354975322050721159': 'file_storage/function-call-15354975322050721159.json', 'var_function-call-7124253353373534264': 'file_storage/function-call-7124253353373534264.json', 'var_function-call-6716638884988876037': 'AGMH', 'var_function-call-15052622844809232288': 'file_storage/function-call-15052622844809232288.json', 'var_function-call-5589474846248085487': 'file_storage/function-call-5589474846248085487.json', 'var_function-call-1630190946285422547': 'ALACU', 'var_function-call-2082428859144401488': 'file_storage/function-call-2082428859144401488.json', 'var_function-call-4862821447373348263': 'file_storage/function-call-4862821447373348263.json', 'var_function-call-8974616772342119342': 'AMHC', 'var_function-call-17619054041370918647': [], 'var_function-call-8302530347764829921': 'file_storage/function-call-8302530347764829921.json', 'var_function-call-17300402841462973553': 'ANDA', 'var_function-call-12611247074743606965': 'file_storage/function-call-12611247074743606965.json', 'var_function-call-7828986226260441911': 'file_storage/function-call-7828986226260441911.json', 'var_function-call-1445233854669907742': 'APEX', 'var_function-call-8111415431269354460': 'file_storage/function-call-8111415431269354460.json'}

exec(code, env_args)
