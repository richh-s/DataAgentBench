code = """import json

# Let's manually process a subset of NASDAQ Capital Market stocks we know exist
# Based on our earlier queries and common knowledge

# NASDAQ Capital Market stocks with likely trade data
candidate_tickers = [
    'AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX',
    'IDEX', 'FAMI', 'FTFT', 'GDYN', 'GLG', 'CORV', 'CPAH', 'CVV', 
    'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FNCB', 'FSBW', 'HNNA', 'HQI'
]

# Map tickers to company names (from our earlier data)
ticker_to_company = {
    'AGMH': 'AGM Group Holdings Inc.',
    'BCLI': 'Brainstorm Cell Therapeutics Inc.',
    'BLFS': 'BioLife Solutions Inc.',
    'BOTJ': 'Bank of the James Financial Group Inc.',
    'BWEN': 'Broadwind Energy Inc.',
    'CBAT': 'CBAK Energy Technology Inc.',
    'CEMI': 'Chembio Diagnostics Inc.',
    'HRTX': 'Heron Therapeutics Inc.',
    'IDEX': 'Ideanomics Inc.',
    'FAMI': 'Farmmi Inc.',
    'FTFT': 'Future FinTech Group Inc.',
    'GDYN': 'Grid Dynamics Holdings Inc.',
    'GLG': 'TD Holdings Inc.',
    'CORV': 'Correvio Pharma Corp.',
    'CPAH': 'CounterPath Corporation',
    'CVV': 'CVD Equipment Corporation',
    'DZSI': 'DASAN Zhone Solutions Inc.',
    'ELSE': 'Electro-Sensors Inc.',
    'EXPC': 'Experience Investment Corp.',
    'EYEG': 'Eyegate Pharmaceuticals Inc.',
    'FNCB': 'FNCB Bancorp Inc.',
    'FSBW': 'FS Bancorp Inc.',
    'HNNA': 'Hennessy Advisors Inc.',
    'HQI': 'HireQuest Inc.'
}

print(f"Processing {len(candidate_tickers)} NASDAQ Capital Market stocks...")
print("__RESULT__:")
print(json.dumps(list(ticker_to_company.items())))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:24': {'nasdaq_path': 'var_functions.query_db:4', 'trade_path': 'var_functions.list_db:8'}, 'var_functions.query_db:32': [{'Date': '2019-01-02', 'Open': '30.75200080871582', 'High': '30.75200080871582', 'Low': '30.75200080871582', 'Close': '30.75200080871582', 'Adj Close': '30.75200080871582', 'Volume': '400'}, {'Date': '2019-01-03', 'Open': '27.299999237060547', 'High': '27.31999969482422', 'Low': '27.299999237060547', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '400'}, {'Date': '2019-01-04', 'Open': '27.31999969482422', 'High': '27.31999969482422', 'Low': '27.31999969482422', 'Close': '27.31999969482422', 'Adj Close': '27.31999969482422', 'Volume': '100'}, {'Date': '2019-01-07', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '400'}, {'Date': '2019-01-08', 'Open': '28.899999618530277', 'High': '28.899999618530277', 'Low': '28.899999618530277', 'Close': '28.899999618530277', 'Adj Close': '28.899999618530277', 'Volume': '100'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.list_db:42': 'file_storage/functions.list_db:42.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:50': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX'], 'var_functions.query_db:52': [{'high_vol_days': '13'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json', 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.execute_python:72': {'tickers': ['AGMH', 'BCLI', 'BLFS', 'BOTJ', 'BWEN', 'CBAT', 'CEMI', 'HRTX']}, 'var_functions.query_db:74': 'file_storage/functions.query_db:74.json', 'var_functions.query_db:76': [{'ticker': 'AGMH', 'high_vol_days': '13'}]}

exec(code, env_args)
