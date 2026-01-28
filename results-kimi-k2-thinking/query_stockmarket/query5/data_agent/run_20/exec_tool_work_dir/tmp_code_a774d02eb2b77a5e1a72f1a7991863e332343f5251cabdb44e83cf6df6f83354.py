code = """import json

# Get the file path from previous storage
file_path = locals()['var_functions.query_db:4']

# Read the complete list of NASDAQ Capital Market stocks
with open(file_path, 'r') as f:
    stockinfo_data = json.load(f)

# Create a dictionary mapping symbols to company descriptions
symbol_to_company = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

print(f'Total NASDAQ Capital Market stocks: {len(symbol_to_company)}')
print('Sample:')
for symbol in list(symbol_to_company.keys())[:10]:
    print(f'  {symbol}: {symbol_to_company[symbol][:60]}...')

result = {
    'total_stocks': len(symbol_to_company),
    'symbols': list(symbol_to_company.keys()),
    'symbol_to_company': symbol_to_company
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BCLI', 'Company Description': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BHAT', 'Company Description': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BLFS', 'Company Description': 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'total_stocks': 86, 'first_10_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}}

exec(code, env_args)
