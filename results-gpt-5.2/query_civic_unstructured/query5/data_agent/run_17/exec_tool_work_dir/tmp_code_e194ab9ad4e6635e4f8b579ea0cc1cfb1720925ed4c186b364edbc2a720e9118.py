code = """import json, re, pandas as pd

def load_tool_result(var):
    # var may be list (already loaded) or a file path str
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_tool_result(var_call_LlWG397XrqTb1fV6hmjlKIJU)
fund = load_tool_result(var_call_neVS3o2h6gHsTJFpcffeuHww)

# Identify disaster projects that started in 2022 from text.
# Heuristic: in Disaster Recovery Projects section and line contains 'Project Schedule' with 'Begin' and '2022'
# We'll parse blocks under 'Disaster Recovery Projects' header until next major header.

disaster_2022_projects = set()

for d in docs:
    text = d.get('text','')
    if not re.search(r'Disaster Recovery Projects', text, re.IGNORECASE):
        continue
    # split into lines
    lines = text.splitlines()
    in_disaster = False
    current_project = None
    for ln in lines:
        l = ln.strip()
        if re.search(r'^Disaster Recovery Projects', l, re.IGNORECASE):
            in_disaster = True
            current_project = None
            continue
        if in_disaster and re.search(r'^Capital Improvement Projects', l, re.IGNORECASE):
            in_disaster = False
            current_project = None
            continue
        if not in_disaster:
            continue
        # detect a project title line: non-empty, not bullets, not 'Updates', not 'Project Schedule', no colon.
        if l and not l.startswith(('(cid', '•', '-', 'Page', 'Agenda', 'Recommended', 'DISCUSSION', 'RECOMMENDED')):
            if not re.search(r'(Updates|Project Schedule|Estimated Schedule|Project Description|Complete|Advertise|Begin Construction|Final Design|Preliminary)', l, re.IGNORECASE) and ':' not in l:
                # likely project name
                current_project = l
        # detect begin/start in 2022
        if current_project and re.search(r'(Begin|Start)', l, re.IGNORECASE) and '2022' in l:
            disaster_2022_projects.add(current_project)

# Fallback: include any funding project names with FEMA/CalOES/CalJPIA and started 2022 mentioned anywhere as 'Begin' line near it.
# But keep conservative: only those found above.

# Build funding map
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = fund_df['Total_Amount'].astype(int)

matched = fund_df[fund_df['Project_Name'].isin(sorted(disaster_2022_projects))]

total = int(matched['Total_Amount'].sum())

out = {
    'disaster_projects_started_2022': sorted(disaster_2022_projects),
    'matched_funding_projects_count': int(matched.shape[0]),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0KZba2jifjjARfyhQA7R0oHf': ['Funding'], 'var_call_rVwVClsXWvPM67F278tl1OC2': ['civic_docs'], 'var_call_LlWG397XrqTb1fV6hmjlKIJU': 'file_storage/call_LlWG397XrqTb1fV6hmjlKIJU.json', 'var_call_neVS3o2h6gHsTJFpcffeuHww': 'file_storage/call_neVS3o2h6gHsTJFpcffeuHww.json'}

exec(code, env_args)
