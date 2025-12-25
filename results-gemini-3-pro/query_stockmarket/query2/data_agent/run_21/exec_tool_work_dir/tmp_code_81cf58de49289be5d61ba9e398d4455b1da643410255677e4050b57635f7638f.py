code = """import json

stock_file = locals()['var_function-call-9917169383885839858']
trade_file = locals()['var_function-call-12815242675246571232']

with open(stock_file, 'r') as f:
    stockinfo_results = json.load(f)

with open(trade_file, 'r') as f:
    trade_tables = json.load(f)

candidate_symbols = set([item['Symbol'] for item in stockinfo_results])
available_tables = set(trade_tables)
intersection = sorted(list(candidate_symbols.intersection(available_tables)))

batch_size = 200
queries = []

for i in range(0, len(intersection), batch_size):
    batch = intersection[i:i+batch_size]
    sub_queries = []
    for sym in batch:
        # Use simple string concatenation
        q = "SELECT '" + sym + "' as Symbol FROM \"" + sym + "\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json', 'var_function-call-18203547688103422521': {'count': 1435, 'sample': ['AXJL', 'PHYS', 'BUYN', 'SCAP', 'FXR', 'AUSF', 'EGPT', 'FEZ', 'KMED', 'JPGE', 'IDHQ', 'RUSL', 'IAK', 'EWJ', 'KBA', 'GDXJ', 'IQSU', 'EFAX', 'URTH', 'JPNL']}, 'var_function-call-323069020816069390': [{'Date': '2006-06-16'}, {'Date': '2006-06-19'}, {'Date': '2006-06-20'}, {'Date': '2006-06-21'}, {'Date': '2006-06-22'}]}

exec(code, env_args)
