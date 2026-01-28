code = """import json

# Load NASDAQ Capital Market symbols and company names
symbols_result = locals()['var_functions.query_db:14']
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    nasdaq_cap_stocks = symbols_result

# Create symbol to company description map
symbol_to_company = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_stocks}

# Get list of all tables from stocktrade database
all_tables_result = locals()['var_functions.list_db:5']
if isinstance(all_tables_result, str):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

# Filter to only symbols that have data tables
symbols_with_data = [symbol for symbol in symbol_to_company.keys() if symbol in all_tables]

# Split into batches of 15 symbols each to avoid huge queries
batch_size = 15
batches = [symbols_with_data[i:i+batch_size] for i in range(0, len(symbols_with_data), batch_size)]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols_with_data),
    'total_batches': len(batches),
    'batch_size': batch_size,
    'first_batch': batches[0] if batches else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'], ['BCLI', 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'], ['BHAT', 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'], ['BIOC', 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'], ['BKYI', 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'], ['BLFS', 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.']], 'var_functions.execute_python:8': {'total_nasdaq_cap_symbols': 86, 'total_available_tables': 86, 'sample_symbols': ['VRRM', 'EXPC', 'VERB', 'FNCB', 'ALACU', 'CUBA', 'HQI', 'VMD', 'PLIN', 'ISNS']}, 'var_functions.execute_python:10': {'message': 'Will analyze 86 NASDAQ Capital Market symbols', 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:12': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_symbols': 86, 'symbols_with_tables': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:20': [{'high_volatility_days': '13'}], 'var_functions.execute_python:22': {'total_symbols': 86, 'sample_queries': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'symbol': 'ALACU', 'company': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'symbol': 'AMHC', 'company': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.query_db:24': [{'high_volatility_days': '0'}], 'var_functions.execute_python:28': {'total_symbols': 86, 'query_preview': "SELECT 'AGMH' as Symbol, COUNT(*) as high_volatility_days FROM AGMH WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND ((High - Low) > (0.20 * Low)) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as high_volatility_days FROM ALACU WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND ((High - Low) > (0.20 * Low)) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as high_volatility_days FROM AMHC WH...", 'sample_symbols': ['AGMH', 'ALACU', 'AMHC']}}

exec(code, env_args)
