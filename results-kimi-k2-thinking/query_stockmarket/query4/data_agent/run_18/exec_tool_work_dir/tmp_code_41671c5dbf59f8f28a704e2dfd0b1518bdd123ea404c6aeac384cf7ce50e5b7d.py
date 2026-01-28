code = """import json
import os

# Read the file path from the storage
db_query_result_path = locals().get('var_functions.query_db:0', '')
tables_list_path = locals().get('var_functions.list_db:5', '')

if not db_query_result_path or not os.path.exists(db_query_result_path):
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not find the stock list file'}))
elif not tables_list_path or not os.path.exists(tables_list_path):
    print('__RESULT__:')
    print(json.dumps({'error': 'Could not find the tables list file'}))
else:
    with open(db_query_result_path, 'r') as f:
        nyse_stocks = json.load(f)
    
    with open(tables_list_path, 'r') as f:
        all_tables = json.load(f)
    
    # Get symbols that exist in both
    nyse_symbols = [stock['Symbol'] for stock in nyse_stocks]
    available_symbols = [sym for sym in nyse_symbols if sym in all_tables]
    
    print('__RESULT__:')
    print(json.dumps({
        'total_nyse_stocks': len(nyse_symbols),
        'available_in_trade_db': len(available_symbols),
        'first_few_available': available_symbols[:10]
    }))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'count': 234, 'first_few': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}]}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json'}

exec(code, env_args)
