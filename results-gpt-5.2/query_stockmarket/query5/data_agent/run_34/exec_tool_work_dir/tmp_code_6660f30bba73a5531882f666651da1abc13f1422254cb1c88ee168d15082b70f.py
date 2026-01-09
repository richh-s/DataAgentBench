code = """import json, pandas as pd
from pathlib import Path

# load capital market symbols
recs = json.loads(Path(var_call_SJDvuDlh3OpinUytl9I4duYD).read_text())
cap = pd.DataFrame(recs)
cap_syms = set(cap['Symbol'].dropna())

# load available trade tables (tickers)
trade_tables = [r['table_name'] for r in var_call_x9mxXvdmPQWmFCwyWzhCRFI2]
# need full list; query only returned 5, so output that we must fetch all table names
print('__RESULT__:')
print(json.dumps({'cap_n': len(cap_syms), 'trade_tables_preview': trade_tables}))"""

env_args = {'var_call_SJDvuDlh3OpinUytl9I4duYD': 'file_storage/call_SJDvuDlh3OpinUytl9I4duYD.json', 'var_call_kaW2wwsm2FuRm2l6dc9eZPMo': [{'n_tables': '2753'}], 'var_call_x9mxXvdmPQWmFCwyWzhCRFI2': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}]}

exec(code, env_args)
