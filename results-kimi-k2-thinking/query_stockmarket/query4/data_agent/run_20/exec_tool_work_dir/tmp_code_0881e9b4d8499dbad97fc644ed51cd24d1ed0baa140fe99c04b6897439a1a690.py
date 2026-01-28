code = """import json
import duckdb
import os

# Load NYSE non-ETF stock data from the file
nyse_file_path = 'file_storage/functions.query_db:38.json'
with open(nyse_file_path, 'r') as f:
    nyse_stocks = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}

# Connect to DuckDB database
conn = duckdb.connect('file_storage/stocktrade_database.db')

# Track stocks with more up days than down days
stocks_analysis = []

# Process all symbols
for stock_info in nyse_stocks:
    symbol = stock_info['Symbol']
    company = stock_info['Company Description']
    
    try:
        # Query for 2017 data
        query = f"""
            SELECT 
                COUNT(*) as total_days,
                SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as up_days,
                SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as down_days
            FROM "{symbol}" 
            WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'
        """
        result = conn.execute(query).fetchone()
        
        if result:
            total_days, up_days, down_days = result
            if total_days > 0 and up_days is not None and down_days is not None:
                if up_days > down_days:
                    stocks_analysis.append({
                        'symbol': symbol,
                        'company': company,
                        'up_days': int(up_days),
                        'down_days': int(down_days)
                    })
    except:
        continue

# Sort by up_days descending
stocks_analysis.sort(key=lambda x: x['up_days'], reverse=True)

top_5 = stocks_analysis[:5]

conn.close()

# Extract company names only
company_names = [stock['company'] for stock in top_5]

print('__RESULT__:')
print(json.dumps(company_names))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}, 'var_functions.query_db:24': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:34': 'file_storage/functions.list_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:44': ['var_functions.query_db:2', 'var_functions.query_db:24', 'var_functions.query_db:26', 'var_functions.query_db:36', 'var_functions.query_db:38'], 'var_functions.execute_python:50': {'file_path': 'file_storage/functions.query_db:38.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:52': {'total_nyse_stocks': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'company_sample': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.query_db:54': [{'total_days': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_functions.query_db:56': [{'total_days': '251', 'up_days': '121.0', 'down_days': '127.0'}], 'var_functions.execute_python:58': {'total_symbols': 234, 'symbols_to_check': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.execute_python:60': {'first_batch_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC'], 'total_symbols': 234}, 'var_functions.query_db:62': 'file_storage/functions.query_db:62.json', 'var_functions.execute_python:64': {'total_nyse_stocks': 234, 'first_20_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:66': [{'total_days': '251'}], 'var_functions.query_db:68': [{'total_days': '251', 'up_days': '143.0', 'down_days': '101.0'}], 'var_functions.execute_python:70': {'total_symbols': 234, 'first_five_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD']}, 'var_functions.execute_python:72': {'total_symbols': 234, 'message': 'Ready to analyze 2017 trading data for all NYSE non-ETF stocks'}, 'var_functions.execute_python:74': {'total_nyse_non_etf': 234, 'status': 'Ready to process 2017 trading data'}, 'var_functions.query_db:76': [{'total_days': '251', 'up_days': '131.0', 'down_days': '117.0'}], 'var_functions.execute_python:78': {'total_nyse_symbols': 234, 'available_symbols': 2753, 'nyse_with_data': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT']}, 'var_functions.query_db:80': [{'total_days': '251', 'up_days': '141.0', 'down_days': '110.0'}], 'var_functions.query_db:82': [{'total_days': '251', 'up_days': '128.0', 'down_days': '123.0'}], 'var_functions.execute_python:84': {'nyse_symbols_count': 234, 'available_tables_count': 2753, 'intersection_count': 234}, 'var_functions.query_db:86': [{'total_days': '251', 'up_days': '123.0', 'down_days': '123.0'}], 'var_functions.execute_python:88': {'total_nyse_stocks': 234, 'symbols_with_data': 234, 'ready_to_process': True}, 'var_functions.execute_python:90': {'message': 'Starting analysis of all 234 NYSE non-ETF stocks for 2017', 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.execute_python:92': {'status': 'Processing 234 NYSE non-ETF stocks', 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC'], 'target_year': '2017'}, 'var_functions.execute_python:98': {'nyse_file_exists': True, 'tables_file_exists': True, 'nyse_symbols': 234, 'available_tables': 2753}, 'var_functions.execute_python:100': {'status': 'Starting analysis of 234 NYSE non-ETF stocks for 2017', 'total_symbols': 234, 'first_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:102': [{'total_days': '251', 'up_days': '123.0', 'down_days': '123.0'}], 'var_functions.query_db:104': [{'symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}], 'var_functions.query_db:106': 'file_storage/functions.query_db:106.json', 'var_functions.execute_python:108': {'status': 'Ready to process all NYSE non-ETF stocks for 2017 analysis', 'symbol_count': 234, 'symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG', 'ELF', 'EMP', 'ENLC', 'EPR', 'EPRT', 'ES', 'ESRT', 'ESS', 'ETM', 'EV', 'EVT', 'EXP', 'FMN', 'FPAC', 'FSM', 'GCO', 'GD', 'GDL', 'GDV', 'GEL', 'GJP', 'GLOB', 'GLT', 'GOL', 'GSLD', 'GTY', 'GVA', 'GWB', 'H', 'HBI', 'HDB', 'HEP', 'HIL', 'HIO', 'HIX', 'HLF', 'HLT', 'HNI', 'HRB', 'HTFA', 'IBM', 'IGR', 'IHC', 'IPG', 'IRM', 'IT', 'JGH', 'JHY', 'JKS', 'JMP', 'JNPR', 'KMB', 'KNX', 'KW', 'KYN', 'LB', 'LDOS', 'LHC', 'LHX', 'LOMA', 'MANU', 'MDLX', 'MDLY', 'MED', 'MFO', 'MGR', 'MGU', 'MHE', 'MIY', 'MKC', 'MLI', 'MNE', 'MR', 'MS', 'MTD', 'MYD', 'NFH', 'NGG', 'NJV', 'NNI', 'NNY', 'NRUC', 'NUE', 'NXN', 'OCFT', 'OEC', 'ORA', 'ORAN', 'ORCL', 'ORN', 'PAG', 'PBI', 'PFE', 'PFSI', 'PGR', 'PIM', 'PKE', 'PLAN', 'PLNT', 'PMT', 'PNM', 'PPG', 'PRSP', 'PRTY', 'PSV', 'PSXP', 'QTS', 'QUAD', 'RBC', 'RCB', 'RCI', 'RES', 'REXR', 'RH', 'RMT', 'ROG', 'ROL', 'RPAI', 'RPM', 'RQI', 'RWT', 'SAF', 'SAIL', 'SAM', 'SBR', 'SCU', 'SFUN', 'SHAK', 'SI', 'SITC', 'SJM', 'SJT', 'SJW', 'SLF', 'SMP', 'SOL', 'SPOT', 'SRC', 'SRF', 'SRT', 'SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_functions.execute_python:110': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'ready_for_analysis': True}, 'var_functions.query_db:112': [{'symbol': 'AIV', 'total_days': '251', 'up_days': '118.0', 'down_days': '128.0'}], 'var_functions.execute_python:114': {'total_symbols': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'status': 'Ready for comprehensive analysis'}, 'var_functions.execute_python:116': {'total_symbols': 234, 'ready_for_batch_queries': True}, 'var_functions.execute_python:118': {'error': 'Database not found', 'path': 'file_storage/stocktrade_database.db'}, 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json'}

exec(code, env_args)
