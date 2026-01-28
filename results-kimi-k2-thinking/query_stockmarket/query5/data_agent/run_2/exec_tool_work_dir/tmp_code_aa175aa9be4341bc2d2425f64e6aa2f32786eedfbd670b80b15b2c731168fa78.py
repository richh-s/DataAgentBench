code = """import json

# Load NASDAQ Capital Market symbols and company names
symbols_result = locals()['var_functions.query_db:14']
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    nasdaq_cap_stocks = symbols_result

# Load the list of available tables from stocktrade database
all_tables_result = locals()['var_functions.list_db:5']
if isinstance(all_tables_result, str):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Create mapping of symbol to company description
symbol_to_company = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_stocks}

# Generate all query IDs for NASDAQ Capital Market symbols
symbols = [s for s in symbol_to_company.keys() if s in all_tables]

# Create a plan to query each symbol
query_plan = []
for symbol in symbols:
    query_plan.append({
        'symbol': symbol,
        'company': symbol_to_company[symbol]
    })

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(query_plan),
    'sample_queries': query_plan[:3]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'], ['BCLI', 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'], ['BHAT', 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'], ['BIOC', 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'], ['BKYI', 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'], ['BLFS', 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.']], 'var_functions.execute_python:8': {'total_nasdaq_cap_symbols': 86, 'total_available_tables': 86, 'sample_symbols': ['VRRM', 'EXPC', 'VERB', 'FNCB', 'ALACU', 'CUBA', 'HQI', 'VMD', 'PLIN', 'ISNS']}, 'var_functions.execute_python:10': {'message': 'Will analyze 86 NASDAQ Capital Market symbols', 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:12': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_symbols': 86, 'symbols_with_tables': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:20': [{'high_volatility_days': '13'}]}

exec(code, env_args)
