code = """import json

# Read the result file using locals()
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    nyse_stocks = json.load(f)

print(f"Total NYSE non-ETF stocks: {len(nyse_stocks)}")
print(f"First few stocks: {[s['Symbol'] for s in nyse_stocks[:10]]}")

# Create a mapping of symbol to company name
symbol_to_company = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    # Extract company name from description (usually before the first period or comma)
    desc = stock['Company Description']
    company_name = desc.split('.')[0].split(',')[0]
    symbol_to_company[symbol] = company_name

print(f"Sample company names: {list(symbol_to_company.items())[:5]}")

# Save the symbol list and mapping to file for later use
with open('nyse_stocks_data.json', 'w') as f:
    json.dump({
        'symbols': [s['Symbol'] for s in nyse_stocks],
        'symbol_to_company': symbol_to_company
    }, f)

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(nyse_stocks),
    'sample_symbols': [s['Symbol'] for s in nyse_stocks[:10]],
    'sample_companies': dict(list(symbol_to_company.items())[:5])
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
