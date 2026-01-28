code = """import json, re, pandas as pd

def load_tool_result(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_tool_result(var_call_NQAcQDN6mQpn5H4Syx2xwZEi)
fund = load_tool_result(var_call_neVS3o2h6gHsTJFpcffeuHww)

fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = fund_df['Total_Amount'].astype(int)

# Extract disaster project blocks with explicit Start/Begin in 2022.
# We'll look for patterns like:
# <Project Name>
# ...
# Project Schedule:
# ... Begin ... 2022 ...

disaster_started_2022 = set()

for d in docs:
    text = d.get('text','')
    # Find section after 'Disaster Recovery Projects' if present, else skip
    m = re.search(r'Disaster Recovery Projects', text, re.IGNORECASE)
    if not m:
        continue
    section = text[m.end():]
    # stop at end or next 'Capital Improvement Projects' (if disaster first)
    m2 = re.search(r'Capital Improvement Projects', section, re.IGNORECASE)
    if m2:
        section = section[:m2.start()]
    lines = [ln.rstrip() for ln in section.splitlines()]
    # scan for begin 2022 lines and backtrack to nearest plausible project name above
    for i, ln in enumerate(lines):
        if re.search(r'\b(Begin|Start)\b', ln, re.IGNORECASE) and '2022' in ln:
            # backtrack to find project title: previous non-empty line without colon/bullets
            for j in range(i-1, max(-1, i-30), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if cand.startswith(('(cid', '•', '-', 'Page', 'Agenda')):
                    continue
                if ':' in cand:
                    continue
                if re.search(r'(Updates|Project Schedule|Estimated Schedule|Project Description)', cand, re.IGNORECASE):
                    continue
                disaster_started_2022.add(cand)
                break

matched = fund_df[fund_df['Project_Name'].isin(disaster_started_2022)]
total = int(matched['Total_Amount'].sum())

out = {
    'projects': sorted(disaster_started_2022),
    'matched_funding_projects_count': int(matched.shape[0]),
    'total_funding': total
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0KZba2jifjjARfyhQA7R0oHf': ['Funding'], 'var_call_rVwVClsXWvPM67F278tl1OC2': ['civic_docs'], 'var_call_LlWG397XrqTb1fV6hmjlKIJU': 'file_storage/call_LlWG397XrqTb1fV6hmjlKIJU.json', 'var_call_neVS3o2h6gHsTJFpcffeuHww': 'file_storage/call_neVS3o2h6gHsTJFpcffeuHww.json', 'var_call_3XTdhVxljAvubgkamDgiu0zf': {'disaster_projects_started_2022': [], 'matched_funding_projects_count': 0, 'total_funding': 0}, 'var_call_NQAcQDN6mQpn5H4Syx2xwZEi': 'file_storage/call_NQAcQDN6mQpn5H4Syx2xwZEi.json'}

exec(code, env_args)
