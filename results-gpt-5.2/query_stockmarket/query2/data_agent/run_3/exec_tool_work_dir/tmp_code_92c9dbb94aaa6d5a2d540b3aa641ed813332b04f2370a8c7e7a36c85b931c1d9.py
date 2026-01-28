code = """import json, pandas as pd
import duckdb

# Load NYSE Arca ETFs
path = var_call_o84Oh8SkIPFhXx6zUTdO5ZJn
with open(path, 'r') as f:
    etfs = json.load(f)

# Determine which tickers have a table in stocktrade_database list
# Load full table list
tbls_path = var_call_oEphkAuLQrFiLRZIfAo1H2KM
with open(tbls_path, 'r') as f:
    tbls = set(json.load(f))

tickers = [r['Symbol'] for r in etfs if r['Symbol'] in tbls]

# Query DuckDB for each ticker's max Adj Close during 2015
con = duckdb.connect(database=':memory:')
con.execute("ATTACH 'stocktrade_database' AS st;")

rows = []
for sym in tickers:
    q = f'''SELECT '{sym}' AS Symbol, MAX("Adj Close") AS max_adj_close_2015
            FROM st."{sym}"
            WHERE "Date" >= '2015-01-01' AND "Date" <= '2015-12-31';'''
    try:
        res = con.execute(q).fetchone()
        rows.append({'Symbol': res[0], 'max_adj_close_2015': res[1]})
    except Exception:
        # skip problematic table names
        continue

res_df = pd.DataFrame(rows)
res_df = res_df.dropna(subset=['max_adj_close_2015'])
above = res_df[res_df['max_adj_close_2015'] > 200].copy()
above = above.sort_values(['Symbol']).reset_index(drop=True)

# Add descriptions
desc = pd.DataFrame(etfs).rename(columns={'company_description':'Company Description'})
final_df = above.merge(desc[['Symbol','Company Description']], on='Symbol', how='left')

out = {
    'total_etfs': int(final_df.shape[0]),
    'etfs': final_df.to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Sk4bpIXrh9p4aw5g9DSpoMFB': ['stockinfo'], 'var_call_oEphkAuLQrFiLRZIfAo1H2KM': 'file_storage/call_oEphkAuLQrFiLRZIfAo1H2KM.json', 'var_call_o84Oh8SkIPFhXx6zUTdO5ZJn': 'file_storage/call_o84Oh8SkIPFhXx6zUTdO5ZJn.json'}

exec(code, env_args)
