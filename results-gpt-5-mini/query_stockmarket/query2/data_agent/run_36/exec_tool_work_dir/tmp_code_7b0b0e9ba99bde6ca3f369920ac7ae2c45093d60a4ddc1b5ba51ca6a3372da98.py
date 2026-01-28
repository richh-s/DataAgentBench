code = """import json
# Load the stockinfo query results and list_db results from storage files
with open(var_call_81ZiPdIF1G7CPi99Rtt3w4pr, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ONhfeFX5gPfa2gDRgYKNP6U1, 'r') as f:
    trade_tables = json.load(f)

# Filter stockinfo for ETFs listed on NYSE Arca (Listing Exchange == 'P' already from query)
etf_symbols = [rec['Symbol'] for rec in stockinfo if rec.get('ETF','').upper() == 'Y']
# Ensure symbol exists as a table in the trade database (tables list may be uppercase)
trade_set = set(trade_tables)
symbols_to_check = [s for s in etf_symbols if s in trade_set]

# Output the list of symbols to check as JSON
result = {'symbols_to_check': symbols_to_check}
import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_81ZiPdIF1G7CPi99Rtt3w4pr': 'file_storage/call_81ZiPdIF1G7CPi99Rtt3w4pr.json', 'var_call_ONhfeFX5gPfa2gDRgYKNP6U1': 'file_storage/call_ONhfeFX5gPfa2gDRgYKNP6U1.json'}

exec(code, env_args)
