code = """import json

# Load the NYSE non-ETF stocks data
nyse_stocks_file = locals()['var_functions.query_db:0']
with open(nyse_stocks_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create a list of symbols to analyze (limit to first 20 for initial testing)
test_symbols = [stock['Symbol'] for stock in nyse_stocks[:20]]

print('__RESULT__:')
print(json.dumps({
    'test_symbols': test_symbols,
    'count': len(test_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:10': {'total_nyse_stocks': 234, 'total_available_tables': 2753, 'common_stocks_count': 234, 'sample_common_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:14': {'stocks_to_analyze': 234, 'sample_stocks': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant'], ['AJRD', 'Aerojet Rocketdyne Holdings'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc'], ['AMP', 'Ameriprise Financial'], ['AMT', 'American Tower Corporation'], ['ARD', 'Ardagh Group S']]}}

exec(code, env_args)
