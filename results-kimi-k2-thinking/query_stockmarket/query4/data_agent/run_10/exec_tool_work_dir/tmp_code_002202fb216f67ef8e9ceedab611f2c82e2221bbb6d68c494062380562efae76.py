code = """import json

# Load the NYSE non-ETF stocks
nyse_stocks_file = locals()['var_functions.query_db:0']
with open(nyse_stocks_file, 'r') as f:
    nyse_stocks = json.load(f)

# Create a list of (symbol, company_name) tuples for tracking
stock_data = []
for stock in nyse_stocks:
    symbol = stock['Symbol']
    # Parse company name from description (usually first part before punctuation)
    desc = stock['Company Description']
    company_name = desc.split(',')[0].split('.')[0].split(' specializes')[0].split(' is')[0].strip()
    stock_data.append((symbol, company_name))

print('__RESULT__:')
print(json.dumps({
    'stocks_to_analyze': len(stock_data),
    'sample_stocks': stock_data[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:10': {'total_nyse_stocks': 234, 'total_available_tables': 2753, 'common_stocks_count': 234, 'sample_common_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}}

exec(code, env_args)
