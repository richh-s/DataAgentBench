code = """import json

# Load stockinfo data
stockinfo_path = locals()['var_functions.query_db:35']
with open(stockinfo_path) as f:
    nasdaq_stocks = json.load(f)

# Build symbol list
symbols = [stock['Symbol'] for stock in nasdaq_stocks]
company_map = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}

print('Loaded', len(symbols), 'symbols')
print('First few:', symbols[:3])

# Build query
def build_query(syms):
    parts = []
    for sym in syms:
        template = 'SELECT "{}" as Symbol, COUNT(*) as days FROM "{}"'.format(sym, sym)
        template += " WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'"
        template += " AND (High - Low) > (Low * 0.20)"
        parts.append(template)
    return ' UNION ALL '.join(parts) + ' ORDER BY days DESC LIMIT 5'

# Test with first 3 symbols
test_symbols = symbols[:3]
test_query = build_query(test_symbols)
print('Test query:', test_query)

print('__RESULT__:')
print(json.dumps({
    'symbol_count': len(symbols),
    'test_query': test_query,
    'symbols': symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:10': {'total_tables': 2753, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}, 'var_functions.execute_python:12': {'nasdaq_capital_count': 86, 'available_in_stocktrade': 86, 'sample_symbols': ['BWEN', 'SSNT', 'HQI', 'FSBW', 'CCCL', 'CUBA', 'WHLM', 'IGIC', 'CPAH', 'FTFT']}, 'var_functions.query_db:14': [{'high_volatility_days': '13'}], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.list_db:36': 'file_storage/functions.list_db:36.json', 'var_functions.execute_python:38': {'length': 14144, 'complete': False}}

exec(code, env_args)
