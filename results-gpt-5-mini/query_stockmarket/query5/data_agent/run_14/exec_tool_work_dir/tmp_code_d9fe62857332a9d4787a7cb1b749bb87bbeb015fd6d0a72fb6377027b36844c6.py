code = """import json
import os
# Load previous tool results
# var_call_HGyGjC7o6mlyzGcV9YqRot21 and var_call_EEujyNWciR62lhYczKx9JiG1 are available
data_stockinfo = None
if isinstance(var_call_HGyGjC7o6mlyzGcV9YqRot21, str) and os.path.exists(var_call_HGyGjC7o6mlyzGcV9YqRot21):
    with open(var_call_HGyGjC7o6mlyzGcV9YqRot21, 'r') as f:
        data_stockinfo = json.load(f)
else:
    data_stockinfo = var_call_HGyGjC7o6mlyzGcV9YqRot21

data_stocktrade_tables = None
if isinstance(var_call_EEujyNWciR62lhYczKx9JiG1, str) and os.path.exists(var_call_EEujyNWciR62lhYczKx9JiG1):
    with open(var_call_EEujyNWciR62lhYczKx9JiG1, 'r') as f:
        data_stocktrade_tables = json.load(f)
else:
    data_stocktrade_tables = var_call_EEujyNWciR62lhYczKx9JiG1

# data_stockinfo is a list of dicts with Symbol and Company Description
symbols_info = {item['Symbol']: item.get('Company Description','') for item in data_stockinfo}
# stocktrade tables list
tables = set(data_stocktrade_tables)

# Find symbols that are in both
common_symbols = [s for s in symbols_info.keys() if s in tables]
# Prepare queries
queries = []
for s in common_symbols:
    q = f'SELECT "{s}" AS symbol, COUNT(*) AS cnt FROM "{s}" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND (High - Low) > 0.2 * Low;'
    queries.append({"symbol": s, "company": symbols_info[s], "query": q})

# Limit: if too many queries, keep them all; multi_tool_use can handle many
output = {"count": len(queries), "queries": queries}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_EEujyNWciR62lhYczKx9JiG1': 'file_storage/call_EEujyNWciR62lhYczKx9JiG1.json', 'var_call_HGyGjC7o6mlyzGcV9YqRot21': 'file_storage/call_HGyGjC7o6mlyzGcV9YqRot21.json'}

exec(code, env_args)
