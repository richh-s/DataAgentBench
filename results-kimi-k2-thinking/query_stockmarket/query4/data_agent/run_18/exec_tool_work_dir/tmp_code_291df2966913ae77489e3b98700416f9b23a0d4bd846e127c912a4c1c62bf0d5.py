code = """import json
import os
import sqlite3
from collections import defaultdict

# Read the NYSE stocks list
db_query_result_path = locals().get('var_functions.query_db:14', '')
if not db_query_result_path or not os.path.exists(db_query_result_path):
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not find NYSE stock list file'}))
else:
    with open(db_query_result_path, 'r') as f:
        nyse_stocks = json.load(f)
    
    # Create symbol to company name mapping
    symbol_to_name = {stock['Symbol']: stock['Company Description'] for stock in nyse_stocks}
    symbols = list(symbol_to_name.keys())
    
    print('__RESULT__:')
    print(json.dumps({
        'total_symbols': len(symbols),
        'first_few_symbols': symbols[:10],
        'sample_company_name': symbol_to_name[symbols[0]]
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 234, 'first_few': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nyse_stocks': 234, 'available_in_trade_db': 234, 'first_few_available': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'total_symbols': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD'], 'sample_mapping': {'AEFC': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}}, 'var_functions.execute_python:12': {'total_nyse_stocks': 234, 'first_ten_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
