code = """import json
import pandas as pd
# var_call_rXv6uZ0DDNksTWfPiVrfTqtu and var_call_5jcJoDfvBouMTBJgTuzgin4N are available from storage
records = pd.DataFrame(var_call_rXv6uZ0DDNksTWfPiVrfTqtu)
tables = list(var_call_5jcJoDfvBouMTBJgTuzgin4N)
# Prepare mapping of symbol to company description for NYSE non-ETF from stockinfo query
records = records.dropna(subset=['Symbol'])
records['Symbol'] = records['Symbol'].astype(str)
# Only include symbols present in stocktrade tables
tables_set = set(tables)
records['in_trade_db'] = records['Symbol'].apply(lambda s: s in tables_set)
filtered = records[records['in_trade_db'] == True]
# Build list and mapping
symbols = filtered['Symbol'].tolist()
mapping = dict(zip(filtered['Symbol'].tolist(), filtered['Company Description'].tolist()))
result = {'count': len(symbols), 'symbols': symbols, 'mapping_sample': {k: mapping[k] for k in list(mapping)[:20]}}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rXv6uZ0DDNksTWfPiVrfTqtu': 'file_storage/call_rXv6uZ0DDNksTWfPiVrfTqtu.json', 'var_call_5jcJoDfvBouMTBJgTuzgin4N': 'file_storage/call_5jcJoDfvBouMTBJgTuzgin4N.json'}

exec(code, env_args)
