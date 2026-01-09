code = """import json
import pandas as pd

with open(var_call_UNBMamz12gvCXT5WzkaUkcAA,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_K6LcJ7mQSoeipU97uzMMhTVq,'r') as f:
    tbls = json.load(f)
tbl_set = set(tbls)

syms = sorted(set(info_df['Symbol']).intersection(tbl_set))

selects = []
for s in syms:
    selects.append("SELECT '{s}' AS symbol, COUNT(*)::BIGINT AS cnt FROM \"{s}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low IS NOT NULL AND Low > 0 AND High IS NOT NULL AND (High - Low) / Low > 0.2".format(s=s))

final_query = "SELECT symbol, SUM(cnt) AS days_exceed_20pct FROM (" + " UNION ALL ".join(selects) + ") t GROUP BY symbol ORDER BY days_exceed_20pct DESC, symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': final_query, 'n_symbols': len(syms)}))"""

env_args = {'var_call_UNBMamz12gvCXT5WzkaUkcAA': 'file_storage/call_UNBMamz12gvCXT5WzkaUkcAA.json', 'var_call_K6LcJ7mQSoeipU97uzMMhTVq': 'file_storage/call_K6LcJ7mQSoeipU97uzMMhTVq.json', 'var_call_paZkjFjx2eBAvI1kSeDJMVGF': 'file_storage/call_paZkjFjx2eBAvI1kSeDJMVGF.json', 'var_call_7qS22m3TaqnEH5BeewS7iMWE': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}]}

exec(code, env_args)
