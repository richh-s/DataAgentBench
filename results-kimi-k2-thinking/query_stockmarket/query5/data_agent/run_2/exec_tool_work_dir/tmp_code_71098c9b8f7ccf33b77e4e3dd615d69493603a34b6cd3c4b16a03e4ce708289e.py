code = """import json
import os

# Check if the database listing is a file path or direct result
all_tables_result = locals()['var_functions.list_db:5']

if isinstance(all_tables_result, str):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Get NASDAQ Capital Market symbols
symbols_result = locals()['var_functions.query_db:0']
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    nasdaq_cap_stocks = symbols_result

# Create symbol to company map
symbol_to_company = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_stocks}

# Find which symbols have tables in stocktrade_database
nasdaq_cap_symbols = list(symbol_to_company.keys())
available_symbols = set(nasdaq_cap_symbols) & set(all_tables)

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap_symbols': len(nasdaq_cap_symbols),
    'total_available_tables': len(available_symbols),
    'sample_symbols': list(available_symbols)[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'], ['BCLI', 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'], ['BHAT', 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'], ['BIOC', 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'], ['BKYI', 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'], ['BLFS', 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.']]}

exec(code, env_args)
