code = """import json

# Load the current state
with open(locals()['var_function-call-2976895715951625902'], 'r') as f:
    state = json.load(f)

all_companies_intraday_range_data = state['all_companies_intraday_range_data']
symbol_to_description = state['symbol_to_description']
all_symbols = state['all_symbols']

# Process the data for the current symbol (AMHC), which was queried in var_function-call-12349534778468379365
current_symbol = state['next_symbol_to_query']
stock_data_current_symbol = locals()['var_function-call-12349534778468379365']

day_count = 0
for record in stock_data_current_symbol:
    high = float(record['High'])
    low = float(record['Low'])
    if low > 0 and (high - low) / low > 0.20: # Ensure low is not zero to avoid division by zero
        day_count += 1

all_companies_intraday_range_data.append({'symbol': current_symbol, 'count': day_count})

# Determine the next symbol to query
current_symbol_index = all_symbols.index(current_symbol)
next_symbol_index = current_symbol_index + 1

next_symbol_to_query = None
if next_symbol_index < len(all_symbols):
    next_symbol_to_query = all_symbols[next_symbol_index]

print("__RESULT__:")
print(json.dumps({
    'all_companies_intraday_range_data': all_companies_intraday_range_data,
    'next_symbol_to_query': next_symbol_to_query,
    'symbol_to_description': symbol_to_description,
    'all_symbols': all_symbols
}))"""

env_args = {'var_function-call-10635938268862818382': 'file_storage/function-call-10635938268862818382.json', 'var_function-call-7512712772181424858': 'file_storage/function-call-7512712772181424858.json', 'var_function-call-14575303271704160794': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7698664705107236352': 'file_storage/function-call-7698664705107236352.json', 'var_function-call-5390203662496531257': 'file_storage/function-call-5390203662496531257.json', 'var_function-call-8796463335682772801': 'file_storage/function-call-8796463335682772801.json', 'var_function-call-10882724012973181006': 'file_storage/function-call-10882724012973181006.json', 'var_function-call-9742123529145069746': 'file_storage/function-call-9742123529145069746.json', 'var_function-call-11049086404300196738': {'count': 86, 'first_five_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'last_five_symbols': ['VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'all_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_function-call-4932084830650739945': 'file_storage/function-call-4932084830650739945.json', 'var_function-call-4372485336932054191': {'symbol': 'AGMH', 'count': 13}, 'var_function-call-12711188421763189926': 'file_storage/function-call-12711188421763189926.json', 'var_function-call-9505908982906908764': 'file_storage/function-call-9505908982906908764.json', 'var_function-call-2976895715951625902': 'file_storage/function-call-2976895715951625902.json', 'var_function-call-12349534778468379365': []}

exec(code, env_args)
