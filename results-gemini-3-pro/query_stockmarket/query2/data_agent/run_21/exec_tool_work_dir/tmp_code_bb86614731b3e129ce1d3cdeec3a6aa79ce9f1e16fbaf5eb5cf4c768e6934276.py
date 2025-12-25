code = """import json

# Load symbols and tables
with open(locals()['var_function-call-9917169383885839858'], 'r') as f:
    stockinfo_results = json.load(f)
candidate_symbols = set(item['Symbol'] for item in stockinfo_results)

with open(locals()['var_function-call-12815242675246571232'], 'r') as f:
    trade_tables = json.load(f)
available_tables = set(trade_tables)

intersection = sorted(list(candidate_symbols.intersection(available_tables)))

# Create batches
batch_size = 100
batches = [intersection[i:i + batch_size] for i in range(0, len(intersection), batch_size)]

queries = []
for batch in batches:
    sub_queries = []
    for sym in batch:
        # Check if table exists (it should, based on intersection)
        # Quote symbol in case of keywords or special chars
        sub_queries.append(f"SELECT '{sym}' as Symbol FROM \"{sym}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1")
    
    full_query = " UNION ALL ".join(sub_queries)
    queries.append(full_query)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-13690384345775752249': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9917169383885839858': 'file_storage/function-call-9917169383885839858.json', 'var_function-call-12815242675246571232': 'file_storage/function-call-12815242675246571232.json', 'var_function-call-18203547688103422521': {'count': 1435, 'sample': ['AXJL', 'PHYS', 'BUYN', 'SCAP', 'FXR', 'AUSF', 'EGPT', 'FEZ', 'KMED', 'JPGE', 'IDHQ', 'RUSL', 'IAK', 'EWJ', 'KBA', 'GDXJ', 'IQSU', 'EFAX', 'URTH', 'JPNL']}, 'var_function-call-323069020816069390': [{'Date': '2006-06-16'}, {'Date': '2006-06-19'}, {'Date': '2006-06-20'}, {'Date': '2006-06-21'}, {'Date': '2006-06-22'}]}

exec(code, env_args)
