code = """import json
# Load the previous large results from storage keys
p1 = var_call_Y7rxCrvX6WVPPi3ugiwhDD9v
p2 = var_call_VuyiRNBM8CKaNAkawM6Ve5v7

def load_json_var(p):
    if isinstance(p, str):
        with open(p, 'r') as f:
            return json.load(f)
    return p

stockinfo = load_json_var(p1)
trade_tables = load_json_var(p2)

# Extract symbols from stockinfo (Market Category = 'S' was already filtered in query)
symbols = [rec['Symbol'] for rec in stockinfo]
# trade_tables is list of table names
trade_set = set(trade_tables)
# Intersection
symbols_in_trade = [s for s in symbols if s in trade_set]

# Print the result as JSON list
result = json.dumps(symbols_in_trade)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Y7rxCrvX6WVPPi3ugiwhDD9v': 'file_storage/call_Y7rxCrvX6WVPPi3ugiwhDD9v.json', 'var_call_VuyiRNBM8CKaNAkawM6Ve5v7': 'file_storage/call_VuyiRNBM8CKaNAkawM6Ve5v7.json'}

exec(code, env_args)
