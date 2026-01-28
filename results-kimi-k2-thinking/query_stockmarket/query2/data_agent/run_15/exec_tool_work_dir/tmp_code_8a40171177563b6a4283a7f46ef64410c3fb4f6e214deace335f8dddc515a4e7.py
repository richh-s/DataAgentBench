code = """import json
import sqlite3
import os

# Read the NYSE Arca ETF symbols
arca_symbols_file = locals()['var_functions.query_db:0']
with open(arca_symbols_file, 'r') as f:
    arca_symbols_data = json.load(f)

symbols = [item['Symbol'] for item in arca_symbols_data]

# Create a simple batch query approach - query 100 symbols at a time to avoid flooding
def check_high_priced_etfs(symbols_list):
    high_priced_etfs = []
    checked_count = 0
    
    # Process in batches
    batch_size = 100
    for i in range(0, len(symbols_list), batch_size):
        batch = symbols_list[i:i+batch_size]
        checked_count += len(batch)
        
        if i % 500 == 0 and i > 0:
            print(f"Processed {checked_count}/{len(symbols_list)} symbols...")
    
    return high_priced_etfs, checked_count

# Just return a status to see what we're working with
result = {
    'total_symbols_to_check': len(symbols),
    'message': 'Ready to check which ETFs had Adj Close > 200 in 2015'
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:10': {'arca_etf_count': 1435, 'available_in_trade_db': 1435, 'first_available': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': [], 'var_functions.execute_python:16': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_functions.query_db:18': [], 'var_functions.query_db:22': [{'Date': '2015-12-31', 'Adj Close': '37.5300407409668'}, {'Date': '2015-12-30', 'Adj Close': '37.87096405029297'}, {'Date': '2015-12-29', 'Adj Close': '38.065765380859375'}, {'Date': '2015-12-28', 'Adj Close': '37.403419494628906'}, {'Date': '2015-12-24', 'Adj Close': '37.98784637451172'}, {'Date': '2015-12-23', 'Adj Close': '37.865116119384766'}, {'Date': '2015-12-22', 'Adj Close': '37.54372787475586'}, {'Date': '2015-12-21', 'Adj Close': '36.73539733886719'}, {'Date': '2015-12-18', 'Adj Close': '37.183387756347656'}, {'Date': '2015-12-17', 'Adj Close': '37.29051208496094'}]}

exec(code, env_args)
