code = """import json, pandas as pd
import json as js

with open(var_call_bCLQtbyLXZoPE0OHwtZcVuCJ, 'r') as f:
    cit_records = js.load(f)

print('__RESULT__:')
print(json.dumps({'keys': list(cit_records[0].keys())}))"""

env_args = {'var_call_fQom8adI882atG1Z9SpR4GSk': 'file_storage/call_fQom8adI882atG1Z9SpR4GSk.json', 'var_call_bCLQtbyLXZoPE0OHwtZcVuCJ': 'file_storage/call_bCLQtbyLXZoPE0OHwtZcVuCJ.json'}

exec(code, env_args)
