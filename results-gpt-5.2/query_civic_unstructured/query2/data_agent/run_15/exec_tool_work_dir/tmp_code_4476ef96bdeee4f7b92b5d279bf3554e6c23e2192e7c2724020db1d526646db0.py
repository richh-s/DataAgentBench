code = """import json, re
import pandas as pd

# load civic docs
path_docs = var_call_YtD90rUj03rayH0hWzM7kgCV
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# parse projects from docs: rely on headings and bullets as in agendas
projects = []
current_section = None
current_status = None
current_project = None

def flush():
    global current_project
    if current_project is not None:
        projects.append(current_project)
        current_project = None

section_status_map = {
    'capital improvement projects (design)': 'design',
    'capital improvement projects (construction)': 'construction',
    'capital improvement projects (not started)': 'not started',
    'disaster recovery projects (design)': 'design',
    'disaster recovery projects (construction)': 'construction',
    'disaster recovery projects (not started)': 'not started',
}

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = re.sub(r'\s+', ' ', ln).strip().lower()
        if low in section_status_map:
            flush()
            current_section = low
            current_status = section_status_map[low]
            continue
        # project name line: a line with no colon and not a bullet and not generic labels
        if current_section and not any(low.startswith(x) for x in ['(cid', 'page ', 'agenda item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'updates', 'project schedule', 'estimated schedule', 'project description']):
            # ignore schedule rows
            if re.match(r'^(complete design|advertise|begin construction|complete construction|final design|project is delayed|city will be issuing|funding agreement)', low):
                continue
            # treat as possible project title if it's relatively short and title case-ish and not ending with ':'
            if ':' not in ln and len(ln) <= 120 and not low.endswith('.'):
                # if line looks like a schedule item with year etc skip
                if re.match(r'^\d{4}[- ]', ln.strip()):
                    # still can be a project title (e.g., 2022 Morning View...)
                    pass
                # start new project
                if current_project is None or ln != current_project.get('Project_Name'):
                    flush()
                    current_project = {
                        'Project_Name': ln.strip(),
                        'status_block': current_status,
                        'section': current_section,
                        'source_file': d.get('filename')
                    }
                continue
        # capture completion info
        if current_project is not None:
            m = re.search(r'construction was completed\s*(?:,|in)?\s*([A-Za-z]+\s*\d{4}|\w+\s*\d{4}|\w+\s*\d{4})', low)
            if m:
                current_project['completed_text'] = m.group(1)
            m2 = re.search(r'complete construction\s*:\s*([^\n]+)$', low)
            if m2:
                current_project['complete_construction'] = m2.group(1).strip()

flush()

# normalize completed year detection
park_keywords = ['park','playground','bluffs']

def is_park(name):
    n = name.lower()
    return any(k in n for k in park_keywords)


def completed_in_2022(p):
    # consider explicit completion statements containing 2022
    for k in ['completed_text','complete_construction']:
        if k in p and p[k] and '2022' in str(p[k]):
            return True
    # also if project is in construction section and mentions completed November 2022 etc in text captured
    return False

park_completed_2022 = {}
for p in projects:
    if not p.get('Project_Name'):
        continue
    if is_park(p['Project_Name']) and completed_in_2022(p):
        park_completed_2022[p['Project_Name']] = p

# load funding grouped totals
path_fund = var_call_7rv7dzdnvLIhF51JyL0Jqu7x
with open(path_fund,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

# join on exact project name
names = list(park_completed_2022.keys())
res = fund_df[fund_df['Project_Name'].isin(names)]

total = int(res['Total_Amount'].sum())

out = {
    'total_funding': total,
    'projects': res.sort_values('Project_Name').to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YtD90rUj03rayH0hWzM7kgCV': 'file_storage/call_YtD90rUj03rayH0hWzM7kgCV.json', 'var_call_7rv7dzdnvLIhF51JyL0Jqu7x': 'file_storage/call_7rv7dzdnvLIhF51JyL0Jqu7x.json'}

exec(code, env_args)
