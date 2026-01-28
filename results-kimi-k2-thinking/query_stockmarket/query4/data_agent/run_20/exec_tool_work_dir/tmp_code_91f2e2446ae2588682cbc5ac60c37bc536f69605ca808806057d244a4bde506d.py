code = """import json
import os

# Access NYSE stocks data
nyse_file = var_functions.query_db:38

with open(nyse_file, 'r') as f:
    nyse_stocks = json.load(f)

symbols = [s['Symbol'] for s in nyse_stocks]

print('__RESULT__:')
print(json.dumps({
    'total': len(symbols),
    'sample': symbols[:5]
}))"""

env_args = {'var_functions.list_db:0': 'file_storage/functions.list_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'type': 'str', 'length': 38, 'first_item': 'f'}, 'var_functions.query_db:24': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.'}, {'Symbol': 'AL', 'Company Description': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.'}, {'Symbol': 'AMN', 'Company Description': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.'}, {'Symbol': 'AMP', 'Company Description': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.'}, {'Symbol': 'AMT', 'Company Description': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.'}, {'Symbol': 'ARD', 'Company Description': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:34': 'file_storage/functions.list_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
