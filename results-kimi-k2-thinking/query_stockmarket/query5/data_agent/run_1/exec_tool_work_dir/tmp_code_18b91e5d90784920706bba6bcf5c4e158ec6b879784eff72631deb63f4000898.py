code = """import json

# Get company data
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

company_names = {c['Symbol']: c['Company Description'] for c in companies_data}
symbols = [c['Symbol'] for c in companies_data]

# Function to count high volatility days
def count_volatility_days(stock_data):
    if not stock_data:
        return 0
    count = 0
    for day in stock_data:
        try:
            high = float(day['High'])
            low = float(day['Low'])
            if low > 0:
                range_pct = (high - low) / low
                if range_pct > 0.20:
                    count += 1
        except (ValueError, TypeError):
            continue
    return count

# Process the data we already have
results = []

# Process AGMH (var_functions.query_db:30)
agmh_data = locals()['var_functions.query_db:30']
if isinstance(agmh_data, str):
    with open(agmh_data, 'r') as f:
        agmh_data = json.load(f)
agmh_count = count_volatility_days(agmh_data)
results.append({
    'symbol': 'AGMH',
    'company': company_names['AGMH'],
    'volatility_days': agmh_count
})

# Process ALACU (var_functions.query_db:31) - empty
alacu_data = locals()['var_functions.query_db:31']
if isinstance(alacu_data, str):
    with open(alacu_data, 'r') as f:
        alacu_data = json.load(f)
alacu_count = count_volatility_days(alacu_data)
results.append({
    'symbol': 'ALACU',
    'company': company_names['ALACU'],
    'volatility_days': alacu_count
})

# Process AMHC (var_functions.query_db:32)
amhc_data = locals()['var_functions.query_db:32']
if isinstance(amhc_data, str):
    with open(amhc_data, 'r') as f:
        amhc_data = json.load(f)
amhc_count = count_volatility_days(amhc_data)
results.append({
    'symbol': 'AMHC',
    'company': company_names['AMHC'],
    'volatility_days': amhc_count
})

# Process ANDA (var_functions.query_db:33)
anda_data = locals()['var_functions.query_db:33']
if isinstance(anda_data, str):
    with open(anda_data, 'r') as f:
        anda_data = json.load(f)
anda_count = count_volatility_days(anda_data)
results.append({
    'symbol': 'ANDA',
    'company': company_names['ANDA'],
    'volatility_days': anda_count
})

# Process APEX (var_functions.query_db:34)
apex_data = locals()['var_functions.query_db:34']
if isinstance(apex_data, str):
    with open(apex_data, 'r') as f:
        apex_data = json.load(f)
apex_count = count_volatility_days(apex_data)
results.append({
    'symbol': 'APEX',
    'company': company_names['APEX'],
    'volatility_days': apex_count
})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:16': {'nasdaq_count': 86, 'available_count': 86, 'missing_count': 0, 'sample_available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'sample_missing': []}, 'var_functions.execute_python:18': {'message': 'Ready to process 86 stocks', 'stock_count': 86}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_symbols': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:24': {'symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing f...', 'total_2019_days': 252, 'high_volatility_days': 13}, 'var_functions.execute_python:26': {'message': 'Ready to query all 86 stocks', 'symbols_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.execute_python:28': {'action': 'query_all_symbols', 'symbol_count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:32': [], 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': {'status': 'initialized', 'symbol_count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:43': 'file_storage/functions.query_db:43.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:45': 'file_storage/functions.query_db:45.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:52': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatility_days': 13}], 'var_functions.execute_python:54': {'total_symbols': 86, 'queried_so_far': 10, 'remaining_symbols': 76, 'next_batch': ['BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:57': 'file_storage/functions.query_db:57.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json'}

exec(code, env_args)
