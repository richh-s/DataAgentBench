code = """import json

# Load NYSE non-ETF stock data from previous query
stockinfo_data = locals()['var_functions.query_db:24']
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

# Create mapping of symbol to company name
nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
nyse_symbols = list(nyse_companies.keys())

print(f"Total NYSE non-ETF stocks: {len(nyse_symbols)}")
print(f"First few symbols: {nyse_symbols[:5]}")

# Create UNION ALL query for first batch of 20 stocks
batch_size = 20
batch = nyse_symbols[:batch_size]

subqueries = []
for symbol in batch:
    # Count up days, down days, and total days for 2017
    subquery = f"""
    SELECT 
        '{symbol}' as Symbol,
        (SELECT COUNT(*) FROM "{symbol}" 
         WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' 
           AND Close > Open) as UpDays,
        (SELECT COUNT(*) FROM "{symbol}" 
         WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' 
           AND Close < Open) as DownDays,
        (SELECT COUNT(*) FROM "{symbol}" 
         WHERE Date >= '2017-01-01' AND Date <= '2017-12-31') as TotalDays
    """
    subqueries.append(subquery)

union_query = " UNION ALL ".join(subqueries)

result = {
    'batch_size': len(batch),
    'sample_symbols': batch[:3],
    'query_preview': union_query[:200]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'status': 'ready', 'symbol_count': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'batch_size': 20, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:18': {'total_symbols': 234, 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}, 'var_functions.execute_python:22': {'total_symbols': 234, 'batch_size': 20, 'num_batches': 12, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'status': 'starting_analysis', 'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:28': {'total_stocks': 234, 'num_batches': 5, 'batch_size': 47}, 'var_functions.execute_python:32': {'status': 'test_symbols', 'test_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}}

exec(code, env_args)
