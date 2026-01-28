code = """import json
import os

# Load ETF symbols
etf_file = locals()['var_functions.query_db:14']
if isinstance(etf_file, str) and os.path.exists(etf_file):
    with open(etf_file, 'r') as f:
        nyse_arca_etfs = json.load(f)
else:
    nyse_arca_etfs = etf_file

symbols = [item['Symbol'] for item in nyse_arca_etfs]

# Create a query to check all symbols at once using UNION ALL
# This will be more efficient than individual queries
queries = []
for symbol in symbols[:1435]:  # Keep all 1435 for completeness
    queries.append(f'''
    SELECT '{symbol}' as Symbol, "Adj Close", Date 
    FROM "{symbol}" 
    WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND "Adj Close" > 200
    ''')

# For DuckDB, we need to limit the query size. Let's create a batch query.
batch_size = 100
all_results = []

for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    batch_queries = []
    for symbol in batch:
        batch_queries.append(f'''
        SELECT '{symbol}' as Symbol, "Adj Close", Date 
        FROM "{symbol}" 
        WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND "Adj Close" > 200
        ''')
    
    if batch_queries:
        union_query = ' UNION ALL '.join(batch_queries)
        all_results.append(union_query)

# Store the batches for execution
with open('/tmp/query_batches.json', 'w') as f:
    json.dump(all_results, f)

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'batches_created': len(all_results),
    'batch_size': batch_size,
    'first_batch_preview': all_results[0][:200] if all_results else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 1435, 'head': [{'Symbol': 'AAAU'}, {'Symbol': 'AADR'}, {'Symbol': 'ABEQ'}, {'Symbol': 'ACSG'}, {'Symbol': 'ACWF'}, {'Symbol': 'AFK'}, {'Symbol': 'AFLG'}, {'Symbol': 'AFMC'}, {'Symbol': 'AFSM'}, {'Symbol': 'AFTY'}]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:8': {'nyse_arca_etf_count': 1435, 'available_tables_count': 2753, 'common_symbols_count': 1435, 'common_symbols_sample': ['LOWC', 'RYZZ', 'PPDM', 'XDIV', 'ZROZ', 'FXY', 'RYE', 'XSOE', 'IYY', 'ERUS']}, 'var_functions.execute_python:10': {'total_symbols': 1435, 'first_20_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:12': {'message': 'Need to query 1435 symbols for 2015 data', 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_nyse_arca_etfs': 1435, 'first_10_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:18': {'status': 'Stored ETF symbols', 'count': 1435}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [], 'var_functions.execute_python:26': {'total_symbols': 1435, 'batch_count': 29, 'first_batch_size': 50, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}}

exec(code, env_args)
