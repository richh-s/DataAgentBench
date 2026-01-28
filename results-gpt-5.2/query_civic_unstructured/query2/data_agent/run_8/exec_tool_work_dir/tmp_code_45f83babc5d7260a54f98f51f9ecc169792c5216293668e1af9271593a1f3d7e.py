code = """import json, re, pandas as pd

# load mongo docs
mongo_path = var_call_U1uywrQCDDYMENcY6WTiiEB8
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# load funding rows
funding_path = var_call_JlYa1nV6qjPm3RbXQiAVSwd8
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype('int64')

# Build index for quick lookup if project appears in text
proj_names = fund_df['Project_Name'].dropna().unique().tolist()
# precompile regex for park-related (topic detection): require word park in project context.
park_word_re = re.compile(r'\bpark\b', re.IGNORECASE)
# completion in 2022 detection
completed_2022_re = re.compile(r'\bcompleted\b[^\n\r]{0,120}?\b2022\b|\bConstruction was completed\b[^\n\r]{0,120}?\b2022\b|\bComplete(?:d)?\s+Construction\b[^\n\r]{0,120}?\b2022\b|\bConstruction\s+was\s+completed\b[^\n\r]{0,120}?\b2022\b', re.IGNORECASE)

# collect candidate completed-in-2022 park projects by scanning for each project name occurrences.
completed_park_projects = set()

# For efficiency, only scan docs that contain '2022' and 'completed'
for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text or ('completed' not in text.lower() and 'Construction was completed' not in text):
        continue
    # only if park word exists in doc
    if not park_word_re.search(text):
        continue
    # find sentences/lines around completions and check for project names nearby
    # We'll split into lines for locality.
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if '2022' not in line and 'completed' not in line.lower() and 'Construction was completed' not in line:
            continue
        window = '\n'.join(lines[max(0,i-2):min(len(lines), i+3)])
        if not (park_word_re.search(window) and completed_2022_re.search(window)):
            continue
        # check which funded project names appear in this window
        wlow = window.lower()
        for pn in proj_names:
            plow = str(pn).lower()
            if plow and plow in wlow:
                # ensure project itself is park-related: contains 'park' in name OR window indicates park
                if 'park' in plow or park_word_re.search(window):
                    completed_park_projects.add(pn)

# Additionally, some docs may list projects and then have completion line separate (e.g., "Bluffs Park Shade Structure" then "Construction was completed November 2022")
# We'll capture patterns: a line with project name containing Park, followed by within next 3 lines a completion in 2022.
for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not park_word_re.search(line):
            continue
        # match any project name that appears in this line
        line_low = line.lower()
        matched = [pn for pn in proj_names if str(pn).lower() in line_low]
        if not matched:
            continue
        window = '\n'.join(lines[i:min(len(lines), i+4)])
        if completed_2022_re.search(window):
            for pn in matched:
                completed_park_projects.add(pn)

# Sum funding amounts for these projects
sel = fund_df[fund_df['Project_Name'].isin(completed_park_projects)].copy()

total = int(sel['Amount'].sum())

out = {
    'total_funding_completed_park_projects_2022': total,
    'projects': sel.groupby('Project_Name', as_index=False)['Amount'].sum().sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_U1uywrQCDDYMENcY6WTiiEB8': 'file_storage/call_U1uywrQCDDYMENcY6WTiiEB8.json', 'var_call_JlYa1nV6qjPm3RbXQiAVSwd8': 'file_storage/call_JlYa1nV6qjPm3RbXQiAVSwd8.json'}

exec(code, env_args)
