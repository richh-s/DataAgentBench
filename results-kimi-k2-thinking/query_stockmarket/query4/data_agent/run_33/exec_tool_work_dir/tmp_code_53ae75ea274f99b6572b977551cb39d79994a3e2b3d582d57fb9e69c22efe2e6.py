code = """def create_batch_query(symbols, year=2017):
    """Create a SQL query that analyzes up/down days for multiple symbols"""
    conditions = []
    
    for symbol in symbols:
        # Count trading days
        count_query = f"(SELECT COUNT(*) FROM {symbol} WHERE Date >= '{year}-01-01' AND Date <= '{year}-12-31')"
        
        # Count up days (Close > Open)
        up_query = f"(SELECT COUNT(*) FROM {symbol} WHERE Date >= '{year}-01-01' AND Date <= '{year}-12-31' AND Close > Open)"
        
        # Count down days (Close < Open)
        down_query = f"(SELECT COUNT(*) FROM {symbol} WHERE Date >= '{year}-01-01' AND Date <= '{year}-12-31' AND Close < Open)"
        
        conditions.append(f"SELECT '{symbol}' as Symbol, {up_query} as UpDays, {down_query} as DownDays, {count_query} as TotalDays")
    
    return " UNION ALL ".join(conditions)

# Get all NYSE symbols
stockinfo_data = locals()['var_functions.query_db:0']
if isinstance(stockinfo_data, str):
    with open(stockinfo_data, 'r') as f:
        stockinfo_data = json.load(f)

nyse_companies = {item['Symbol']: item['Company Description'] for item in stockinfo_data}
nyse_symbols = list(nyse_companies.keys())

# Create batched queries for efficient processing
batch_size = 20
batches = [nyse_symbols[i:i+batch_size] for i in range(0, len(nyse_symbols), batch_size)]

print('__RESULT__:')
print(f"Total NYSE non-ETF symbols: {len(nyse_symbols)}")
print(f"Number of batches: {len(batches)}")
print(f"Batch size: {batch_size}")
print(f"First batch sample: {batches[0]}")

# Save batch info for next step
import json
result = {
    'total_symbols': len(nyse_symbols),
    'batch_size': batch_size,
    'num_batches': len(batches),
    'batches': batches
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'total_stocktrade_tables': 2753, 'available_for_analysis': 234, 'sample_stocks': ['SJT', 'LHC', 'GOL', 'RMT', 'NFH', 'NNI', 'HIO', 'OCFT', 'MLI', 'PNM']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'status': 'ready', 'symbol_count': 234, 'first_10_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'batch_size': 20, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:18': {'total_symbols': 234, 'sample_companies': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}}

exec(code, env_args)
