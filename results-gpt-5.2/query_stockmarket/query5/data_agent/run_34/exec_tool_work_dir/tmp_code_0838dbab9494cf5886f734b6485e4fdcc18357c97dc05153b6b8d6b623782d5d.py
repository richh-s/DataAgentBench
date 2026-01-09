code = """import json, pandas as pd
from pathlib import Path

def qident(x:str)->str:
    return '"' + x.replace('"','""') + '"'

cap_recs = json.loads(Path(var_call_SJDvuDlh3OpinUytl9I4duYD).read_text())
cap_df = pd.DataFrame(cap_recs)
cap_syms = set(cap_df['Symbol'].dropna().astype(str))

all_tables = json.loads(Path(var_call_7Gub8ubmE2rLxG0fbsOksNBt).read_text())
trade_syms = set(r['table_name'] for r in all_tables)

syms = sorted([s for s in cap_syms if (s in trade_syms) and ('#' not in s)])

parts = []
for t in syms:
    parts.append(
        "SELECT '" + t + "' AS Symbol, COUNT(*) AS days_cnt "
        + "FROM " + qident(t) + " "
        + "WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' "
        + "  AND Low IS NOT NULL AND Low > 0 "
        + "  AND High IS NOT NULL "
        + "  AND ((High - Low) / Low) > 0.2"
    )

final_sql = "SELECT Symbol, days_cnt FROM (" + " UNION ALL ".join(parts) + ") ORDER BY days_cnt DESC, Symbol ASC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'sql': final_sql}))"""

env_args = {'var_call_SJDvuDlh3OpinUytl9I4duYD': 'file_storage/call_SJDvuDlh3OpinUytl9I4duYD.json', 'var_call_kaW2wwsm2FuRm2l6dc9eZPMo': [{'n_tables': '2753'}], 'var_call_x9mxXvdmPQWmFCwyWzhCRFI2': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_INbpFJ4xocBqds1y2rCtpr3w': {'cap_n': 86, 'trade_tables_preview': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_call_7Gub8ubmE2rLxG0fbsOksNBt': 'file_storage/call_7Gub8ubmE2rLxG0fbsOksNBt.json', 'var_call_QMTTBr97OmyWtLyYj4O5ENny': 'file_storage/call_QMTTBr97OmyWtLyYj4O5ENny.json', 'var_call_FZjjX1XWIrxUdIBvjnnIFfaY': 'file_storage/call_FZjjX1XWIrxUdIBvjnnIFfaY.json', 'var_call_hyegFmwO2j7RQkZl9RDqPUfV': 'file_storage/call_hyegFmwO2j7RQkZl9RDqPUfV.json', 'var_call_VW7S6EB2uR1L5Uh7q1wXxdgk': [{'table_name': 'MBCN'}, {'table_name': 'MINC'}]}

exec(code, env_args)
