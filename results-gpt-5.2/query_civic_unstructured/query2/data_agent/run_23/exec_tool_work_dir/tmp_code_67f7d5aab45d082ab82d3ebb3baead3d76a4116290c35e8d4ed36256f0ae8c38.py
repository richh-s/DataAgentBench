code = """import json, re
import pandas as pd

# load funding totals
fp = var_call_s2zxLpt2M81xgHj3iD5tzsh9
with open(fp, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load docs
dp = var_call_Eai1gFyqM6dFXNoszLVPh4Kg
with open(dp, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# parse projects: find headings and their following Updates line containing completed and 2022
# We'll capture project blocks by finding lines that look like project names (not bullet/header)
completed_2022_projects = set()

# common non-project headings to skip
skip_prefixes = {
    'Public Works', 'Agenda Report', 'Capital Improvement Projects', 'Disaster Recovery Projects',
    'RECOMMENDED ACTION', 'DISCUSSION', 'Project Schedule', 'Estimated Schedule', 'Project Updates',
    'Project Description', 'Updates', 'Page', 'Agenda Item', 'To:', 'Prepared by:', 'Approved by:',
    'Date prepared:', 'Meeting date:', 'Subject:'
}

park_keywords = re.compile(r'\bpark\b', re.IGNORECASE)

def extract_completed_2022(text):
    lines = [ln.strip() for ln in text.splitlines()]
    # keep non-empty lines
    lines = [ln for ln in lines if ln]
    # identify candidate project name lines: those that have letters and not too long and not start with bullets
    cand_idxs = []
    for i, ln in enumerate(lines):
        if ln.startswith(('(cid', '•', '-', '–')):
            continue
        if any(ln.startswith(p) for p in skip_prefixes):
            continue
        # likely project name appears alone and later has 'Updates' lines
        if len(ln) <= 120 and re.search(r'[A-Za-z]', ln):
            # exclude sentences with ':'
            if ':' in ln:
                continue
            # exclude generic words
            if ln.lower() in {'item', 'discussion', 'recommended action'}:
                continue
            cand_idxs.append(i)

    # For each candidate, scan next ~25 lines for completion phrase mentioning 2022
    for idx in cand_idxs:
        name = lines[idx]
        window = ' '.join(lines[idx: idx+30])
        if re.search(r'completed\s+(in|,)?\s*(november|december|january|february|march|april|may|june|july|august|september|october)?\s*2022', window, re.IGNORECASE) or \
           re.search(r'construction\s+was\s+completed\s+[^.]*2022', window, re.IGNORECASE) or \
           re.search(r'completed\s+[^.]*2022', window, re.IGNORECASE):
            if park_keywords.search(name):
                completed_2022_projects.add(name)
            else:
                # also allow if window mentions park and the name doesn't
                if park_keywords.search(window):
                    completed_2022_projects.add(name)

for d in docs:
    extract_completed_2022(d.get('text',''))

# Join with funding
parks_completed_2022 = fund_df[fund_df['Project_Name'].isin(sorted(completed_2022_projects))]

total = int(parks_completed_2022['total_amount'].sum())

out = {
    'total_funding': total,
    'projects': parks_completed_2022.sort_values('Project_Name')[['Project_Name','total_amount']].to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_s2zxLpt2M81xgHj3iD5tzsh9': 'file_storage/call_s2zxLpt2M81xgHj3iD5tzsh9.json', 'var_call_Eai1gFyqM6dFXNoszLVPh4Kg': 'file_storage/call_Eai1gFyqM6dFXNoszLVPh4Kg.json'}

exec(code, env_args)
