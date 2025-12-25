code = """import json, re
import pandas as pd

path = var_call_SL5A2udGjvH3mxQZQcbFqudW
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Extract publication_number and assignee from Patents_info
pub_nums = []
assignees = []
for txt in df['Patents_info']:
    m_pub = re.search(r'pub\. number ([A-Z0-9-]+)', txt)
    pub_nums.append(m_pub.group(1) if m_pub else None)
    m_ass = re.search(r'owned by ([^,]+)|assigned to ([^,]+)|holds the .* filing .*?, with', txt)
    assignee = None
    if m_ass:
        assignee = m_ass.group(1) or m_ass.group(2)
    assignees.append(assignee)

df['pub_number'] = pub_nums
df['assignee'] = assignees

# Build a map of cited publication numbers -> set of citing assignees (excluding UNIV CALIFORNIA)
map_cited_to_assignees = {}
for _, row in df.iterrows():
    if not row['citation']:
        continue
    try:
        cites = json.loads(row['citation'])
    except Exception:
        continue
    citing_assignee = row['assignee']
    if not citing_assignee or 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    for c in cites:
        pn = c.get('publication_number')
        if not pn:
            continue
        map_cited_to_assignees.setdefault(pn, set()).add(citing_assignee)

# Now find which of those cited publications are UNIV CALIFORNIA-owned in our db
# First, get all UNIV CALIFORNIA-owned publications with their pub numbers and CPC codes
univ_mask = df['Patents_info'].str.contains('UNIV CALIFORNIA')
uc_df = df[univ_mask].copy()

uc_pub_to_cpc = {}
for _, row in uc_df.iterrows():
    try:
        cpcs = [e['code'] for e in json.loads(row['cpc'])]
    except Exception:
        cpcs = []
    uc_pub_to_cpc[row['pub_number']] = cpcs

# Intersect
records = []
for cited_pn, assignees_set in map_cited_to_assignees.items():
    if cited_pn in uc_pub_to_cpc:
        for ass in assignees_set:
            for code in uc_pub_to_cpc[cited_pn]:
                primary = False
                # mark primary if first & inventive where available; here we approximate: first occurrence
                primary = True
                records.append({'citing_assignee': ass, 'cited_pub_number': cited_pn, 'cpc_code': code})

# Deduplicate
if records:
    rec_df = pd.DataFrame(records).drop_duplicates()
    # keep only main subclass (up to first "/")
    rec_df['cpc_main'] = rec_df['cpc_code'].str.extract(r'(^[^/]+)')[0]
    cpc_codes = sorted(rec_df['cpc_main'].unique().tolist())
else:
    rec_df = pd.DataFrame(columns=['citing_assignee','cited_pub_number','cpc_code','cpc_main'])
    cpc_codes = []

result = {
    'cpc_codes': cpc_codes,
    'relations': rec_df.to_dict(orient='records')
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9Dz8DJfRx31HsA2lht1cm9II': [], 'var_call_6LaFEV8Pl8UD8kcc6KeuJ0CW': [], 'var_call_SL5A2udGjvH3mxQZQcbFqudW': 'file_storage/call_SL5A2udGjvH3mxQZQcbFqudW.json'}

exec(code, env_args)
