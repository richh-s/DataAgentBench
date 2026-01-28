code = """import json
import re
import pandas as pd

# Load the query results from storage variables (file paths)
with open(var_call_E6MvchDfScozHZ9VKvnN9Q7n, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_5415WbJmoV56RgxwmCEHNEAJ, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Function to normalize project names for matching
def normalize(name):
    if name is None:
        return ''
    # remove parentheses and their contents
    name = re.sub(r"\([^)]*\)", "", name)
    # lowercase
    name = name.lower()
    # replace ampersand with and
    name = name.replace('&', ' and ')
    # remove non-alphanumeric characters except spaces
    name = re.sub(r'[^a-z0-9 ]+', ' ', name)
    # collapse spaces
    name = re.sub(r'\s+', ' ', name).strip()
    return name

# Extract capital projects in Design status from civic_docs texts
design_projects = set()
pattern_start = re.compile(r'capital improvement projects\s*\(design\)', re.IGNORECASE)
end_markers = [r'capital improvement projects\s*\(construction\)',
               r'capital improvement projects\s*\(not started\)',
               r'capital improvement projects\s*\(construction\)',
               r'capital improvement projects\s*\(construction\)',
               r'capital improvement projects\s*\(construction\)',
               r'capital improvement projects\s*\(construction\)']
# also stop at headings like 'Capital Improvement Projects (Construction)' or 'Capital Improvement Projects (Not Started)'
end_markers_regex = re.compile(r'capital improvement projects\s*\((construction|not started)\)', re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text', '')
    m = pattern_start.search(text)
    if not m:
        continue
    start = m.end()
    # search for next end marker after start
    m2 = end_markers_regex.search(text, pos=start)
    end = m2.start() if m2 else len(text)
    segment = text[start:end]
    # split lines and extract candidate project title lines
    for line in segment.splitlines():
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        # skip lines that are clearly not titles
        skip_terms = ['updates', 'project schedule', 'project description', 'page', 'agenda', 'item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', 'complete design', 'advertise', 'begin construction', 'estimated schedule', 'updates:']
        if any(term in low for term in skip_terms):
            continue
        if low.startswith('(cid') or low.startswith('('):
            continue
        if ':' in line:
            # lines with colon likely headings or labels, skip
            continue
        # filter out short lines
        if len(line) < 5:
            continue
        # filter out lines that look like 'Page 1 of 6' etc
        if re.search(r'page \d+ of', low):
            continue
        # Some lines might be part of paragraphs; heuristics: if line ends with 'Project' or contains common keywords, accept
        # Accept if contains words like 'road', 'park', 'project', 'drain', 'walkway', 'median', 'repair', 'improvements', 'skate', 'traffic', 'center', 'storm', 'walkway', 'playground', 'civic', 'bluffs', 'paver'
        keywords = ['road', 'park', 'project', 'drain', 'walkway', 'median', 'repair', 'improvements', 'skate', 'traffic', 'center', 'storm', 'walkway', 'playground', 'civic', 'bluffs', 'paver', 'speed humps', 'retaining wall', 'biofilter', 'treatment']
        if any(k in low for k in keywords) or low[0].isdigit():
            design_projects.add(line)
        else:
            # also accept lines that have Title Case style (a mix of uppercase first letters)
            # simple heuristic: count uppercase letters
            upper_count = sum(1 for ch in line if ch.isupper())
            if upper_count >= 2:
                design_projects.add(line)

# Normalize design project names
norm_design = {normalize(p): p for p in design_projects}

# Load funding records into DataFrame
fund_df = pd.DataFrame(funding_records)
# Ensure Amount numeric
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')
# Only records with Amount > 50000 (our earlier query already filtered), but keep just in case
fund_df = fund_df[fund_df['Amount'] > 50000]
# Build normalized name mapping for funding
fund_df['norm_name'] = fund_df['Project_Name'].fillna('').apply(normalize)
fund_norm_set = set(fund_df['norm_name'].unique())

# Find intersection
matched = []
for norm, orig in norm_design.items():
    if norm in fund_norm_set:
        # get funding amounts for this normalized name (could be multiple records)
        rows = fund_df[fund_df['norm_name'] == norm]
        # sum or keep as list
        amounts = rows['Amount'].tolist()
        matched.append({'project_name': orig, 'normalized': norm, 'funding_amounts': amounts})

# Count unique capital projects in design with funding > 50k
count = len(matched)
projects_list = [m['project_name'] for m in matched]

output = {'count': count, 'projects': projects_list}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_5415WbJmoV56RgxwmCEHNEAJ': 'file_storage/call_5415WbJmoV56RgxwmCEHNEAJ.json', 'var_call_E6MvchDfScozHZ9VKvnN9Q7n': 'file_storage/call_E6MvchDfScozHZ9VKvnN9Q7n.json'}

exec(code, env_args)
