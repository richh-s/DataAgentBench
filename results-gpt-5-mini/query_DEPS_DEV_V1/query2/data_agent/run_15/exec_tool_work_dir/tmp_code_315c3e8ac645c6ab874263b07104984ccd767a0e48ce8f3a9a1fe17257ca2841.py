code = """import json
# We'll load the generated query from previous storage file and trim it to a reasonable number of tuples
path = var_call_j5nh3QRkcOIwMMc0xyRfWypX
with open(path, 'r', encoding='utf-8') as f:
    obj = json.load(f)
query = obj['query']
# Trim the IN list to first 200 tuples to avoid parser limits
start = query.find('IN (')
if start != -1:
    prefix = query[:start+4]
    rest = query[start+4:]
    # find closing ); at end
    end = rest.rfind(');')
    if end!=-1:
        inner = rest[:end]
    else:
        inner = rest
    # split tuples
    tuples = inner.split('),(')
    tuples = [t.strip('()') for t in tuples]
    tuples = tuples[:200]
    new_inner = ','.join(['('+t+')' for t in tuples])
    new_query = prefix + new_inner + ');'
else:
    new_query = query
output = {'query': new_query}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_mtrPk4lBt9oRBdOdheZeKJcw': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json', 'var_call_NfH6qyUofiDUnG2SC01PQ4Tb': 'file_storage/call_mtrPk4lBt9oRBdOdheZeKJcw.json', 'var_call_j5nh3QRkcOIwMMc0xyRfWypX': 'file_storage/call_j5nh3QRkcOIwMMc0xyRfWypX.json'}

exec(code, env_args)
