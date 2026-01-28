code = """import json
# Read storage files
with open(var_call_rRmEOQdBJdvZ2MWsGvcVRR1D, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_TNNo3PG04ccYq62LaQbnWW9w, 'r') as f:
    trade_tables = json.load(f)
# Extract symbols from stockinfo (Listing Exchange 'N' already filtered in query)
symbols = [rec['Symbol'] for rec in stockinfo]
# Intersect with trade_tables
trade_set = set(trade_tables)
symbols_in_trade = [s for s in symbols if s in trade_set]
# Build union SQL
parts = []
for s in symbols_in_trade:
    part = f"SELECT '{s}' AS symbol, SUM(CASE WHEN \"Close\">\"Open\" AND \"Date\">='2017-01-01' AND \"Date\'<='2017-12-31' THEN 1 ELSE 0 END) AS up, SUM(CASE WHEN \"Close\"<\"Open\" AND \"Date\">='2017-01-01' AND \"Date\'<='2017-12-31' THEN 1 ELSE 0 END) AS down FROM \"{s}\""
    parts.append(part)
sql = '\nUNION ALL\n'.join(parts)
# Print result as JSON string
import json
out = json.dumps(sql)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rRmEOQdBJdvZ2MWsGvcVRR1D': 'file_storage/call_rRmEOQdBJdvZ2MWsGvcVRR1D.json', 'var_call_TNNo3PG04ccYq62LaQbnWW9w': 'file_storage/call_TNNo3PG04ccYq62LaQbnWW9w.json'}

exec(code, env_args)
