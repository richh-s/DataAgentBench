code = """import json, pandas as pd

# Load NYSE non-ETF symbols
sym_src = var_call_EJnjIyamO9JbQqPIIhhNpeTp
if isinstance(sym_src, str):
    with open(sym_src, 'r') as f:
        sym_src = json.load(f)
nyse_df = pd.DataFrame(sym_src)
nyse_syms = set(nyse_df['Symbol'].astype(str))

# Load trade tables list
tbl_src = var_call_cGSbCvlnqeKUTDEQTSOWVQyw
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tbl_src = json.load(f)
trade_tables = set(map(str, tbl_src))

syms = sorted(nyse_syms.intersection(trade_tables))

batch_size = 200
batches = [syms[i:i+batch_size] for i in range(0, len(syms), batch_size)]

results = []
for batch in batches:
    parts = []
    for s in batch:
        t = s.replace('"','""')
        parts.append(
            "SELECT '"+s+"' AS Symbol, "
            "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            "FROM \""+t+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    q = " UNION ALL ".join(parts)
    recs = functions.query_db(db_name='stocktrade_database', query=q)
    results.extend(recs)

res_df = pd.DataFrame(results)
for c in ['up_days','down_days']:
    res_df[c] = pd.to_numeric(res_df[c], errors='coerce').fillna(0).astype(int)

res_df = res_df[res_df['up_days'] > res_df['down_days']].copy()
res_df['net_up'] = res_df['up_days'] - res_df['down_days']
res_df = res_df.sort_values(['net_up','up_days','down_days','Symbol'], ascending=[False, False, True, True]).head(5)

out = res_df.merge(nyse_df, on='Symbol', how='left')
answer_list = out['company_name'].fillna('').tolist()

print('__RESULT__:')
print(json.dumps({'top5_company_names': answer_list, 'details': out[['Symbol','company_name','up_days','down_days','net_up']].to_dict(orient='records')}))"""

env_args = {'var_call_EJnjIyamO9JbQqPIIhhNpeTp': 'file_storage/call_EJnjIyamO9JbQqPIIhhNpeTp.json', 'var_call_cGSbCvlnqeKUTDEQTSOWVQyw': 'file_storage/call_cGSbCvlnqeKUTDEQTSOWVQyw.json'}

exec(code, env_args)
