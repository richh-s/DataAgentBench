code = """import json, pandas as pd
import json as js

with open(var_call_bCLQtbyLXZoPE0OHwtZcVuCJ, 'r') as f:
    cit_records = js.load(f)

cit_df = pd.DataFrame(cit_records)
info = {'columns': list(cit_df.columns), 'sample': cit_df.head(5).to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(info))"""

env_args = {'var_call_fQom8adI882atG1Z9SpR4GSk': 'file_storage/call_fQom8adI882atG1Z9SpR4GSk.json', 'var_call_bCLQtbyLXZoPE0OHwtZcVuCJ': 'file_storage/call_bCLQtbyLXZoPE0OHwtZcVuCJ.json', 'var_call_TodI2PcnmfqKoLuXfup6UTch': {'keys': ['title', 'total_citations']}}

exec(code, env_args)
