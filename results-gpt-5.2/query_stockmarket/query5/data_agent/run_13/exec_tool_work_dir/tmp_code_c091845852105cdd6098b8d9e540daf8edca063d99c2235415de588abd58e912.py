code = """import json, pandas as pd

path_info = var_call_UNBMamz12gvCXT5WzkaUkcAA
a = open(path_info,'r')
info = json.load(a)
a.close()
info_df = pd.DataFrame(info)

path_tbl = var_call_K6LcJ7mQSoeipU97uzMMhTVq
b = open(path_tbl,'r')
tbls = json.load(b)
b.close()
tbl_set = set(tbls)

syms = sorted(set(info_df['Symbol']).intersection(tbl_set))

selects = []
for s in syms:
    q = (
        "SELECT '{sym}' AS symbol, COUNT(*)::BIGINT AS cnt "
        "FROM \"{sym}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL "
        "AND (High - Low) / Low > 0.2"
    ).format(sym=s)
    selects.append(q)

if not selects:
    out = json.dumps([])
    print('__RESULT__:')
    print(out)
else:
    union_query = " UNION ALL ".join(selects)
    final_query = "SELECT symbol, SUM(cnt) AS days_exceed_20pct FROM ({u}) t GROUP BY symbol ORDER BY days_exceed_20pct DESC, symbol ASC LIMIT 5;".format(u=union_query)
    out = json.dumps({'query': final_query, 'n_symbols': len(syms)})
    print('__RESULT__:')
    print(out)"""

env_args = {'var_call_UNBMamz12gvCXT5WzkaUkcAA': 'file_storage/call_UNBMamz12gvCXT5WzkaUkcAA.json', 'var_call_K6LcJ7mQSoeipU97uzMMhTVq': 'file_storage/call_K6LcJ7mQSoeipU97uzMMhTVq.json'}

exec(code, env_args)
