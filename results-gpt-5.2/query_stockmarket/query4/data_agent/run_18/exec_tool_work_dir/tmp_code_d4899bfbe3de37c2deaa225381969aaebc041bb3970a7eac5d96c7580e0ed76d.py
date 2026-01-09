code = """import json, pandas as pd

path_info = var_call_zTiNOqsbb8aEMrGQTHPmYH8s
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

path_tables = var_call_HqDnH921PkySWzUaQ71v8H8z
with open(path_tables, 'r') as f:
    tables = json.load(f)
table_set = set(tables)

symbols = [s for s in info_df['symbol'].tolist() if s in table_set]

parts = []
for s in symbols:
    t = s.replace('"','""')
    parts.append(
        "SELECT '{sym}' AS symbol, "
        "SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
        "SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
        "FROM \"{tbl}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'".format(sym=s, tbl=t)
    )

union_sql = "\nUNION ALL\n".join(parts)
final_query = (
    "WITH agg AS (\n" + union_sql +
    "\n)\nSELECT symbol, up_days, down_days, (up_days - down_days) AS diff\n"
    "FROM agg\nWHERE up_days > down_days\nORDER BY diff DESC, up_days DESC\nLIMIT 5;"
)

print('__RESULT__:')
print(json.dumps({'sql': final_query, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_zTiNOqsbb8aEMrGQTHPmYH8s': 'file_storage/call_zTiNOqsbb8aEMrGQTHPmYH8s.json', 'var_call_HqDnH921PkySWzUaQ71v8H8z': 'file_storage/call_HqDnH921PkySWzUaQ71v8H8z.json'}

exec(code, env_args)
