code = """import json, pandas as pd

sym_src = var_call_EJnjIyamO9JbQqPIIhhNpeTp
if isinstance(sym_src, str):
    with open(sym_src, 'r') as f:
        sym_src = json.load(f)
nyse_df = pd.DataFrame(sym_src)

# trade tables list
tbl_src = var_call_cGSbCvlnqeKUTDEQTSOWVQyw
if isinstance(tbl_src, str):
    with open(tbl_src, 'r') as f:
        tbl_src = json.load(f)
trade_tables = sorted(map(str, tbl_src))

# build one union query to find 2017 coverage for all tables
parts = []
for t in trade_tables:
    tn = t.replace('"','""')
    parts.append(
        "SELECT '"+t+"' AS Symbol, COUNT(*) AS n2017 "
        "FROM \""+tn+"\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
    )

# Split to avoid too-long query strings
batch_size = 200
batches = [parts[i:i+batch_size] for i in range(0, len(parts), batch_size)]
union_queries = [" UNION ALL ".join(b) for b in batches]

print('__RESULT__:')
print(json.dumps({'total_tables': len(trade_tables), 'batches': len(union_queries), 'union_queries': union_queries}))"""

env_args = {'var_call_EJnjIyamO9JbQqPIIhhNpeTp': 'file_storage/call_EJnjIyamO9JbQqPIIhhNpeTp.json', 'var_call_cGSbCvlnqeKUTDEQTSOWVQyw': 'file_storage/call_cGSbCvlnqeKUTDEQTSOWVQyw.json', 'var_call_PW3OIINXLTxbFy5Ai7nXKQXQ': 'file_storage/call_PW3OIINXLTxbFy5Ai7nXKQXQ.json', 'var_call_PAIdw1kguTq94xjRH1sgUKGF': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_fexbFCEI7Q8iTms8axE4otfw': [{'n': '0', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_e0TywSJwtnJv4pSpWIKpwNg1': [{'min_date': '2019-10-24', 'max_date': '2020-04-01', 'n': '110'}]}

exec(code, env_args)
