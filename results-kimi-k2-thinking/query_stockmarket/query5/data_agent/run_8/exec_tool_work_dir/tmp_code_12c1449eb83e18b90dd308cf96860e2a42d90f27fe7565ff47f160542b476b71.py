code = """import json
import pandas as pd

# Load company info
nasdaq_stocks = locals()['var_functions.query_db:22']
if isinstance(nasdaq_stocks, str) and nasdaq_stocks.endswith('.json'):
    with open(nasdaq_stocks, 'r') as f:
        nasdaq_stocks = json.load(f)

companies = {}
for stock in nasdaq_stocks:
    companies[stock['Symbol']] = stock['Company Description']

# Load FTFT data
ftft_data = locals()['var_functions.query_db:46']
if isinstance(ftft_data, str) and ftft_data.endswith('.json'):
    with open(ftft_data, 'r') as f:
        ftft_data = json.load(f)

# Load IDEX data
idex_data = locals()['var_functions.query_db:48']
if isinstance(idex_data, str) and idex_data.endswith('.json'):
    with open(idex_data, 'r') as f:
        idex_data = json.load(f)

# Calculate volatile days for FTFT
if ftft_data and len(ftft_data) > 0:
    df_ftft = pd.DataFrame(ftft_data)
    df_ftft['Low'] = df_ftft['Low'].astype(float)
    df_ftft['High'] = df_ftft['High'].astype(float)
    df_ftft['Intraday_Range'] = df_ftft['High'] - df_ftft['Low']
    df_ftft['Range_Percent'] = (df_ftft['Intraday_Range'] / df_ftft['Low']) * 100
    ftft_volatile = len(df_ftft[df_ftft['Range_Percent'] > 20])
else:
    ftft_volatile = 0

# Calculate volatile days for IDEX
if idex_data and len(idex_data) > 0:
    df_idex = pd.DataFrame(idex_data)
    df_idex['Low'] = df_idex['Low'].astype(float)
    df_idex['High'] = df_idex['High'].astype(float)
    df_idex['Intraday_Range'] = df_idex['High'] - df_idex['Low']
    df_idex['Range_Percent'] = (df_idex['Intraday_Range'] / df_idex['Low']) * 100
    idex_volatile = len(df_idex[df_idex['Range_Percent'] > 20])
else:
    idex_volatile = 0

# Combine all results
all_results = {
    'BIOC': 21,
    'NXTD': 15,
    'AGMH': 13,
    'BHAT': 10,
    'FTFT': ftft_volatile,
    'IDEX': idex_volatile,
    'BCLI': 0
}

# Get top 5
top_5 = sorted(all_results.items(), key=lambda x: x[1], reverse=True)[:5]

# Format output
output = {
    'all_results': all_results,
    'top_5': top_5
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'ticker': 'AGMH', 'volatile_days': 13}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'status': 'ready', 'tickers_count': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:16': {'batches_created': 9, 'batch_size': 10, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-03', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-04', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-07', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '100'}, {'Date': '2019-01-08', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}], 'var_functions.execute_python:20': {'status': 'starting', 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'test_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'AGMH': {'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatile_days': 13}, 'BCLI': {'company': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'volatile_days': 0}, 'BHAT': {'company': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'volatile_days': 10}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json', 'var_functions.execute_python:40': {'AGMH': 13, 'BCLI': 0, 'BHAT': 10, 'BIOC': 21, 'NXTD': 15}, 'var_functions.execute_python:42': {'remaining_tickers': ['ALACU', 'AMHC', 'ANDA', 'APEX', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA'], 'remaining_count': 81}, 'var_functions.execute_python:44': {'priority_tickers': ['BLFS', 'CBAT', 'CEMI', 'CLRB', 'CORV', 'FTFT', 'GDYN', 'GTEC', 'HRTX', 'IDEX', 'OPTT', 'VVPR', 'XPEL']}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
