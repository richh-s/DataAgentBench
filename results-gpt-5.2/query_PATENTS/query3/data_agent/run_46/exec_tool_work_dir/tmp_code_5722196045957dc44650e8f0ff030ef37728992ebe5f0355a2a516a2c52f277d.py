code = """import json, pandas as pd
from pathlib import Path

# Load UC-owned publications
uc_path = var_call_49Kxtie9NLEDCwI2oZhVg8MW
uc_recs = json.loads(Path(uc_path).read_text()) if isinstance(uc_path,str) else uc_path
uc_df = pd.DataFrame(uc_recs)

# Extract UC publication numbers
import re
uc_df['uc_pub'] = uc_df['Patents_info'].str.extract(r'pub\. number\s+([^\.]+)\.')
uc_df['uc_pub2'] = uc_df['Patents_info'].str.extract(r'publication number\s+([^\.]+)\.')
uc_pubs = pd.Series(pd.concat([uc_df['uc_pub'], uc_df['uc_pub2']]).dropna().unique()).tolist()

# Query all publications that cite any UC pub number
# SQLite has limit on variable number, so chunk
chunks = [uc_pubs[i:i+400] for i in range(0,len(uc_pubs),400)]
all_citers = []

for ch in chunks:
    in_list = ','.join(["'"+p.replace("'","''")+"'" for p in ch])
    q = f"""
    SELECT Patents_info, cpc, citation
    FROM publicationinfo
    WHERE citation IS NOT NULL AND citation != ''
      AND (
        {' OR '.join([f"citation LIKE '%{p.replace("'","''")}%'" for p in ch])}
      );
    """
    # can't run SQL here; instead store queries? We must use query_db tool, so skip

print('__RESULT__:')
print(json.dumps({'uc_pubs_count': len(uc_pubs)}))"""

env_args = {'var_call_6GhUfvarjLHE8sfzCxe0mGMv': [], 'var_call_HCbCWAow5fIDZsMHdoDeo4Pv': 'file_storage/call_HCbCWAow5fIDZsMHdoDeo4Pv.json', 'var_call_hsv0knknrti2Eh8U3w7bn1Nh': ['publicationinfo'], 'var_call_acERZDrrBhL3GK3uh1b2Sfd4': 'file_storage/call_acERZDrrBhL3GK3uh1b2Sfd4.json', 'var_call_49Kxtie9NLEDCwI2oZhVg8MW': 'file_storage/call_49Kxtie9NLEDCwI2oZhVg8MW.json'}

exec(code, env_args)
