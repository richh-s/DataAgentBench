code = """import json
import os

# Access the stored NASDAQ Capital Market tickers
nasdaq_capital_stocks = []
var_key = 'var_functions.query_db:0'
file_path = locals().get(var_key)

if file_path and isinstance(file_path, str) and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        nasdaq_capital_stocks = json.load(f)
        print(f"Loaded {len(nasdaq_capital_stocks)} NASDAQ Capital Market stocks")
else:
    print(f"Could not access NASDAQ Capital data. File path: {file_path}")

# Get tickers
tickers = [stock['Symbol'] for stock in nasdaq_capital_stocks]
print(f"Total tickers: {len(tickers)}")
print(f"Sample: {tickers[:10]}")

# Access the table list from stocktrade_database
stocktrade_tables = []
var_key2 = 'var_functions.list_db:10'
file_path2 = locals().get(var_key2)

if file_path2 and isinstance(file_path2, str) and os.path.exists(file_path2):
    with open(file_path2, 'r') as f:
        stocktrade_tables = json.load(f)
        print(f"Loaded {len(stocktrade_tables)} tables from stocktrade database")
else:
    print(f"Could not access stocktrade tables. File path: {file_path2}")

# Find intersection
available_tickers = set(tickers).intersection(set(stocktrade_tables))
print(f"Available tickers count: {len(available_tickers)}")

# Save results
result = {
    "nasdaq_capital_count": len(tickers),
    "available_count": len(available_tickers),
    "available_tickers": sorted(list(available_tickers))
}

print(f"__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'tickers_count': 86, 'sample_stocks': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json'}

exec(code, env_args)
