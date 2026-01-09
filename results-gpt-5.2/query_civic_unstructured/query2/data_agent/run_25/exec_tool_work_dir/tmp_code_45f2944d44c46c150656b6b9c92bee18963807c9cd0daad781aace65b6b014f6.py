code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_YtsNFBoCr6P16Gs6Q2UlssJl
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract projects with status completed and completion year 2022
# Heuristic parser for agenda-style project lists.
completed_2022 = set()

status_re = re.compile(r'\b(completed|complete)\b', re.IGNORECASE)
park_re = re.compile(r'\bpark\b', re.IGNORECASE)

# Lines that look like project headers (not bullet updates/schedule)
def is_project_header(line):
    l=line.strip()
    if not l:
        return False
    if len(l) > 120:
        return False
    # exclude common section headers
    if re.search(r'^(Capital Improvement Projects|Disaster Recovery Projects|Project Schedule|Updates|Discussion|RECOMMENDED ACTION|Subject|Prepared by|Approved by|Date prepared|Meeting date|Page\s+\d+)', l, re.IGNORECASE):
        return False
    # exclude bullets
    if l.startswith(('(cid', '•', '-', '–')):
        return False
    # likely a project name if it has letters and not ending with ':'
    if l.endswith(':'):
        return False
    if not re.search(r'[A-Za-z]', l):
        return False
    return True

for d in docs:
    text = d.get('text','')
    if '2022' not in text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        if not is_project_header(line):
            continue
        # window of following lines to find completion indicators and year
        window = '\n'.join(lines[i:i+12])
        if '2022' not in window:
            continue
        if not status_re.search(window):
            continue
        # must indicate completion in 2022 (e.g., completed Nov 2022)
        if not re.search(r'(completed|complete\s+construction)\b[^\n]{0,80}2022', window, re.IGNORECASE):
            continue
        # park-related: project header or window contains 'park'
        if not (park_re.search(line) or park_re.search(window)):
            continue
        completed_2022.add(line)

# Load funding totals per project
path_funding = var_call_l3We3iHxmlG92pJP4GDyTDRU
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

matched = fund_df[fund_df['Project_Name'].isin(completed_2022)]

result = {
    'park_completed_2022_projects': sorted(list(completed_2022)),
    'matched_projects_in_funding': matched[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records'),
    'total_funding': int(matched['total_amount'].sum())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_1koA4201hQvtHR1nFhidbeAc': ['Funding'], 'var_call_5DwqmCtTEQDSa8lx0hDRAv0A': ['civic_docs'], 'var_call_YtsNFBoCr6P16Gs6Q2UlssJl': 'file_storage/call_YtsNFBoCr6P16Gs6Q2UlssJl.json', 'var_call_l3We3iHxmlG92pJP4GDyTDRU': 'file_storage/call_l3We3iHxmlG92pJP4GDyTDRU.json'}

exec(code, env_args)
