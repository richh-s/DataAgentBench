code = """import json

# Read the full result from the file
result_path = var_stockinfo_query
with open(result_path, 'r') as f:
    stockinfo_data = json.load(f)

# Filter for NASDAQ Capital Market (Market Category = 'S')
capital_market_stocks = []
for row in stockinfo_data:
    # Check if Market Category is 'S'
    if row.get('Market Category') == 'S':
        capital_market_stocks.append({
            'Symbol': row['Symbol'],
            'Company Description': row['Company Description']
        })

print('__RESULT__:')
print(json.dumps({
    'total_records': len(stockinfo_data),
    'capital_market_count': len(capital_market_stocks),
    'sample_stocks': capital_market_stocks[:10]
}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
