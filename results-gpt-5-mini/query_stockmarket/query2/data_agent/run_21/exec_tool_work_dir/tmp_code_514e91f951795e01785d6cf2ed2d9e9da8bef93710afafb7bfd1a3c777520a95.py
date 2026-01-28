code = """import json
# var_call_PJv4fEwEjySI9DhFTpfQqJp8 and var_call_ce66kTF43vUEfp0JUMXmCAQY are available in storage
with open(var_call_PJv4fEwEjySI9DhFTpfQqJp8, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ce66kTF43vUEfp0JUMXmCAQY, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo
symbols = [rec['Symbol'] for rec in stockinfo]
# Keep only symbols that have a table in trade_tables
available_symbols = [s for s in symbols if s in trade_tables]
# Output the list
import json
print("__RESULT__:")
print(json.dumps(available_symbols))"""

env_args = {'var_call_PJv4fEwEjySI9DhFTpfQqJp8': 'file_storage/call_PJv4fEwEjySI9DhFTpfQqJp8.json', 'var_call_ce66kTF43vUEfp0JUMXmCAQY': 'file_storage/call_ce66kTF43vUEfp0JUMXmCAQY.json'}

exec(code, env_args)
