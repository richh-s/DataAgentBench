code = """import json
import pandas as pd
from pathlib import Path
import re

uc_path = var_call_49Kxtie9NLEDCwI2oZhVg8MW
uc_recs = json.loads(Path(uc_path).read_text()) if isinstance(uc_path, str) else uc_path
uc_df = pd.DataFrame(uc_recs)

uc_df['uc_pub'] = uc_df['Patents_info'].str.extract(r'pub\. number\s+([^\.]+)\.')
uc_df['uc_pub2'] = uc_df['Patents_info'].str.extract(r'publication number\s+([^\.]+)\.')
uc_pubs = pd.Series(pd.concat([uc_df['uc_pub'], uc_df['uc_pub2']]).dropna().unique()).tolist()

print('__RESULT__:')
print(json.dumps({'uc_pubs_count': len(uc_pubs), 'sample': uc_pubs[:10]}))"""

env_args = {'var_call_6GhUfvarjLHE8sfzCxe0mGMv': [], 'var_call_HCbCWAow5fIDZsMHdoDeo4Pv': 'file_storage/call_HCbCWAow5fIDZsMHdoDeo4Pv.json', 'var_call_hsv0knknrti2Eh8U3w7bn1Nh': ['publicationinfo'], 'var_call_acERZDrrBhL3GK3uh1b2Sfd4': 'file_storage/call_acERZDrrBhL3GK3uh1b2Sfd4.json', 'var_call_49Kxtie9NLEDCwI2oZhVg8MW': 'file_storage/call_49Kxtie9NLEDCwI2oZhVg8MW.json'}

exec(code, env_args)
