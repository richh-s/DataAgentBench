code = """import json
import pandas as pd

# Load and calculate BIOC
biloc_data = locals()['var_functions.query_db:34']
if isinstance(biloc_data, str) and biloc_data.endswith('.json'):
    with open(biloc_data, 'r') as f:
        biloc_data = json.load(f)

if biloc_data:
    df_bioc = pd.DataFrame(biloc_data)
    df_bioc['Low'] = df_bioc['Low'].astype(float)
    df_bioc['High'] = df_bioc['High'].astype(float)
    df_bioc['Intraday_Range'] = df_bioc['High'] - df_bioc['Low']
    df_bioc['Range_Percent'] = (df_bioc['Intraday_Range'] / df_bioc['Low']) * 100
    bioc_volatile = len(df_bioc[df_bioc['Range_Percent'] > 20])
    print(f"BIOC had {bioc_volatile} volatile days")
else:
    bioc_volatile = 0

# Load and calculate NXTD
nxtd_data = locals()['var_functions.query_db:36']
if isinstance(nxtd_data, str) and nxtd_data.endswith('.json'):
    with open(nxtd_data, 'r') as f:
        nxtd_data = json.load(f)

if nxtd_data:
    df_nxtd = pd.DataFrame(nxtd_data)
    df_nxtd['Low'] = df_nxtd['Low'].astype(float)
    df_nxtd['High'] = df_nxtd['High'].astype(float)
    df_nxtd['Intraday_Range'] = df_nxtd['High'] - df_nxtd['Low']
    df_nxtd['Range_Percent'] = (df_nxtd['Intraday_Range'] / df_nxtd['Low']) * 100
    nxtd_volatile = len(df_nxtd[df_nxtd['Range_Percent'] > 20])
    print(f"NXTD had {nxtd_volatile} volatile days")
else:
    nxtd_volatile = 0

# Current results
all_results = {
    'AGMH': 13,
    'BCLI': 0,
    'BHAT': 10,
    'BIOC': bioc_volatile,
    'NXTD': nxtd_volatile
}

print("Current results:", all_results)

print("__RESULT__:")
print(json.dumps(all_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'status': 'initialized', 'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:5': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:8': {'ticker': 'AGMH', 'volatile_days': 13}, 'var_functions.list_db:10': 'file_storage/functions.list_db:10.json', 'var_functions.execute_python:12': {'status': 'ready', 'tickers_count': 86, 'sample_tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:14': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:16': {'batches_created': 9, 'batch_size': 10, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:18': [{'Date': '2019-01-02', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-03', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-04', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}, {'Date': '2019-01-07', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '100'}, {'Date': '2019-01-08', 'Open': '10.09000015258789', 'High': '10.09000015258789', 'Low': '10.09000015258789', 'Close': '10.09000015258789', 'Adj Close': '10.09000015258789', 'Volume': '0'}], 'var_functions.execute_python:20': {'status': 'starting', 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.execute_python:28': {'tickers_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'test_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:32': {'AGMH': {'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatile_days': 13}, 'BCLI': {'company': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'volatile_days': 0}, 'BHAT': {'company': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'volatile_days': 10}}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': 'file_storage/functions.execute_python:38.json'}

exec(code, env_args)
