code = """import json
import os

# Load ETF symbols from file
with open('/tmp/nyse_arca_etfs.json', 'r') as f:
    etf_symbols = json.load(f)

# Process ETFs in batches to find those with Adj Close > 200 in 2015
batch_size = 50
all_results = []

# We'll track progress
num_processed = 0
num_found = 0

print(f'Starting to process {len(etf_symbols)} ETFs...', file=os.sys.stderr)

# Since we need to call query_db for each batch, we'll prepare the batch queries
batch_queries = []
for i in range(0, len(etf_symbols), batch_size):
    batch = etf_symbols[i:i+batch_size]
    union_parts = []
    
    for symbol in batch:
        # Handle special characters in symbol names if needed
        safe_symbol = symbol
        part = f"SELECT '{safe_symbol}' as Symbol FROM \"{safe_symbol}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND \"Adj Close\" > 200 LIMIT 1"
        union_parts.append(part)
    
    if union_parts:
        batch_query = " UNION ALL ".join(union_parts)
        batch_queries.append({
            'batch_num': len(batch_queries) + 1,
            'start_idx': i,
            'end_idx': min(i + batch_size, len(etf_symbols)),
            'query': batch_query,
            'size': len(union_parts)
        })

print(f'Created {len(batch_queries)} batch queries', file=os.sys.stderr)

print('__RESULT__:')
print(json.dumps({
    'total_etfs': len(etf_symbols),
    'batches_created': len(batch_queries),
    'first_batch_query': batch_queries[0]['query'] if batch_queries else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.query_db:6': [], 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [], 'var_functions.list_db:12': 'file_storage/functions.list_db:12.json', 'var_functions.execute_python:14': {'total_nyse_arca_etfs': 1435, 'available_in_stocktrade': 1435, 'available_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_functions.execute_python:16': {'total_etfs_to_check': 1435, 'test_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.query_db:20': [], 'var_functions.execute_python:22': {'total_nyse_arca_etfs': 1435, 'available_as_tables': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.execute_python:24': {'etfs_to_check': 1435, 'first_50_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_functions.execute_python:26': {'etfs_to_check': 1435, 'symbols_file': '/tmp/nyse_arca_etfs.json'}, 'var_functions.execute_python:28': {'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'total_symbols': 1435}, 'var_functions.query_db:32': [], 'var_functions.query_db:34': [{'Adj Close': '125.2300033569336'}, {'Adj Close': '124.4000015258789'}, {'Adj Close': '124.2300033569336'}, {'Adj Close': '124.2300033569336'}, {'Adj Close': '124.1999969482422'}], 'var_functions.execute_python:36': {'total_symbols': 1435, 'num_batches': 15, 'first_batch': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX']}, 'var_functions.query_db:40': [], 'var_functions.execute_python:44': {'total_etfs': 1435, 'batch_size': 50, 'num_batches': 29}, 'var_functions.execute_python:46': {'sample_etfs': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF']}}

exec(code, env_args)
