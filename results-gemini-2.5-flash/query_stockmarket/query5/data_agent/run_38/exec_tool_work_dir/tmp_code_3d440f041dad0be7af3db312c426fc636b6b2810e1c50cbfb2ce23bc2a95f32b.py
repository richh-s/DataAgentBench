code = """import json

# Load NASDAQ Capital Market symbols
with open(locals()['var_function-call-7512712772181424858'], 'r') as f:
    nasdaq_capital_market_companies_full_info = json.load(f)

nasdaq_capital_market_symbols = [company['Symbol'] for company in nasdaq_capital_market_companies_full_info]

# Load all table names from stocktrade_database
with open(locals()['var_function-call-8796463335682772801'], 'r') as f:
    stocktrade_tables = json.load(f)

# Filter symbols that exist in stocktrade_database
filtered_symbols = [symbol for symbol in nasdaq_capital_market_symbols if symbol in stocktrade_tables]

# Create a dictionary to map filtered symbols to their company descriptions
symbol_to_description = {
    company['Symbol']: company['Company Description'] 
    for company in nasdaq_capital_market_companies_full_info 
    if company['Symbol'] in filtered_symbols
}

print("__RESULT__:")
print(json.dumps({
    'filtered_symbols': filtered_symbols,
    'symbol_to_description': symbol_to_description
}))"""

env_args = {'var_function-call-10635938268862818382': 'file_storage/function-call-10635938268862818382.json', 'var_function-call-7512712772181424858': 'file_storage/function-call-7512712772181424858.json', 'var_function-call-14575303271704160794': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-7698664705107236352': 'file_storage/function-call-7698664705107236352.json', 'var_function-call-5390203662496531257': 'file_storage/function-call-5390203662496531257.json', 'var_function-call-8796463335682772801': 'file_storage/function-call-8796463335682772801.json'}

exec(code, env_args)
