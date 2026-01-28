code = """import json

# Load NASDAQ Capital Market stocks
with open('file_storage/functions.query_db:0.json', 'r') as f:
    stockinfo_records = json.load(f)

# Extract symbols
symbols = [rec['Symbol'] for rec in stockinfo_records]

print('__RESULT__:')
print(json.dumps({
    'total_symbols': len(symbols),
    'symbols': symbols
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'file_path': 'file_storage/functions.query_db:0.json', 'status': 'file_path_retrieved'}, 'var_functions.execute_python:6': {'total_stocks': 86, 'sample_records': [{'Symbol': 'AGMH', 'Market Category': 'S', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.', 'Listing Exchange': 'Q'}, {'Symbol': 'ALACU', 'Market Category': 'S', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.', 'Listing Exchange': 'Q'}, {'Symbol': 'AMHC', 'Market Category': 'S', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.', 'Listing Exchange': 'Q'}], 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.list_db:8': 'file_storage/functions.list_db:8.json'}

exec(code, env_args)
