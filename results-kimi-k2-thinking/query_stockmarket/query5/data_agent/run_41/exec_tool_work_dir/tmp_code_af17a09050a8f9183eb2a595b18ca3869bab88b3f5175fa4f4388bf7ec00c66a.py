code = """import json

# Load the stock info data
stockinfo_path = locals()['var_functions.query_db:52']
with open(stockinfo_path) as f:
    nasdaq_stocks = json.load(f)

# Build symbol list and company mapping
symbols = [stock['Symbol'] for stock in nasdaq_stocks]
company_map = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}

print('Total NASDAQ Capital Market symbols:', len(symbols))
print('First 3 symbols:', symbols[:3])

# Build one giant UNION ALL query
query_parts = []
for symbol in symbols:
    part = f"SELECT '{symbol}' as Symbol, COUNT(*) as high_vol_days FROM \"{symbol}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31' AND (\"High\" - \"Low\") > (\"Low\" * 0.20)"
    query_parts.append(part)
    
full_query = ' UNION ALL '.join(query_parts) + ' ORDER BY high_vol_days DESC'

print('Generated UNION ALL query with', len(query_parts), 'parts')
print('Query length:', len(full_query))

print('__RESULT__:')
print(json.dumps({'full_query': full_query, 'company_map': company_map}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:10': {'total_tables': 2753, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}, 'var_functions.execute_python:12': {'nasdaq_capital_count': 86, 'available_in_stocktrade': 86, 'sample_symbols': ['BWEN', 'SSNT', 'HQI', 'FSBW', 'CCCL', 'CUBA', 'WHLM', 'IGIC', 'CPAH', 'FTFT']}, 'var_functions.query_db:14': [{'high_volatility_days': '13'}], 'var_functions.execute_python:18': 'file_storage/functions.execute_python:18.json', 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': 'file_storage/functions.execute_python:22.json', 'var_functions.execute_python:24': 'file_storage/functions.execute_python:24.json', 'var_functions.execute_python:26': 'file_storage/functions.execute_python:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json', 'var_functions.execute_python:32': 'file_storage/functions.execute_python:32.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.list_db:36': 'file_storage/functions.list_db:36.json', 'var_functions.execute_python:38': {'length': 14144, 'complete': False}, 'var_functions.execute_python:44': {'symbol_count': 86, 'test_query': 'SELECT "AGMH" as Symbol, COUNT(*) as days FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND (High - Low) > (Low * 0.20) UNION ALL SELECT "ALACU" as Symbol, COUNT(*) as days FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND (High - Low) > (Low * 0.20) UNION ALL SELECT "AMHC" as Symbol, COUNT(*) as days FROM "AMHC" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND (High - Low) > (Low * 0.20) ORDER BY days DESC LIMIT 5', 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.execute_python:48': {'first_query_part': 'SELECT \n        \'AGMH\' as Symbol, \n        COUNT(*) as high_volatility_days \n    FROM "AGMH" \n    WHERE \n        "Date" >= \'2019-01-01\' AND \n        "Date" <= \'2019-12-31\' AND \n        ("High" - "Low") > ("Low" * 0.20)', 'total_symbols': 86}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json', 'var_functions.query_db:54': [{'Symbol': 'AGMH', 'high_volatility_days': '13'}]}

exec(code, env_args)
