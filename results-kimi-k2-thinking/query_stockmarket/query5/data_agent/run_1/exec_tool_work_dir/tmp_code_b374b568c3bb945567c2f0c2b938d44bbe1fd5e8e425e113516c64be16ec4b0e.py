code = """import json

# Get all NASDAQ Capital Market stocks
companies_data = locals()['var_functions.query_db:12']
if isinstance(companies_data, str):
    with open(companies_data, 'r') as f:
        companies_data = json.load(f)

symbols = [c['Symbol'] for c in companies_data]
company_names = {c['Symbol']: c['Company Description'] for c in companies_data}

# Function to count high volatility days
def count_volatility_days(stock_data):
    if not stock_data:
        return 0
    count = 0
    for day in stock_data:
        try:
            high = float(day['High'])
            low = float(day['Low'])
            if low > 0:
                range_pct = (high - low) / low
                if range_pct > 0.20:
                    count += 1
        except (ValueError, TypeError):
            continue
    return count

# Store all results
all_results = [
    # Already processed
    {'symbol': 'AGMH', 'company': company_names['AGMH'], 'volatility_days': 13},
    {'symbol': 'ALACU', 'company': company_names['ALACU'], 'volatility_days': 0},
    {'symbol': 'AMHC', 'company': company_names['AMHC'], 'volatility_days': 0},
    {'symbol': 'ANDA', 'company': company_names['ANDA'], 'volatility_days': 0},
    {'symbol': 'APEX', 'company': company_names['APEX'], 'volatility_days': 15},
    {'symbol': 'BCLI', 'company': company_names['BCLI'], 'volatility_days': 0},
    {'symbol': 'BHAT', 'company': company_names['BHAT'], 'volatility_days': 10},
    {'symbol': 'BIOC', 'company': company_names['BIOC'], 'volatility_days': 21},
    {'symbol': 'BKYI', 'company': company_names['BKYI'], 'volatility_days': 16},
    {'symbol': 'BLFS', 'company': company_names['BLFS'], 'volatility_days': 0},
]

print('__RESULT__:')
print(json.dumps({
    'status': 'ready_to_query_remaining',
    'processed_count': len(all_results),
    'remaining_symbols': symbols[len(all_results):]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:6': 'Total: 86', 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json', 'var_functions.execute_python:10': 'NASDAQ Capital Market stocks (non-ETF): 86', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'symbol_count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_functions.execute_python:16': {'nasdaq_count': 86, 'available_count': 86, 'missing_count': 0, 'sample_available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'sample_missing': []}, 'var_functions.execute_python:18': {'message': 'Ready to process 86 stocks', 'stock_count': 86}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_symbols': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.execute_python:24': {'symbol': 'AGMH', 'company_name': 'AGM Group Holdings Inc. specializes in providing f...', 'total_2019_days': 252, 'high_volatility_days': 13}, 'var_functions.execute_python:26': {'message': 'Ready to query all 86 stocks', 'symbols_to_process': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.execute_python:28': {'action': 'query_all_symbols', 'symbol_count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:31': 'file_storage/functions.query_db:31.json', 'var_functions.query_db:32': [], 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:40': {'status': 'initialized', 'symbol_count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:43': 'file_storage/functions.query_db:43.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:45': 'file_storage/functions.query_db:45.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:52': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatility_days': 13}], 'var_functions.execute_python:54': {'total_symbols': 86, 'queried_so_far': 10, 'remaining_symbols': 76, 'next_batch': ['BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.query_db:56': 'file_storage/functions.query_db:56.json', 'var_functions.query_db:57': 'file_storage/functions.query_db:57.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:59': 'file_storage/functions.query_db:59.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.execute_python:66': [{'symbol': 'AGMH', 'company': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'volatility_days': 13}, {'symbol': 'ALACU', 'company': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'volatility_days': 0}, {'symbol': 'AMHC', 'company': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.', 'volatility_days': 0}, {'symbol': 'ANDA', 'company': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.', 'volatility_days': 0}, {'symbol': 'APEX', 'company': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'volatility_days': 15}], 'var_functions.execute_python:68': [{'symbol': 'BCLI', 'company': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'volatility_days': 0}, {'symbol': 'BHAT', 'company': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'volatility_days': 10}, {'symbol': 'BIOC', 'company': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'volatility_days': 21}, {'symbol': 'BKYI', 'company': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'volatility_days': 16}, {'symbol': 'BLFS', 'company': 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.', 'volatility_days': 0}]}

exec(code, env_args)
