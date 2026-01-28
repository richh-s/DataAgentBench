code = """import json
import re
import pandas as pd

# Load data from storage file paths
civic_docs_path = var_call_K6CNq9QRscQHMxQogdGNgSjC
funding_path = var_call_J36FWzODqpQAuBfxtFUh4H7K

with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding table into DataFrame and ensure Amount is int
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df['Project_Name_norm'] = fund_df['Project_Name'].str.lower()

# Function to extract design projects from a document text
def extract_design_projects(text):
    projects = []
    # Find the Capital Improvement Projects (Design) section
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|$)', text, flags=re.IGNORECASE|re.DOTALL)
    if not m:
        return projects
    block = m.group(1)
    # Split into lines and pick likely project title lines
    lines = [ln.strip() for ln in block.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        low = ln.lower()
        # Skip lines that are clearly not project titles
        if low.startswith('(cid:') or low.startswith('updates') or low.startswith('project schedule') or 'page' in low or low.startswith('agenda') or low.startswith('item') or low.startswith('subject'):
            continue
        # Skip short lines
        if len(ln) < 6:
            continue
        # Also skip lines that end with a colon or start with 'complete design' etc
        if ln.endswith(':'):
            continue
        if re.match(r'complete design', low) or re.match(r'advertise', low) or re.match(r'begin construction', low):
            continue
        projects.append(ln)
    return projects

# Extract projects from all documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    extracted = extract_design_projects(text)
    design_projects.extend(extracted)

# Deduplicate and normalize
design_projects_unique = []
seen = set()
for p in design_projects:
    pn = re.sub(r'\s+', ' ', p).strip()
    if pn.lower() not in seen:
        seen.add(pn.lower())
        design_projects_unique.append(pn)

# Now match with funding records with Amount > 50000 using substring matching
matched_projects = []
for proj in design_projects_unique:
    proj_low = proj.lower()
    # find funding records where proj is substring of funding name or vice versa
    contains_mask = fund_df['Project_Name_norm'].str.contains(re.escape(proj_low))
    reverse_mask = fund_df['Project_Name_norm'].apply(lambda x: x in proj_low)
    matches = fund_df[contains_mask | reverse_mask]
    # Now filter by amount > 50000
    matches = matches[matches['Amount'] > 50000]
    if not matches.empty:
        matched_info = []
        for _, row in matches.iterrows():
            matched_info.append({'Funding_ID': int(row['Funding_ID']), 'Funding_Project_Name': row['Project_Name'], 'Amount': int(row['Amount'])})
        matched_projects.append({'Project_Name_extracted': proj, 'Matched_Funding': matched_info})

count = len(matched_projects)
# Prepare output
output = {'count': count, 'projects': matched_projects}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_5fTbmfsk3nQHmy04JGuQZ5UO': ['civic_docs'], 'var_call_rdo9RJzUgq0DrgZEIA64V37n': ['Funding'], 'var_call_K6CNq9QRscQHMxQogdGNgSjC': 'file_storage/call_K6CNq9QRscQHMxQogdGNgSjC.json', 'var_call_J36FWzODqpQAuBfxtFUh4H7K': 'file_storage/call_J36FWzODqpQAuBfxtFUh4H7K.json'}

exec(code, env_args)
