code = """import json, re, pandas as pd

# Load UC-assigned publications subset
uc_path = var_call_efT0MFon4DlBI6omonZohoVs
with open(uc_path, 'r', encoding='utf-8') as f:
    uc_recs = json.load(f)

# Build a set of UC publication_numbers to identify cited patents assigned to UC
pub_re = re.compile(r"pub\. number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)")
uc_pubnums = set()
for r in uc_recs:
    m = pub_re.search(r.get('Patents_info','') or '')
    if m:
        uc_pubnums.add(m.group(1))

# Query all publications that cite any of those UC pubnums (string search)
# (SQLite LIKE with ORs)
terms = sorted(uc_pubnums)
# keep manageable: if too many, truncate (but likely ok)
where = " OR ".join([f"citation LIKE '%{t}%'" for t in terms[:400]])
q = f"SELECT Patents_info, cpc, citation FROM publicationinfo WHERE ({where});"

from sqlite3 import connect

# use query_db tool result? cannot. We'll re-query via tool not possible inside python.
# So instead, parse citer assignees from uc_recs? Not correct.

result = {"error":"Need additional query to find citing patents; run query_db on publication_database with citation LIKE UC pubnums."}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_efT0MFon4DlBI6omonZohoVs': 'file_storage/call_efT0MFon4DlBI6omonZohoVs.json', 'var_call_7IGIUZlAUB6KKpkg7CvtV9if': 'file_storage/call_7IGIUZlAUB6KKpkg7CvtV9if.json'}

exec(code, env_args)
