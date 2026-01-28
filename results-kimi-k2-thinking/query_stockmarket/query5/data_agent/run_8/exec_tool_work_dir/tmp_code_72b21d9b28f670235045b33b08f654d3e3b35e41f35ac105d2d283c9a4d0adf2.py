code = """import json
import pandas as pd

# Get NASDAQ Capital Market tickers and company names
nasdaq_stocks = locals()['var_functions.query_db:22']
if isinstance(nasdaq_stocks, str) and nasdaq_stocks.endswith('.json'):
    with open(nasdaq_stocks, 'r') as f:
        nasdaq_stocks = json.load(f)

company_info = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}
tickers = list(company_info.keys())

print(f"Found {len(tickers)} NASDAQ Capital Market tickers")

# Initial results from manual queries
initial_results = {
    'AGMH': 13,
    'BCLI': 0  # Need to process BCLI data
}

# Let's load BCLI data and calculate
bcli_data = locals()['var_functions.query_db:24']
if isinstance(bcli_data, str) and bcli_data.endswith('.json'):
    with open(bcli_data, 'r') as f:
        bcli_data = json.load(f)

if bcli_data:
    df_bcli = pd.DataFrame(bcli_data)
    df_bcli['Low'] = df_bcli['Low'].astype(float)
    df_bcli['High'] = df_bcli['High'].astype(float)
    df_bcli['Intraday_Range'] = df_bcli['High'] - df_bcli['Low']
    df_bcli['Range_Percent'] = (df_bcli['Intraday_Range'] / df_bcli['Low']) * 100
    volatile_days = df_bcli[df_bcli['Range_Percent'] > 20]
    bcli_volatile = len(volatile_days)
    print(f"BCLI had {bcli_volatile} volatile days")
    initial_results['BCLI'] = bcli_volatile

# Store tickers for next processing step
print("__RESULT__:")
print(json.dumps({
    "company_info": company_info,
    "initial_results": initial_results,
    "total_tickers": len(tickers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'ticker': 'AGMH', 'volatile_days': 13}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'status': 'ready', 'tickers_count': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:16': {'batches_created': 9, 'batch_size': 10, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-03', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-04', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-07', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '100'}, {'Date': '2019-01-08', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}], 'var_functions.execute_python:20': {'status': 'starting', 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
