code = """import json, pandas as pd
from pathlib import Path

# top symbols
top = pd.DataFrame(var_call_kVKKwrehLqlhoQ4k41BApfA6)

cap = pd.DataFrame(json.loads(Path(var_call_SJDvuDlh3OpinUytl9I4duYD).read_text()))
cap = cap.rename(columns={'company_name':'Company'})

merged = top.merge(cap[['Symbol','company_name']], on='Symbol', how='left')
companies = merged['company_name'].fillna(merged['Symbol']).tolist()

print('__RESULT__:')
print(json.dumps(companies))"""

env_args = {'var_call_SJDvuDlh3OpinUytl9I4duYD': 'file_storage/call_SJDvuDlh3OpinUytl9I4duYD.json', 'var_call_kaW2wwsm2FuRm2l6dc9eZPMo': [{'n_tables': '2753'}], 'var_call_x9mxXvdmPQWmFCwyWzhCRFI2': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_INbpFJ4xocBqds1y2rCtpr3w': {'cap_n': 86, 'trade_tables_preview': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_call_7Gub8ubmE2rLxG0fbsOksNBt': 'file_storage/call_7Gub8ubmE2rLxG0fbsOksNBt.json', 'var_call_QMTTBr97OmyWtLyYj4O5ENny': 'file_storage/call_QMTTBr97OmyWtLyYj4O5ENny.json', 'var_call_FZjjX1XWIrxUdIBvjnnIFfaY': 'file_storage/call_FZjjX1XWIrxUdIBvjnnIFfaY.json', 'var_call_hyegFmwO2j7RQkZl9RDqPUfV': 'file_storage/call_hyegFmwO2j7RQkZl9RDqPUfV.json', 'var_call_VW7S6EB2uR1L5Uh7q1wXxdgk': [{'table_name': 'MBCN'}, {'table_name': 'MINC'}], 'var_call_7A8PLtJ9TfWc2E8xIEq1r8gX': 'file_storage/call_7A8PLtJ9TfWc2E8xIEq1r8gX.json', 'var_call_LCQUH9ew75IGd7ERaGTeQy8h': 'file_storage/call_LCQUH9ew75IGd7ERaGTeQy8h.json', 'var_call_kVKKwrehLqlhoQ4k41BApfA6': [{'Symbol': 'GLG', 'days_cnt': '42'}, {'Symbol': 'CBAT', 'days_cnt': '23'}, {'Symbol': 'FAMI', 'days_cnt': '23'}, {'Symbol': 'BIOC', 'days_cnt': '21'}, {'Symbol': 'FTFT', 'days_cnt': '21'}]}

exec(code, env_args)
