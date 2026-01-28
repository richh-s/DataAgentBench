code = """import json
import pandas as pd

# Read the company mapping from file
stockinfo_path = locals()['var_functions.query_db:30']
if isinstance(stockinfo_path, str):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals()['var_functions.query_db:30']

# Create symbol -> company name mapping for NASDAQ Capital Market companies
company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# Get list of symbols to process
symbols = list(company_map.keys())

# Read available tables in stocktrade database
stocktrade_path = locals()['var_functions.list_db:2']
if isinstance(stocktrade_path, str):
    with open(stocktrade_path, 'r') as f:
        available_tables = json.load(f)
else:
    available_tables = locals()['var_functions.list_db:2']

# Find intersection (NASDAQ Capital Market stocks with trade data)
available_symbols = set(available_tables)
nasdaq_cap_symbols = set(symbols)
eligible_symbols = list(nasdaq_cap_symbols.intersection(available_symbols))

print('__RESULT__:')
print(json.dumps({
    'total_nasdaq_cap_stocks': len(nasdaq_cap_symbols),
    'stocks_with_trade_data': len(available_symbols),
    'eligible_stocks': len(eligible_symbols),
    'sample_eligible': eligible_symbols[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'eligible_count': 86, 'sample_symbols': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR']}, 'var_functions.query_db:6': [{'Date': '2019-01-02', 'High': '7.28000020980835', 'Low': '5.840000152587891'}, {'Date': '2019-01-03', 'High': '7.28000020980835', 'Low': '6.400000095367432'}, {'Date': '2019-01-04', 'High': '8.319999694824219', 'Low': '6.480000019073486'}, {'Date': '2019-01-07', 'High': '7.039999961853027', 'Low': '6.960000038146973'}, {'Date': '2019-01-08', 'High': '7.039999961853027', 'Low': '6.400000095367432'}], 'var_functions.execute_python:8': {'symbols_to_process': 88, 'sample': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'symbol': 'SES', 'company': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'days_2019': 252, 'days_exceeding_20pct': 51, 'calculation_logic_test': 'passed'}, 'var_functions.execute_python:14': {'status': 'starting_batch_process', 'total_symbols': 88, 'batch_size': 20, 'batches': 5, 'first_batch': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR', 'AEGN', 'CPSR', 'YTRA', 'MCC', 'RHE', 'FSTR', 'CPSH', 'PRPO', 'MCHX', 'BLCM']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_symbols': 88, 'sample_queries': ['SELECT Date, High, Low FROM "SES" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'', 'SELECT Date, High, Low FROM "POPE" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'', 'SELECT Date, High, Low FROM "PCSB" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\''], 'company_sample': {'SES': 'Synthesis Energy Systems, Inc. specializes in tran...', 'POPE': 'Pope Resources - Limited Partnership is dedicated ...', 'PCSB': 'PCSB Financial Corporation operates as a community...'}}, 'var_functions.execute_python:22': [{'symbol': 'SES', 'company': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'days_exceeding_20pct': 51, 'total_days': 252}, {'symbol': 'POPE', 'company': 'Pope Resources - Limited Partnership is dedicated to managing timberland and real estate, focusing on sustainable forestry and land development in the Pacific Northwest.', 'days_exceeding_20pct': 0, 'total_days': 252}, {'symbol': 'PCSB', 'company': 'PCSB Financial Corporation operates as a community bank, providing a range of financial services and products to individuals and businesses in its local markets.', 'days_exceeding_20pct': 0, 'total_days': 252}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': [{'symbol': 'SES', 'company': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'days_exceeding_20pct': 51, 'total_days': 252}, {'symbol': 'CEMI', 'company': 'Chembio Diagnostics, Inc. specializes in developing rapid diagnostic tests that help detect infectious diseases, providing crucial solutions for healthcare professionals worldwide.', 'days_exceeding_20pct': 3, 'total_days': 252}, {'symbol': 'POPE', 'company': 'Pope Resources - Limited Partnership is dedicated to managing timberland and real estate, focusing on sustainable forestry and land development in the Pacific Northwest.', 'days_exceeding_20pct': 0, 'total_days': 252}, {'symbol': 'PCSB', 'company': 'PCSB Financial Corporation operates as a community bank, providing a range of financial services and products to individuals and businesses in its local markets.', 'days_exceeding_20pct': 0, 'total_days': 252}, {'symbol': 'ANDA', 'company': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.', 'days_exceeding_20pct': 0, 'total_days': 209}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
