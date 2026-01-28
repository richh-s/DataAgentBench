code = """import json
# var_call_AeR6kf3UFq3lhw6nnOMAdHlH and var_call_5U5XZTdRS5oww3MuO3T3CnEC are available as variables
with open(var_call_AeR6kf3UFq3lhw6nnOMAdHlH, 'r') as f:
    data_stockinfo = json.load(f)
with open(var_call_5U5XZTdRS5oww3MuO3T3CnEC, 'r') as f:
    data_stocktrade = json.load(f)

symbols_stockinfo = [rec['Symbol'] for rec in data_stockinfo]
symbols_stocktrade = data_stocktrade

# Compute intersection and sort
common_symbols = sorted(list(set(symbols_stockinfo).intersection(symbols_stocktrade)))
# Output as JSON string
output = json.dumps(common_symbols)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_AeR6kf3UFq3lhw6nnOMAdHlH': 'file_storage/call_AeR6kf3UFq3lhw6nnOMAdHlH.json', 'var_call_5U5XZTdRS5oww3MuO3T3CnEC': 'file_storage/call_5U5XZTdRS5oww3MuO3T3CnEC.json', 'var_call_tCPkV4jcCKV1GrxX4u7ixHVB': []}

exec(code, env_args)
