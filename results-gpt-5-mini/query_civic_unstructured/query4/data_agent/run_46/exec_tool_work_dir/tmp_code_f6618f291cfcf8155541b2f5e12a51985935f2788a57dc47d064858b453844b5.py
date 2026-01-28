code = """import json
import re
import pandas as pd

# Load previous tool results from storage-file paths
civic_docs = json.load(open(var_call_n4NIMLfycMeggnIQSLDKvXTO, 'r'))
funding = json.load(open(var_call_oB5uWLUzgwEqRsRf6aZsmtF4, 'r'))

funding_df = pd.DataFrame(funding)
# Normalize Amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)
funding_df['Project_Name_norm'] = funding_df['Project_Name'].str.lower()

# Helper to normalize strings
def norm(s):
    if s is None:
        return ''
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical suffixes
    s = re.sub(r"[^0-9a-zA-Z ]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

month_keywords = ['march','april','may']

found_projects = set()

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i,line in enumerate(lines):
        low = line.lower()
        if '2022' in low and ( 'spring' in low or any(m in low for m in month_keywords)):
            # try to find project title above
            for j in range(i-1, max(i-12, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip common headings or metadata lines
                skip_terms = ['updates','project schedule','page','agenda','item','to:','prepared by','approved by','meeting date','date prepared','subject:','recommended action','discussion','agenda item']
                if any(cand.lower().startswith(st) for st in skip_terms):
                    continue
                if ':' in cand and len(cand.split(':')[0].split())<6:
                    # likely a label like "Project Schedule:" skip
                    continue
                # Heuristic: candidate should contain alphabetic chars and be reasonably short
                if re.search('[a-zA-Z]', cand) and len(cand) < 200:
                    # Exclude lines that are clearly part of paragraph (start with (cid or bullet)
                    if cand.startswith('(cid') or cand.startswith('('):
                        continue
                    # Accept this as project title
                    found_projects.add(cand)
                    break

# Normalize found projects and deduplicate similar names
normalized_projects = {}
for p in found_projects:
    normalized_projects[p] = norm(p)

# Build mapping of project -> matched funding rows and amount
projects_info = []
for orig, pn in normalized_projects.items():
    # find funding rows where project name contains pn or pn contains funding name
    matches = funding_df[funding_df['Project_Name_norm'].str.contains(pn, na=False) | funding_df['Project_Name_norm'].str.contains(norm(orig), na=False)]
    # Also try substring both ways
    if matches.empty:
        matches = funding_df[funding_df['Project_Name_norm'].str.contains(pn.split()[0], na=False)] if pn.split() else funding_df.iloc[0:0]
    total_amt = int(matches['Amount'].sum()) if not matches.empty else 0
    matched_names = matches['Project_Name'].tolist()
    projects_info.append({'project_name_extracted': orig, 'normalized': pn, 'matched_funding_count': len(matches), 'matched_funding_projects': matched_names, 'funding_amount': total_amt})

# Filter projects that likely started in Spring 2022: some extracted might actually point to 2023 etc because we looked for '2022' in same line. Ensure that the line that triggered contained '2022' and month keywords; we already required that. So keep all.

# Compute totals
num_projects = len(projects_info)
total_funding = sum(p['funding_amount'] for p in projects_info)

result = {'num_projects': num_projects, 'total_funding': total_funding, 'projects': projects_info}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_n4NIMLfycMeggnIQSLDKvXTO': 'file_storage/call_n4NIMLfycMeggnIQSLDKvXTO.json', 'var_call_oB5uWLUzgwEqRsRf6aZsmtF4': 'file_storage/call_oB5uWLUzgwEqRsRf6aZsmtF4.json'}

exec(code, env_args)
