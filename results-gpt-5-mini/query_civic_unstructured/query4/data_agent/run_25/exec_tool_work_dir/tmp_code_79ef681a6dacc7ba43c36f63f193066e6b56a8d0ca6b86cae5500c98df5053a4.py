code = """import json, re, pandas as pd

# Load data from storage file paths
with open(var_call_5EkoC3UvS1FjrllnHi9gLJ8T, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_HTfzgTR3OFhHNvQYKvOrA1WS, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Helper to find project title above a given line index
ignore_prefixes = ('(cid', 'project schedule', 'updates', 'page', 'agenda', 'item', 'subject', 'recommended', 'discussion')

def is_title_line(s):
    if not s:
        return False
    s_low = s.strip().lower()
    if any(s_low.startswith(p) for p in ignore_prefixes):
        return False
    # Exclude lines that look like dates or short words
    if len(s.strip()) < 4:
        return False
    # Exclude lines that are all uppercase section headers like 'CAPITAL IMPROVEMENT PROJECTS (DESIGN)'
    # but some titles are Title Case; accept most lines with letters and words
    # Exclude lines that contain ':' which are likely labels
    if ':' in s:
        return False
    # Exclude lines that are numeric or single word 'Discussion'
    if re.fullmatch(r'[0-9\-\/\s]+', s.strip()):
        return False
    return True

found_projects = []
for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for idx, line in enumerate(lines):
        low = line.lower()
        # look for lines that mention 'spring' and '2022' and a begin phrase
        if 'spring' in low and '2022' in line:
            # ensure it's a begin line or contains 'Begin' or 'Begin Construction' or 'Begin Design' or 'Begin Final Design' etc
            if re.search(r'begin\b', low) or 'complete design' in low or 'advertise' in low:
                # find title by scanning upward
                title = None
                j = idx-1
                # Skip labels and empty lines, find nearest plausible title
                while j >= 0:
                    candidate = lines[j].strip()
                    if is_title_line(candidate):
                        title = candidate
                        break
                    j -= 1
                if title:
                    # clean common bullets or markers
                    title = re.sub(r'^\W+', '', title).strip()
                    # remove trailing project labels like 'Project' if it's standalone? keep as is
                    found_projects.append(title)

# Deduplicate while preserving order
seen = set()
projects = []
for p in found_projects:
    if p not in seen:
        seen.add(p)
        projects.append(p)

# Load funding into DataFrame
fund_df = pd.DataFrame(funding_records)
if not fund_df.empty:
    # Ensure Amount numeric
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)
else:
    fund_df['Amount'] = pd.Series(dtype=int)

# For each project, attempt exact match on funding.Project_Name; if not found, try contains
project_funding = {}
for p in projects:
    matches = fund_df[fund_df['Project_Name'] == p]
    if matches.empty:
        # try case-insensitive contains
        matches = fund_df[fund_df['Project_Name'].str.lower().str.contains(re.escape(p.lower()))]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    project_funding[p] = total

count = len(projects)
total_funding = sum(project_funding.values())

result = {
    'projects': projects,
    'count': count,
    'total_funding': int(total_funding),
    'project_funding_breakdown': project_funding
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dlBEXN7zcHddCpkdOGuFPBbP': ['civic_docs'], 'var_call_ySoORTaCpVb0E0qkkkjJSyAO': ['Funding'], 'var_call_OfYOHsvJrNcXYRHw4qU3WX3M': 'file_storage/call_OfYOHsvJrNcXYRHw4qU3WX3M.json', 'var_call_5EkoC3UvS1FjrllnHi9gLJ8T': 'file_storage/call_5EkoC3UvS1FjrllnHi9gLJ8T.json', 'var_call_HTfzgTR3OFhHNvQYKvOrA1WS': 'file_storage/call_HTfzgTR3OFhHNvQYKvOrA1WS.json'}

exec(code, env_args)
