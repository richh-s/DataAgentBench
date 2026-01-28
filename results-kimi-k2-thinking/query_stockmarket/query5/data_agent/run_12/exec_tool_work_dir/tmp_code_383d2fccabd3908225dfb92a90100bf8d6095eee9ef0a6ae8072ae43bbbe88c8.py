code = """import json

# Load the full NASDAQ Capital Market symbols data
with open('file_storage/functions.query_db:0.json', 'r') as f:
    nasdaq_cap_symbols = json.load(f)

# Create a list of symbols to process
symbols_to_process = [item['Symbol'] for item in nasdaq_cap_symbols]
company_descriptions = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_symbols}

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols_to_process),
    'symbols': symbols_to_process,
    'sample_descriptions': dict(list(company_descriptions.items())[:3])
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:10': {'nasdaq_cap_type': "<class 'str'>", 'nasdaq_cap_len': 38, 'nasdaq_cap_sample': 'file_storage/functions.query_db:0.json', 'available_tables_type': "<class 'str'>", 'available_tables_len': 37, 'available_tables_sample': 'file_storage/functions.list_db:2.json'}, 'var_functions.execute_python:12': {'total_nasdaq_cap_symbols': 86, 'symbols_with_data': 86, 'sample_symbols': [{'symbol': 'AGMH', 'description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'symbol': 'ALACU', 'description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'symbol': 'AMHC', 'description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'symbol': 'ANDA', 'description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'symbol': 'APEX', 'description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}, {'symbol': 'BCLI', 'description': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'}, {'symbol': 'BHAT', 'description': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'}, {'symbol': 'BIOC', 'description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'symbol': 'BKYI', 'description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'}, {'symbol': 'BLFS', 'description': 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.'}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
