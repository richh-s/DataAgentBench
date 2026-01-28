code = """# Get the stored results
stockinfo_result = locals()['var_functions.query_db:2']
stocktrade_tables = locals()['var_functions.list_db:0']

# Load data if they are file paths
import json
if isinstance(stockinfo_result, str) and stockinfo_result.endswith('.json'):
    with open(stockinfo_result, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = stockinfo_result

if isinstance(stocktrade_tables, str) and stocktrade_tables.endswith('.json'):
    with open(stocktrade_tables, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = stocktrade_tables

# Filter for valid tickers and clean them (remove problematic ones)
raw_tickers = [row['Symbol'] for row in stockinfo_data]
valid_tickers = []
company_lookup = {}

for ticker in raw_tickers:
    # Check if ticker exists as a table and doesn't contain problematic characters
    if ticker in trade_tables:
        # Check if ticker can be used in SQL (alphanumeric or standard chars only)
        clean_ticker = ticker.replace('#', '').replace('.', '')
        if clean_ticker.isalnum() and len(clean_ticker) > 0:
            valid_tickers.append(clean_ticker)
            # Store original company description
            for row in stockinfo_data:
                if row['Symbol'] == ticker:
                    company_lookup[clean_ticker] = row['Company Description']
                    break

print(f'Valid tickers after cleaning: {len(valid_tickers)}')
print(f'Company lookup entries: {len(company_lookup)}')

# Save for batch processing
with open('/tmp/clean_tickers.json', 'w') as f:
    json.dump(valid_tickers, f)
with open('/tmp/company_lookup.json', 'w') as f:
    json.dump(company_lookup, f)

print('__RESULT__:')
print(json.dumps(valid_tickers[:20]))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB'], 'var_functions.execute_python:10': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.query_db:12': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.execute_python:16': ['\n        SELECT \'AGMH\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "AGMH"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'ALACU\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "ALACU"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'AMHC\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "AMHC"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'ANDA\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "ANDA"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'APEX\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "APEX"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'BCLI\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "BCLI"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'BHAT\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "BHAT"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'BIOC\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "BIOC"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'BKYI\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "BKYI"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         UNION ALL \n        SELECT \'BLFS\' as ticker, \n               COUNT(*) as high_vol_days\n        FROM "BLFS"\n        WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'\n          AND (High - Low) > (0.20 * Low)\n         ORDER BY high_vol_days DESC'], 'var_functions.query_db:18': [{'ticker': 'BIOC', 'high_vol_days': '21'}, {'ticker': 'BKYI', 'high_vol_days': '16'}, {'ticker': 'APEX', 'high_vol_days': '15'}, {'ticker': 'AGMH', 'high_vol_days': '13'}, {'ticker': 'BHAT', 'high_vol_days': '10'}, {'ticker': 'BCLI', 'high_vol_days': '0'}, {'ticker': 'ALACU', 'high_vol_days': '0'}, {'ticker': 'BLFS', 'high_vol_days': '0'}, {'ticker': 'AMHC', 'high_vol_days': '0'}, {'ticker': 'ANDA', 'high_vol_days': '0'}], 'var_functions.execute_python:20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.execute_python:22': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}

exec(code, env_args)
