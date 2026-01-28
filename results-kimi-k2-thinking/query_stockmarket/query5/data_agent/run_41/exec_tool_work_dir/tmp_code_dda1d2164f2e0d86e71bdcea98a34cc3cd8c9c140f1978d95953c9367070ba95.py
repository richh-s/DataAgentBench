code = """import json
import re

# Load NASDAQ Capital Market stocks
stockinfo_path = locals()['var_functions.query_db:0']
with open(stockinfo_path, 'r') as f:
    nasdaq_stocks = json.load(f)

# Create mapping of symbol to company description
symbol_to_company = {stock['Symbol']: stock['Company Description'] for stock in nasdaq_stocks}
symbols = list(symbol_to_company.keys())

# Generate SQL queries for each symbol
queries = []
for symbol in symbols:
    # Escape quotes in symbol names if any
    safe_symbol = f'"{symbol}"' if not symbol.startswith('"') else symbol
    query = f"""
    SELECT '{symbol}' as Symbol, 
           COUNT(*) as high_volatility_days 
    FROM {safe_symbol} 
    WHERE Date >= '2019-01-01' AND 
          Date <= '2019-12-31' AND 
          (High - Low) > (Low * 0.20)
    """.strip()
    queries.append(query)

# Combine into union query
union_query = ' UNION ALL '.join(queries) + ' ORDER BY high_volatility_days DESC LIMIT 10'

print('__RESULT__:')
print(json.dumps(union_query))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'count': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:10': {'total_tables': 2753, 'sample': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ', 'ABEQ', 'ABMD', 'ACAD', 'ACES', 'ACIO']}, 'var_functions.execute_python:12': {'nasdaq_capital_count': 86, 'available_in_stocktrade': 86, 'sample_symbols': ['BWEN', 'SSNT', 'HQI', 'FSBW', 'CCCL', 'CUBA', 'WHLM', 'IGIC', 'CPAH', 'FTFT']}, 'var_functions.query_db:14': [{'high_volatility_days': '13'}]}

exec(code, env_args)
