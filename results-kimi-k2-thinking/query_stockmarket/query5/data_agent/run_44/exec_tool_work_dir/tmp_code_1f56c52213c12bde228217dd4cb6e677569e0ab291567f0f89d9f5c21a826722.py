code = """import json

# Get all clean tickers
all_tickers = locals()['var_functions.execute_python:10']

# Process in batches to avoid overwhelming the database
batch_size = 50
all_results = []

for batch_start in range(0, min(len(all_tickers), 200), batch_size):  # Process first 200 tickers
    batch = all_tickers[batch_start:batch_start + batch_size]
    
    # Create queries for this batch
    queries = []
    for ticker in batch:
        query = f'''
        SELECT '{ticker}' as ticker, 
               COUNT(*) as high_vol_days
        FROM "{ticker}"
        WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'
          AND (High - Low) > (0.20 * Low)
        '''
        queries.append(query)
    
    # Combine with UNION ALL
    combined_query = ' UNION ALL '.join(queries) + ' ORDER BY high_vol_days DESC'
    
    all_results.append(combined_query)

print('__RESULT__:')
print(json.dumps(all_results[:3]))  # Show first 3 queries"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB'], 'var_functions.execute_python:10': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}]}

exec(code, env_args)
