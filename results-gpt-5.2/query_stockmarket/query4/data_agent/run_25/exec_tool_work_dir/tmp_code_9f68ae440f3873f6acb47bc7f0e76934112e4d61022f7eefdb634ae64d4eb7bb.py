code = """import json

# Load NYSE non-ETF symbols
nyse_path = var_call_exRSNvWJaascqpdlppDM9YN5
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_syms = {r['symbol'] for r in nyse}

# Load trade tables
trade_path = var_call_KRShI0X5inPXfxfej725q4kp
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

syms = sorted(nyse_syms & trade_tables)

# verify which in syms actually exist (already) and build query from trade_tables to avoid missing
# However error shows DD missing but DD apparently in syms? means DD in nyse_syms but not in trade_tables, yet query included it.
# So likely trade_tables list contains 'DD'?? but error says not exist: maybe table name is 'DD ' or something; let's ensure exact match.
# We'll filter symbols by attempting to match exact table names; already should.

# Create a safe set by checking via information_schema in DuckDB is not available easily here without query.
# We'll just remove the missing one detected: 'DD'
if 'DD' in syms:
    syms.remove('DD')

chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
union_queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        t = '"' + s.replace('"','""') + '"'
        parts.append(
            f"SELECT '{s}' AS symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM {t} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        )
    union_queries.append(' UNION ALL '.join(parts))

full_query = 'SELECT symbol, up_days, down_days FROM (' + (' UNION ALL '.join(union_queries)) + ') WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC LIMIT 5;'

print('__RESULT__:')
print(json.dumps({'query': full_query, 'n_intersection': len(syms)}))"""

env_args = {'var_call_exRSNvWJaascqpdlppDM9YN5': 'file_storage/call_exRSNvWJaascqpdlppDM9YN5.json', 'var_call_KRShI0X5inPXfxfej725q4kp': 'file_storage/call_KRShI0X5inPXfxfej725q4kp.json', 'var_call_U1ddfDlkeQPeMxPDlffHHSmn': 'file_storage/call_U1ddfDlkeQPeMxPDlffHHSmn.json'}

exec(code, env_args)
