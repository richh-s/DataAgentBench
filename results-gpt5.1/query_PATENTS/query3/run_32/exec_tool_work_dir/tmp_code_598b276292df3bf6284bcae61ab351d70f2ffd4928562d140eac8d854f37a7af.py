code = """import json, re, pandas as pd, os
path = var_call_FpjW3JkfXY92mTexLxFyRjkQ
with open(path) as f:
    rows = json.load(f)
# build map publication_number -> assignee from Patents_info
pub_to_assignee = {}
for r in rows:
    info = r.get('Patents_info','')
    m_pub = re.search(r'pub. number ([A-Z0-9-]+)', info)
    m_ass = re.search(r'assignee_harmonized: ([^,]+)', info)
    if m_pub and m_ass:
        pub_to_assignee[m_pub.group(1)] = m_ass.group(1).strip()
# now we need citing patents whose citations include a pub number in this set and whose assignee != UNIV CALIFORNIA
univ_pubs = set(pub_to_assignee.keys())
# But our current dataset are only UNIV CALIFORNIA patents, so there will be no such citing patents here.
result = json.dumps({'univ_pubs_count': len(univ_pubs)})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Kk9OwxZzHt7q7EX4uGFvSV8A': [], 'var_call_NrprOQv2RjHwJd2LED8LpNUs': ['cpc_definition'], 'var_call_FpjW3JkfXY92mTexLxFyRjkQ': 'file_storage/call_FpjW3JkfXY92mTexLxFyRjkQ.json', 'var_call_DSOR0p3dc1RS6oE5l2E9bGEF': []}

exec(code, env_args)
