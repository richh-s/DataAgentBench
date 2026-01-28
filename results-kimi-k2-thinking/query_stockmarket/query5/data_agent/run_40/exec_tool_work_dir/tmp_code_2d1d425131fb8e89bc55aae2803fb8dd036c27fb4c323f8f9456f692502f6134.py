code = """# Access the result from the previous query directly
# The result is stored in var_functions.query_db:0
companies_data = var_functions.query_db:0

# Extract ticker symbols for NASDAQ Capital Market companies
tickers = [company['Symbol'] for company in companies_data]

print('__RESULT__:')
print(json.dumps({
    'total_companies': len(tickers),
    'sample_tickers': tickers[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
