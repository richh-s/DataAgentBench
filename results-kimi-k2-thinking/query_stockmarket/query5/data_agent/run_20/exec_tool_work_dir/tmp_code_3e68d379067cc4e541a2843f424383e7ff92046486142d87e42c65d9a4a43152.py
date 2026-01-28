code = """import json
import pandas as pd

# Read the full results from the stockinfo query
with open('var_functions.query_db:4.txt', 'r') as f:
    stockinfo_data = json.load(f)

# Print the count and first few records
print(f'Total NASDAQ Capital Market stocks found: {len(stockinfo_data)}')
print('First 5 records:')
for i, rec in enumerate(stockinfo_data[:5]):
    print(f"  {i+1}. {rec['Symbol']}: {rec['Company Description'][:60]}...")

# Extract symbols list
symbols = [rec['Symbol'] for rec in stockinfo_data]

# Result
result = {
    'total_count': len(stockinfo_data),
    'symbols': symbols,
    'sample_entries': stockinfo_data[:5]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BCLI', 'Company Description': 'Brainstorm Cell Therapeutics Inc. is pioneering advancements in regenerative medicine, focusing on developing innovative stem cell therapies for neurodegenerative diseases.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BHAT', 'Company Description': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BIOC', 'Company Description': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BKYI', 'Company Description': 'BIO-key International, Inc. specializes in advanced biometric solutions, providing secure and convenient identity verification systems for enterprises and consumers alike.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}, {'Symbol': 'BLFS', 'Company Description': 'BioLife Solutions, Inc. specializes in developing and manufacturing biopreservation tools that enhance the storage and transport of cells and tissues, playing a crucial role in advancing regenerative medicine and cell therapy.', 'Nasdaq Traded': 'Y', 'Market Category': 'S', 'ETF': 'N'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
