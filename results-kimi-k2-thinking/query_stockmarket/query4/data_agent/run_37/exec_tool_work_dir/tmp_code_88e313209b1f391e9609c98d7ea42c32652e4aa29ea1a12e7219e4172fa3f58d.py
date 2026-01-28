code = """# Load and organize the stockinfo data
import json

# Get file paths
stockinfo_file = locals()['var_functions.query_db:2']

# Load stockinfo data
with open(stockinfo_file, 'r') as f:
    stockinfo_data = json.load(f)

# Create symbol to company name mapping
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in stockinfo_data}
symbols = list(symbol_to_company.keys())

print(f"Total NYSE non-ETF symbols to analyze: {len(symbols)}")
print(f"Sample symbols: {symbols[:5]}")

# Prepare for analysis - we'll examine each stock's 2017 performance
analysis_plan = {
    'total_stocks': len(symbols),
    'sample_symbols': symbols[:10],
    'symbol_to_company': symbol_to_company
}

print('__RESULT__:')
print(json.dumps(analysis_plan))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:12': {'stockinfo_count': 234, 'trade_tables_count': 2753, 'available_symbols_count': 234, 'sample_available': ['ASG', 'MED', 'DTQ', 'SRC', 'ZTR', 'SPOT', 'ORAN', 'TPH', 'RWT', 'ORN', 'CVX', 'IT', 'WOR', 'MANU', 'VKQ', 'IBM', 'HIO', 'CXH', 'DDT', 'SLF']}, 'var_functions.execute_python:14': {'symbols_to_analyze': 234, 'sample_data': [{'Symbol': 'AEFC', 'Company': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AIN', 'Company': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AIV', 'Company': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AIZP', 'Company': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AJRD', 'Company': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AL', 'Company': 'Air Lease Corporation specializes in leasing commercial aircraft to airlines worldwide, providing them with flexible fleet solutions and financial support.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AMN', 'Company': 'AMN Healthcare Services Inc. specializes in providing workforce solutions and staffing services to healthcare facilities, ensuring they have access to the skilled professionals necessary for quality patient care.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AMP', 'Company': 'Ameriprise Financial, Inc. offers comprehensive financial services, specializing in wealth management, asset management, and insurance solutions to help clients plan and achieve their financial goals.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'AMT', 'Company': 'American Tower Corporation is a leading real estate investment trust that specializes in owning, operating, and developing wireless and broadcast communication towers across the globe.', 'up_days': 0, 'down_days': 0, 'total_days': 0}, {'Symbol': 'ARD', 'Company': 'Ardagh Group S.A. specializes in manufacturing and supplying sustainable packaging solutions, with a focus on glass and metal containers for leading brands across various industries.', 'up_days': 0, 'down_days': 0, 'total_days': 0}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
