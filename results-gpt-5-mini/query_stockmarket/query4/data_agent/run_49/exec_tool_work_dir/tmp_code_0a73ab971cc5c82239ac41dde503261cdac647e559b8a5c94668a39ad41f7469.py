code = """import json
# Load the stored results from previous queries
with open(var_call_Ls30NOC52bmfXM7RxZntF2Om, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_S3eyWjpLEZEkeZSJPgj1iib7, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols and company descriptions from stockinfo_records
symbols = [rec['Symbol'] for rec in stockinfo_records]
comp_map = {rec['Symbol']: rec['Company Description'] for rec in stockinfo_records}
# Intersect with trade_tables
symbols_to_query = [s for s in symbols if s in trade_tables]
# Prepare output
out = {'symbols_to_query': symbols_to_query, 'company_map': comp_map}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_Ls30NOC52bmfXM7RxZntF2Om': 'file_storage/call_Ls30NOC52bmfXM7RxZntF2Om.json', 'var_call_S3eyWjpLEZEkeZSJPgj1iib7': 'file_storage/call_S3eyWjpLEZEkeZSJPgj1iib7.json'}

exec(code, env_args)
