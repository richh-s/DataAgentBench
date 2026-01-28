code = """import json

# Process tickers in batches to avoid too many queries
# Load tickers and mapping
ticker_file = locals()['var_functions.query_db:12']
if isinstance(ticker_file, str):
    with open(ticker_file, 'r') as f:
        capital_market_tickers = json.load(f)
else:
    capital_market_tickers = ticker_file

# Get available tables
all_tables_file = locals()['var_functions.list_db:2']
if isinstance(all_tables_file, str):
    with open(all_tables_file, 'r') as f:
        available_tables = json.load(f)
else:
    available_tables = all_tables_file

# Create list of tickers to analyze
symbol_to_company = {}
for ticker in capital_market_tickers:
    symbol = ticker['Symbol']
    if symbol in available_tables:
        symbol_to_company[symbol] = ticker['Company Description']

tickers_to_analyze = list(symbol_to_company.keys())

# Create queries for first batch
create_queries = []
for i, symbol in enumerate(tickers_to_analyze):
    query = f'SELECT "Date", "High", "Low" FROM "{symbol}" WHERE "Date" >= \'2019-01-01\' AND "Date" <= \'2019-12-31\''
    create_queries.append({"db_name": "stocktrade_database", "query": query, "symbol": symbol})
    if i >= 10:  # Limit batch size
        break

print('__RESULT__:')
print(json.dumps({
    'queries_created': len(create_queries),
    'tickers_remaining': len(tickers_to_analyze) - len(create_queries)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:9': 'Found 86 NASDAQ Capital Market tickers', 'var_functions.execute_python:8': 'Found 2753 total tables in stocktrade_database', 'var_functions.execute_python:10': 'Found 86 NASDAQ Capital Market tickers with data tables', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': 'Loaded 86 NASDAQ Capital Market tickers', 'var_functions.query_db:16': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}, {'Date': '2019-01-09', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}, {'Date': '2019-01-10', 'Open': '27.690000534057617', 'High': '28.149999618530277', 'Low': '27.690000534057617', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '900'}, {'Date': '2019-01-11', 'Open': '28.0', 'High': '28.0', 'Low': '28.0', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '100'}, {'Date': '2019-01-14', 'Open': '28.0', 'High': '28.0', 'Low': '28.0', 'Close': '28.0', 'Adj Close': '28.0', 'Volume': '100'}, {'Date': '2019-01-15', 'Open': '29.149999618530277', 'High': '31.0', 'Low': '29.059999465942383', 'Close': '31.0', 'Adj Close': '31.0', 'Volume': '1800'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']], 'var_functions.execute_python:22': {'total_capital_market_tickers': 86, 'tickers_with_data': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:24': {'ticker': 'AGMH', 'total_days_2019': 252, 'days_range_exceeds_20pct': 13, 'sample_calculations': [{'Date': '2019-01-02', 'High': 30.75200080871582, 'Low': 30.75200080871582, 'Range_Pct': 0.0}, {'Date': '2019-01-03', 'High': 27.31999969482422, 'Low': 27.299999237060547, 'Range_Pct': 0.0007326175209748969}, {'Date': '2019-01-04', 'High': 27.31999969482422, 'Low': 27.31999969482422, 'Range_Pct': 0.0}, {'Date': '2019-01-07', 'High': 28.89999961853028, 'Low': 28.89999961853028, 'Range_Pct': 0.0}, {'Date': '2019-01-08', 'High': 28.89999961853028, 'Low': 28.89999961853028, 'Range_Pct': 0.0}]}, 'var_functions.execute_python:26': {'tickers_to_analyze': 86, 'example_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:28': {'total_tickers': 86, 'sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
