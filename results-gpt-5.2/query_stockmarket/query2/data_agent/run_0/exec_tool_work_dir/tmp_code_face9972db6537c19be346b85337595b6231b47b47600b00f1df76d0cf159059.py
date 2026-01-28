code = """import json

# tickers list
with open(var_call_bavIZzqXN7oDpRfSFpYuYorR,'r') as f:
    etfs = json.load(f)

tickers = sorted({r['Symbol'] for r in etfs})

# Build UNION ALL query for max Adj Close in 2015 per ticker
parts = []
for t in tickers:
    parts.append(f"SELECT '{t}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

query = "\nUNION ALL\n".join(parts)

print('__RESULT__:')
print(json.dumps({'union_query': query, 'ticker_count': len(tickers)}))"""

env_args = {'var_call_MDAuedzCPOgAQD2J4pERdoeB': ['stockinfo'], 'var_call_bavIZzqXN7oDpRfSFpYuYorR': 'file_storage/call_bavIZzqXN7oDpRfSFpYuYorR.json', 'var_call_OZ4dLgiitANHzlGBCgnXcXoE': 'file_storage/call_OZ4dLgiitANHzlGBCgnXcXoE.json', 'var_call_S9xAimDSkqN7IpIX1QXr3f3E': {'total_arca_etfs': 1435, 'valid_with_trade_table': 1435, 'excluded_nonqueryable_or_missing_table': [], 'excluded_count': 0}, 'var_call_S8YwUrpjgmf7Vsg7RFfVLuva': 'file_storage/call_S8YwUrpjgmf7Vsg7RFfVLuva.json'}

exec(code, env_args)
