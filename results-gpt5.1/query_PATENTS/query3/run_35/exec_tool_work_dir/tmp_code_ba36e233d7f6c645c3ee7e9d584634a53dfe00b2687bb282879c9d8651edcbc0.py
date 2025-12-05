code = """import json, re, pandas as pd
from collections import defaultdict

path = var_call_jfrFJs9OeS0y86we5Akc0AHE
with open(path, 'r') as f:
    data = json.load(f)

# Helper to extract publication_number and assignee from Patents_info
assignee_pub_pattern = re.compile(r"pub\. number ([A-Z0-9\-]+)")
assignee_name_pattern = re.compile(r"owned by ([^,]+)|assigned to ([^,]+)|is owned by ([^,]+)|holds the .* patent filing.* is (?:owned by|assigned to) ([^,]+)")

pub_to_assignee = {}
for rec in data:
    info = rec.get('Patents_info','')
    m_pub = assignee_pub_pattern.search(info)
    if not m_pub:
        continue
    pub_num = m_pub.group(1)
    m_assignee = assignee_name_pattern.search(info)
    if m_assignee:
        assignee = next(g for g in m_assignee.groups() if g)
    else:
        # fallback: look for 'owned by X' or 'assigned to X' patterns more loosely
        m2 = re.search(r"(owned by|assigned to) ([^.,]+)", info)
        assignee = m2.group(2) if m2 else None
    if assignee:
        pub_to_assignee[pub_num] = assignee.strip()

# Build mapping of cited publication_number -> list of citing assignees (excluding UC itself)
cited_to_assignees = defaultdict(set)

for rec in data:
    citations_raw = rec.get('citation','')
    try:
        citations = json.loads(citations_raw) if citations_raw else []
    except json.JSONDecodeError:
        continue
    info = rec.get('Patents_info','')
    m_pub = assignee_pub_pattern.search(info)
    if not m_pub:
        continue
    citing_pub = m_pub.group(1)
    citing_assignee = pub_to_assignee.get(citing_pub)
    if not citing_assignee:
        continue
    for c in citations:
        pub_cited = c.get('publication_number')
        if not pub_cited:
            continue
        cited_to_assignees[pub_cited].add(citing_assignee)

# Now find which of the cited publications are owned by UNIV CALIFORNIA
uc_pubs = {pub for pub, assignee in pub_to_assignee.items() if assignee.strip().upper() == 'UNIV CALIFORNIA'}

# For those, gather CPC codes and citing assignees
records = []
for rec in data:
    info = rec.get('Patents_info','')
    m_pub = assignee_pub_pattern.search(info)
    if not m_pub:
        continue
    pub_num = m_pub.group(1)
    if pub_num not in uc_pubs:
        continue
    cpc_raw = rec.get('cpc','')
    try:
        cpcs = json.loads(cpc_raw) if cpc_raw else []
    except json.JSONDecodeError:
        continue
    # primary CPC subclasses: those with first=True and inventive=True
    primary_codes = [c['code'] for c in cpcs if c.get('first') and c.get('inventive')]
    citing_assignees = [a for a in cited_to_assignees.get(pub_num, set()) if a.upper() != 'UNIV CALIFORNIA']
    for assignee in citing_assignees:
        for code in primary_codes:
            # Take subclass portion: up to "/" (inclusive) or space
            m = re.match(r"([A-Z]\d+[A-Z]\s*\d+/\d+|[A-Z]\d+[A-Z]\s*\d+)", code)
            subclass = code if not m else m.group(0).replace(' ', '')
            records.append({'citing_assignee': assignee, 'cpc_code': subclass})

# Deduplicate
if records:
    df = pd.DataFrame(records).drop_duplicates()
    unique_codes = sorted(df['cpc_code'].unique())
else:
    df = pd.DataFrame(columns=['citing_assignee','cpc_code'])
    unique_codes = []

result = {
    'assignee_cpc_pairs': df.to_dict(orient='records'),
    'unique_cpc_codes': unique_codes
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_v8U1elSB3IftvuCxRYCKMmdR': [], 'var_call_vX99LTJDnc1uFPTuZA6UbNDV': ['cpc_definition'], 'var_call_jfrFJs9OeS0y86we5Akc0AHE': 'file_storage/call_jfrFJs9OeS0y86we5Akc0AHE.json'}

exec(code, env_args)
