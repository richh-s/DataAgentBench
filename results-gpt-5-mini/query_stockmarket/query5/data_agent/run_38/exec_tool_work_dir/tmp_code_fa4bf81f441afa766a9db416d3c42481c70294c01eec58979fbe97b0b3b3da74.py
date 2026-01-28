code = """import json
# Load the market category S symbols and company descriptions from var_call_7VImgvlgFEaHlFsiKpCoAckB
# and the list of available tables from var_call_lbLogyRQLAZG0TxA1yH5r3aq
data_path = var_call_7VImgvlgFEaHlFsiKpCoAckB
tables_path = var_call_lbLogyRQLAZG0TxA1yH5r3aq

with open(data_path, 'r') as f:
    stockinfo_records = json.load(f)
with open(tables_path, 'r') as f:
    trade_tables = json.load(f)

# Build a list of symbols (uppercased) present in both stockinfo (Market Category S) and trade_tables
symbols = []
for rec in stockinfo_records:
    sym = rec.get('Symbol')
    if sym in trade_tables:
        symbols.append({'Symbol': sym, 'Company Description': rec.get('Company Description')})

result = json.dumps(symbols)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_7VImgvlgFEaHlFsiKpCoAckB': 'file_storage/call_7VImgvlgFEaHlFsiKpCoAckB.json', 'var_call_lbLogyRQLAZG0TxA1yH5r3aq': 'file_storage/call_lbLogyRQLAZG0TxA1yH5r3aq.json'}

exec(code, env_args)
