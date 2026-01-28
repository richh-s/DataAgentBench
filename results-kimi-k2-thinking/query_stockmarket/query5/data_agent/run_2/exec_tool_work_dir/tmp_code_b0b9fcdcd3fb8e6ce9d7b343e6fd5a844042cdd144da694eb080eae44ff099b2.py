code = """import json

# Load all accumulated results
all_query_results = []

# Load each batch result
for batch_id in ['var_functions.query_db:32', 'var_functions.query_db:36', 'var_functions.query_db:40', 'var_functions.query_db:44', 'var_functions.query_db:50']:
    batch_result = locals()[batch_id]
    if isinstance(batch_result, str):
        with open(batch_result, 'r') as f:
            all_query_results.extend(json.load(f))
    else:
        all_query_results.extend(batch_result)

# Load remaining symbols
remaining_result = locals()['var_functions.execute_python:48']
if isinstance(remaining_result, str):
    with open(remaining_result, 'r') as f:
        remaining_data = json.load(f)
else:
    remaining_data = remaining_result

remaining_symbols = remaining_data['sample_remaining']  # This is just a sample, need full list

# Actually, let me recalculate remaining symbols properly
symbols_result = locals()['var_functions.query_db:14']
if isinstance(symbols_result, str):
    with open(symbols_result, 'r') as f:
        nasdaq_cap_stocks = json.load(f)
else:
    nasdaq_cap_stocks = symbols_result

symbol_to_company = {item['Symbol']: item['Company Description'] for item in nasdaq_cap_stocks}

all_tables_result = locals()['var_functions.list_db:5']
if isinstance(all_tables_result, str):
    with open(all_tables_result, 'r') as f:
        all_tables = json.load(f)
else:
    all_tables = all_tables_result

all_nasdaq_symbols = [s for s in symbol_to_company.keys() if s in all_tables]
processed_symbols = [item['Symbol'] for item in all_query_results]
remaining_symbols = [s for s in all_nasdaq_symbols if s not in processed_symbols]

print('__RESULT__:')
print(json.dumps({
    'total_processed': len(processed_symbols),
    'remaining_symbols': remaining_symbols,
    'remaining_count': len(remaining_symbols)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': {'total_symbols': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'], ['BCLI', 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.'], ['BHAT', 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.'], ['BIOC', 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'], ['BKYI', 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.'], ['BLFS', 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.']], 'var_functions.execute_python:8': {'total_nasdaq_cap_symbols': 86, 'total_available_tables': 86, 'sample_symbols': ['VRRM', 'EXPC', 'VERB', 'FNCB', 'ALACU', 'CUBA', 'HQI', 'VMD', 'PLIN', 'ISNS']}, 'var_functions.execute_python:10': {'message': 'Will analyze 86 NASDAQ Capital Market symbols', 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:12': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:18': {'total_symbols': 86, 'symbols_with_tables': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.query_db:20': [{'high_volatility_days': '13'}], 'var_functions.execute_python:22': {'total_symbols': 86, 'sample_queries': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'symbol': 'ALACU', 'company': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'symbol': 'AMHC', 'company': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.query_db:24': [{'high_volatility_days': '0'}], 'var_functions.execute_python:28': {'total_symbols': 86, 'query_preview': "SELECT 'AGMH' as Symbol, COUNT(*) as high_volatility_days FROM AGMH WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND ((High - Low) > (0.20 * Low)) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as high_volatility_days FROM ALACU WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND ((High - Low) > (0.20 * Low)) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as high_volatility_days FROM AMHC WH...", 'sample_symbols': ['AGMH', 'ALACU', 'AMHC']}, 'var_functions.execute_python:30': {'total_symbols': 86, 'total_batches': 6, 'batch_size': 15, 'first_batch': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL']}, 'var_functions.query_db:32': [{'Symbol': 'AGMH', 'high_volatility_days': '13'}, {'Symbol': 'ALACU', 'high_volatility_days': '0'}, {'Symbol': 'AMHC', 'high_volatility_days': '0'}, {'Symbol': 'ANDA', 'high_volatility_days': '0'}, {'Symbol': 'APEX', 'high_volatility_days': '15'}, {'Symbol': 'BCLI', 'high_volatility_days': '0'}, {'Symbol': 'BHAT', 'high_volatility_days': '10'}, {'Symbol': 'BIOC', 'high_volatility_days': '21'}, {'Symbol': 'BKYI', 'high_volatility_days': '16'}, {'Symbol': 'BLFS', 'high_volatility_days': '0'}, {'Symbol': 'BOSC', 'high_volatility_days': '3'}, {'Symbol': 'BOTJ', 'high_volatility_days': '0'}, {'Symbol': 'BWEN', 'high_volatility_days': '5'}, {'Symbol': 'CBAT', 'high_volatility_days': '23'}, {'Symbol': 'CCCL', 'high_volatility_days': '13'}], 'var_functions.query_db:36': [{'Symbol': 'CDMOP', 'high_volatility_days': '0'}, {'Symbol': 'CEMI', 'high_volatility_days': '3'}, {'Symbol': 'CFBK', 'high_volatility_days': '0'}, {'Symbol': 'CFFA', 'high_volatility_days': '0'}, {'Symbol': 'CLRB', 'high_volatility_days': '14'}], 'var_functions.execute_python:38': {'batch1_count': 15, 'batch2_count': 5, 'total_so_far': 20, 'sample_results': [{'Symbol': 'AGMH', 'high_volatility_days': '13'}, {'Symbol': 'ALACU', 'high_volatility_days': '0'}, {'Symbol': 'AMHC', 'high_volatility_days': '0'}, {'Symbol': 'ANDA', 'high_volatility_days': '0'}, {'Symbol': 'APEX', 'high_volatility_days': '15'}]}, 'var_functions.query_db:40': [{'Symbol': 'CORV', 'high_volatility_days': '10'}, {'Symbol': 'CPAAU', 'high_volatility_days': '0'}, {'Symbol': 'CPAH', 'high_volatility_days': '16'}, {'Symbol': 'CUBA', 'high_volatility_days': '0'}, {'Symbol': 'CVV', 'high_volatility_days': '0'}, {'Symbol': 'DZSI', 'high_volatility_days': '1'}, {'Symbol': 'ELSE', 'high_volatility_days': '0'}, {'Symbol': 'EXPC', 'high_volatility_days': '0'}, {'Symbol': 'EYEG', 'high_volatility_days': '18'}, {'Symbol': 'FAMI', 'high_volatility_days': '23'}, {'Symbol': 'FNCB', 'high_volatility_days': '1'}, {'Symbol': 'FSBW', 'high_volatility_days': '0'}, {'Symbol': 'FTFT', 'high_volatility_days': '21'}, {'Symbol': 'GDYN', 'high_volatility_days': '0'}, {'Symbol': 'GLG', 'high_volatility_days': '42'}], 'var_functions.query_db:44': [{'Symbol': 'GRNVU', 'high_volatility_days': '0'}, {'Symbol': 'GTEC', 'high_volatility_days': '0'}, {'Symbol': 'HCCOU', 'high_volatility_days': '0'}, {'Symbol': 'HNNA', 'high_volatility_days': '0'}, {'Symbol': 'HQI', 'high_volatility_days': '2'}, {'Symbol': 'HRTX', 'high_volatility_days': '1'}, {'Symbol': 'IDEX', 'high_volatility_days': '15'}, {'Symbol': 'IGIC', 'high_volatility_days': '0'}, {'Symbol': 'IOTS', 'high_volatility_days': '1'}], 'var_functions.execute_python:48': {'total_nasdaq_symbols': 86, 'processed': 44, 'remaining': 42, 'sample_remaining': ['ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR']}, 'var_functions.query_db:50': [{'Symbol': 'ISNS', 'high_volatility_days': '0'}, {'Symbol': 'ITI', 'high_volatility_days': '0'}, {'Symbol': 'LACQ', 'high_volatility_days': '0'}, {'Symbol': 'MBCN', 'high_volatility_days': '0'}, {'Symbol': 'MBNKP', 'high_volatility_days': '0'}, {'Symbol': 'MCEP', 'high_volatility_days': '14'}, {'Symbol': 'MLND', 'high_volatility_days': '3'}, {'Symbol': 'MMAC', 'high_volatility_days': '1'}, {'Symbol': 'MNCLU', 'high_volatility_days': '0'}, {'Symbol': 'MNPR', 'high_volatility_days': '4'}]}

exec(code, env_args)
