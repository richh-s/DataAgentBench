code = """import json
import os
from collections import defaultdict

# Load the NYSE non-ETF stocks
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    nyse_stocks = json.load(f)

symbol_to_name = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
symbols = list(symbol_to_name.keys())

# Store results for each stock
stock_results = []

# Process in batches to avoid too many queries at once
for symbol in symbols:
    # Escape special characters in table names for DuckDB
    escaped_symbol = f'"{symbol}"'
    query = f"""
    SELECT 
        COUNT(CASE WHEN Close > Open THEN 1 END) as up_days,
        COUNT(CASE WHEN Close < Open THEN 1 END) as down_days,
        COUNT(*) as total_days
    FROM {escaped_symbol}
    WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'
    """
    
    # Use query_db tool by writing the query to a temporary file
    # For now, collect all queries
    stock_results.append({
        'symbol': symbol,
        'name': symbol_to_name[symbol],
        'query': query
    })

print('__RESULT__:')
print(json.dumps({
    'total_stocks': len(stock_results),
    'sample_symbol': stock_results[0]['symbol'],
    'sample_query': stock_results[0]['query']
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:4': {'count': 234}, 'var_functions.execute_python:6': {'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR'], 'count': 234}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': {'nyse_count': 234, 'total_tables': 2753, 'available_count': 234, 'available_symbols': ['PMT', 'GTY', 'CNK', 'GEL', 'BKT', 'CRC', 'MKC', 'MNE', 'EGY', 'BV']}, 'var_functions.query_db:12': [{'Date': '2017-01-03', 'Open': '46.900001525878906', 'Close': '47.150001525878906'}, {'Date': '2017-01-04', 'Open': '47.29999923706055', 'Close': '48.150001525878906'}, {'Date': '2017-01-05', 'Open': '47.95000076293945', 'Close': '47.75'}, {'Date': '2017-01-06', 'Open': '47.75', 'Close': '46.59999847412109'}, {'Date': '2017-01-09', 'Open': '46.5', 'Close': '45.54999923706055'}], 'var_functions.execute_python:14': {'count': 234, 'sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'AIN': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'AIV': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'AIZP': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'AJRD': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}}, 'var_functions.execute_python:16': {'test': 'complete', 'processed': 10}}

exec(code, env_args)
