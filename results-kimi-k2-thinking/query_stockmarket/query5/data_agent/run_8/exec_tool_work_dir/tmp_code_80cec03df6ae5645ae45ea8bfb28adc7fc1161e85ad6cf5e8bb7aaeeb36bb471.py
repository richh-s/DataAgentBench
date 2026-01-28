code = """import json
import pandas as pd

# Load BHAT data
bhat_data = locals()['var_functions.query_db:30']
if isinstance(bhat_data, str) and bhat_data.endswith('.json'):
    with open(bhat_data, 'r') as f:
        bhat_data = json.load(f)

# Calculate volatile days for BHAT
if bhat_data:
    df_bhat = pd.DataFrame(bhat_data)
    df_bhat['Low'] = df_bhat['Low'].astype(float)
    df_bhat['High'] = df_bhat['High'].astype(float)
    df_bhat['Intraday_Range'] = df_bhat['High'] - df_bhat['Low']
    df_bhat['Range_Percent'] = (df_bhat['Intraday_Range'] / df_bhat['Low']) * 100
    volatile_days = df_bhat[df_bhat['Range_Percent'] > 20]
    bhat_volatile = len(volatile_days)
    print(f"BHAT had {bhat_volatile} volatile days in 2019")
    
    # Show sample volatile days
    if not volatile_days.empty:
        print("Sample volatile days:")
        print(volatile_days[['Date', 'Low', 'High', 'Intraday_Range', 'Range_Percent']].head())
else:
    bhat_volatile = 0
    print("No data for BHAT")

# Load company info
nasdaq_stocks = locals()['var_functions.query_db:22']
if isinstance(nasdaq_stocks, str) and nasdaq_stocks.endswith('.json'):
    with open(nasdaq_stocks, 'r') as f:
        nasdaq_stocks = json.load(f)

company_names = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}

# Current results
results = {
    'AGMH': {'company': company_names['AGMH'], 'volatile_days': 13},
    'BCLI': {'company': company_names['BCLI'], 'volatile_days': 0},
    'BHAT': {'company': company_names['BHAT'], 'volatile_days': bhat_volatile}
}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'ticker': 'AGMH', 'volatile_days': 13}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'status': 'ready', 'tickers_count': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:16': {'batches_created': 9, 'batch_size': 10, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-03', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-04', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-07', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '100'}, {'Date': '2019-01-08', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}], 'var_functions.execute_python:20': {'status': 'starting', 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'test_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
