code = """import json
import os

# Load NYSE stocks and create symbol to name mapping
stockinfo_path = locals().get('var_functions.query_db:56', '')
trade_tables_path = locals().get('var_functions.list_db:5', '')

with open(stockinfo_path, 'r') as f:
    nyse_stocks = json.load(f)

with open(trade_tables_path, 'r') as f:
    all_tables = set(json.load(f))

# Create symbol to clean company name mapping
symbol_to_name = {}
for stock in nyse_stocks:
    symbol = stock['Symbol']
    desc = stock['Company Description']
    # Extract clean company name
    for sep in [' specializes', ' is ', ' offers ', ' provides ', ' excels', ' operates']:
        if sep in desc:
            name = desc.split(sep)[0].strip()
            break
    else:
        name = desc
    symbol_to_name[symbol] = name

# Get valid symbols
valid_symbols = [sym for sym in symbol_to_name.keys() if sym in all_tables]

# Create batch queries for trade data
# Let's process first 50 symbols to start
batch_size = 50
first_batch = valid_symbols[:batch_size]

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(valid_symbols),
    'batch_size': batch_size,
    'first_batch_symbols': first_batch,
    'sample_names': [symbol_to_name[sym] for sym in first_batch[:5]]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 234, 'first_few': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'first_few_available': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'sample_mapping': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.execute_python:12': {'total_nyse_stocks': 234, 'first_ten_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_symbols': 234, 'first_few_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'sample_company_name': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, 'var_functions.execute_python:18': {'count': 234, 'first_stock': {'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.execute_python:20': {'total_stocks': 234, 'num_batches': 8, 'batch_size': 30, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ']}, 'var_functions.execute_python:22': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:24': {'message': 'Preparing to analyze 234 NYSE stocks for 2017 performance', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:26': [], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:30': {'total_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:32': {'message': 'Processing 234 NYSE stocks', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:34': {'total_valid_stocks': 234, 'first_batch_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT'], 'sample_company_name': 'Albany International Corporation'}, 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.execute_python:38': {'total_stocks': 234, 'sample_mapping': {'AEFC': 'Aegon Funding Company LLC', 'AIN': 'Albany International Corporation', 'AIV': 'Apartment Investment and Management Company', 'AIZP': 'Assurant, Inc.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc.', 'AL': 'Air Lease Corporation', 'AMN': 'AMN Healthcare Services Inc.', 'AMP': 'Ameriprise Financial, Inc.', 'AMT': 'American Tower Corporation is a leading real estate investment trust that', 'ARD': 'Ardagh Group S.A.'}}, 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.execute_python:42': {'total_stocks': 234, 'sample_symbols': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.'], ['AL', 'Air Lease Corporation'], ['AMN', 'AMN Healthcare Services Inc.'], ['AMP', 'Ameriprise Financial, Inc.'], ['AMT', 'American Tower Corporation is a leading real estate investment trust that'], ['ARD', 'Ardagh Group S.A.']]}, 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:46': {'total_nyse_stocks': 234, 'valid_stocks_with_data': 234, 'sample_valid_stocks': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:48': {'message': 'Mapped 234 stocks to company names', 'sample': [['AEFC', 'Aegon Funding Company LLC'], ['AIN', 'Albany International Corporation'], ['AIV', 'Apartment Investment and Management Company'], ['AIZP', 'Assurant, Inc.'], ['AJRD', 'Aerojet Rocketdyne Holdings, Inc.']]}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.execute_python:52': {'message': 'Processing 234 valid NYSE stocks', 'first_few': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:54': {'message': 'Prepared to analyze 234 stocks', 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.execute_python:58': {'stock_count': 234, 'message': 'Ready to query trade data for each stock'}, 'var_functions.query_db:60': [], 'var_functions.execute_python:62': {'analysis_plan': 'Will process each stock serially to avoid timeouts', 'total_stocks': 234, 'first_batch': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.execute_python:66': {'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'company_names': ['Aegon Funding Company LLC', 'Albany International Corporation', 'Apartment Investment and Management Company', 'Assurant, Inc.', 'Aerojet Rocketdyne Holdings, Inc.', 'Air Lease Corporation', 'AMN Healthcare Services Inc.', 'Ameriprise Financial, Inc.', 'American Tower Corporation is a leading real estate investment trust that', 'Ardagh Group S.A.']}}

exec(code, env_args)
