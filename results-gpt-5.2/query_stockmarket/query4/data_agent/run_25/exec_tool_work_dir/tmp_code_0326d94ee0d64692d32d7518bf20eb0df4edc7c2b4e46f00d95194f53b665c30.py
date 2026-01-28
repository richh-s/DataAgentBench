code = """import json, pandas as pd

# Load NYSE non-ETF symbols
nyse_path = var_call_exRSNvWJaascqpdlppDM9YN5
with open(nyse_path, 'r') as f:
    nyse = json.load(f)
nyse_syms = {r['symbol'] for r in nyse}

# Load available trade tables
trade_path = var_call_KRShI0X5inPXfxfej725q4kp
with open(trade_path, 'r') as f:
    trade_tables = set(json.load(f))

# Intersection: symbols we can compute from
syms = sorted(nyse_syms & trade_tables)

# Chunk symbols to limit SQL query length
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
union_queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        # Quote table name for DuckDB
        t = '"' + s.replace('"','""') + '"'
        parts.append(
            f"SELECT '{s}' AS symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM {t} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        )
    union_queries.append(' UNION ALL '.join(parts))

full_query = 'SELECT symbol, up_days, down_days FROM (' + (' UNION ALL '.join(union_queries)) + ') WHERE up_days > down_days ORDER BY (up_days - down_days) DESC, up_days DESC LIMIT 5;'

out = {
    'n_nyse_non_etf_symbols': len(nyse_syms),
    'n_trade_tables': len(trade_tables),
    'n_intersection': len(syms),
    'query': full_query
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_exRSNvWJaascqpdlppDM9YN5': 'file_storage/call_exRSNvWJaascqpdlppDM9YN5.json', 'var_call_KRShI0X5inPXfxfej725q4kp': 'file_storage/call_KRShI0X5inPXfxfej725q4kp.json'}

exec(code, env_args)
