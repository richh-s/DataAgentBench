code = """import json
import pandas as pd

# Load company info
nasdaq_stocks = locals()['var_functions.query_db:22']
if isinstance(nasdaq_stocks, str) and nasdaq_stocks.endswith('.json'):
    with open(nasdaq_stocks, 'r') as f:
        nasdaq_stocks = json.load(f)

companies = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}

# Current results
results = {
    'AGMH': 13,
    'BCLI': 0,
    'BHAT': 10,
    'BIOC': 21,
    'NXTD': 15
}

# Get remaining tickers to process
all_tickers = list(companies.keys())
processed_tickers = set(results.keys())
remaining_tickers = [t for t in all_tickers if t not in processed_tickers]

print(f"Processed: {len(processed_tickers)} | Remaining: {len(remaining_tickers)}")
print("Top 5 so far:", sorted(results.items(), key=lambda x: x[1], reverse=True)[:5])

print("__RESULT__:")
print(json.dumps({
    "remaining_tickers": remaining_tickers[:15],  # Show first 15
    "remaining_count": len(remaining_tickers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'ticker': 'AGMH', 'volatile_days': 13}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'status': 'ready', 'tickers_count': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:16': {'batches_created': 9, 'batch_size': 10, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-03', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-04', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-07', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '100'}, {'Date': '2019-01-08', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}], 'var_functions.execute_python:20': {'status': 'starting', 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'test_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'AGMH': {'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatile_days': 13}, 'BCLI': {'company': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'volatile_days': 0}, 'BHAT': {'company': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'volatile_days': 10}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:40': {'AGMH': 13, 'BCLI': 0, 'BHAT': 10, 'BIOC': 21, 'NXTD': 15}}

exec(code, env_args)
