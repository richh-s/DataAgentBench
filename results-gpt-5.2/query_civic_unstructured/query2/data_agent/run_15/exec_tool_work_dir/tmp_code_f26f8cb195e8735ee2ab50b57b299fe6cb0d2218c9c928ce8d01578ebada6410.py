code = """import json, re
import pandas as pd

path_docs = var_call_YtD90rUj03rayH0hWzM7kgCV
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
current_section = None
current_status = None
current_project = None

section_status_map = {
    'capital improvement projects (design)': 'design',
    'capital improvement projects (construction)': 'construction',
    'capital improvement projects (not started)': 'not started',
    'disaster recovery projects (design)': 'design',
    'disaster recovery projects (construction)': 'construction',
    'disaster recovery projects (not started)': 'not started',
}

def flush():
    global current_project
    if current_project is not None:
        projects.append(current_project)
        current_project = None

ignore_prefixes = ['(cid', 'page ', 'agenda item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion']
ignore_line_starts = ['updates', 'project schedule', 'estimated schedule', 'project description']

for d in docs:
    lines = [ln.strip() for ln in d.get('text','').splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = re.sub(r'\s+', ' ', ln).strip().lower()
        if low in section_status_map:
            flush()
            current_section = low
            current_status = section_status_map[low]
            continue
        if any(low.startswith(p) for p in ignore_prefixes):
            continue
        if any(low.startswith(s) for s in ignore_line_starts):
            continue
        if current_section:
            # skip obvious schedule rows
            if re.match(r'^(complete design|advertise|begin construction|complete construction|final design|preliminary design|city will be issuing|project is delayed)', low):
                # but if it's complete construction, capture it
                if current_project is not None and low.startswith('complete construction'):
                    m2 = re.search(r'complete construction\s*:\s*(.+)$', ln, flags=re.I)
                    if m2:
                        current_project['complete_construction'] = m2.group(1).strip()
                continue
            # start of project title: a line with no colon and not too long
            if ':' not in ln and len(ln) <= 120 and not low.endswith('.'):
                # new project
                if current_project is None or ln != current_project.get('Project_Name'):
                    flush()
                    current_project = {
                        'Project_Name': ln.strip(),
                        'status_block': current_status,
                        'section': current_section,
                        'source_file': d.get('filename')
                    }
                continue
        # completion text capture within project
        if current_project is not None:
            m = re.search(r'construction was completed\s*(?:,|in)?\s*([A-Za-z]+\s*\d{4})', ln, flags=re.I)
            if m:
                current_project['completed_text'] = m.group(1)

flush()

park_keywords = ['park', 'playground', 'bluffs']

def is_park(name):
    n = (name or '').lower()
    return any(k in n for k in park_keywords)

def completed_in_2022(p):
    for k in ['completed_text', 'complete_construction']:
        v = p.get(k)
        if v and '2022' in str(v):
            return True
    return False

park_completed_names = sorted({p['Project_Name'] for p in projects if is_park(p.get('Project_Name')) and completed_in_2022(p)})

path_fund = var_call_7rv7dzdnvLIhF51JyL0Jqu7x
with open(path_fund,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

res = fund_df[fund_df['Project_Name'].isin(park_completed_names)].copy()

total = int(res['Total_Amount'].sum())

out = {
    'total_funding': total,
    'project_count': int(res.shape[0]),
    'projects': res.sort_values('Project_Name').to_dict(orient='records'),
    'matched_project_names': park_completed_names
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YtD90rUj03rayH0hWzM7kgCV': 'file_storage/call_YtD90rUj03rayH0hWzM7kgCV.json', 'var_call_7rv7dzdnvLIhF51JyL0Jqu7x': 'file_storage/call_7rv7dzdnvLIhF51JyL0Jqu7x.json'}

exec(code, env_args)
