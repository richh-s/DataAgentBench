code = """import json
from pathlib import Path

uc_path = var_call_49Kxtie9NLEDCwI2oZhVg8MW
uc_recs = json.loads(Path(uc_path).read_text())
import pandas as pd
uc_df = pd.DataFrame(uc_recs)
uc_df['uc_pub'] = uc_df['Patents_info'].str.extract(r'pub\. number\s+([^\.]+)\.')
uc_df['uc_pub2'] = uc_df['Patents_info'].str.extract(r'publication number\s+([^\.]+)\.')
uc_pubs = pd.Series(pd.concat([uc_df['uc_pub'], uc_df['uc_pub2']]).dropna().unique()).tolist()

# Build a single LIKE query using OR (23 items)
conds = []
for p in uc_pubs:
    esc = p.replace("'","''")
    conds.append(f"citation LIKE '%{esc}%'")
where = ' OR '.join(conds)
query = f"SELECT Patents_info, cpc, citation FROM publicationinfo WHERE citation IS NOT NULL AND citation != '' AND ({where});"

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_6GhUfvarjLHE8sfzCxe0mGMv': [], 'var_call_HCbCWAow5fIDZsMHdoDeo4Pv': 'file_storage/call_HCbCWAow5fIDZsMHdoDeo4Pv.json', 'var_call_hsv0knknrti2Eh8U3w7bn1Nh': ['publicationinfo'], 'var_call_acERZDrrBhL3GK3uh1b2Sfd4': 'file_storage/call_acERZDrrBhL3GK3uh1b2Sfd4.json', 'var_call_49Kxtie9NLEDCwI2oZhVg8MW': 'file_storage/call_49Kxtie9NLEDCwI2oZhVg8MW.json', 'var_call_iqsFR2y7D0lkVK9yZVx1mHFV': {'uc_pubs_count': 23, 'sample': ['US-2022074631-A1', 'CN-100339724-C', 'US-2006292670-A1', 'US-11667770-B2', 'AU-2008349842-A1', 'AU-2015364602-B2', 'IL-274176-A', 'AU-2010214112-B2', 'ID-23426-A', 'US-5304932-A']}}

exec(code, env_args)
