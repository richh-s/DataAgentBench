code = """import json
# Load the previous query results from storage files
with open(var_call_CXV6AFYuhWf4cZ3SzcFw0jYo, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_tXOtpY1HEpiyPlku0M5AGz86, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols with Market Category S from stockinfo_records
symbols_s = [rec['Symbol'] for rec in stockinfo_records]
# Filter to those present in trade_tables
trade_set = set(trade_tables)
symbols_to_query = [s for s in symbols_s if s in trade_set]
# Print result as JSON string
import json
print('__RESULT__:')
print(json.dumps(symbols_to_query))"""

env_args = {'var_call_CXV6AFYuhWf4cZ3SzcFw0jYo': 'file_storage/call_CXV6AFYuhWf4cZ3SzcFw0jYo.json', 'var_call_tXOtpY1HEpiyPlku0M5AGz86': 'file_storage/call_tXOtpY1HEpiyPlku0M5AGz86.json'}

exec(code, env_args)
