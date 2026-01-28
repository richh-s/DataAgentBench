code = """import json
import pandas as pd
import re

# Load storage variables (file paths or lists)
from pathlib import Path

# var_call_RYDoXwHwQP3C6w3KWpeJg1hA and var_call_SDrwtL7qxx6JOB3NWS3moZfR are provided by the system

# Determine if variables are file paths (strings) or in-memory lists

def load_var(var):
    if isinstance(var, str) and Path(var).exists():
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

civic_docs = load_var(var_call_RYDoXwHwQP3C6w3KWpeJg1hA)
funding = load_var(var_call_SDrwtL7qxx6JOB3NWS3moZfR)

funding_df = pd.DataFrame(funding)

# Normalize funding fields
funding_df['Project_Name_norm'] = funding_df['Project_Name'].str.replace(r"\(.*?\)", "", regex=True).str.strip().str.lower()

# Helper to extract candidate project names and statuses from civic docs
project_entries = []

keywords = re.compile(r"\b(emergency|fema)\b", re.IGNORECASE)

status_map = {
    'design': re.compile(r"design|preliminary design|complete design", re.IGNORECASE),
    'completed': re.compile(r"construction was completed|complete construction|completed|notice of completion|complete construction:|complete construction", re.IGNORECASE),
    'not started': re.compile(r"not started|identified|waiting|awaiting|will be|to be discussed|scheduled for|pending", re.IGNORECASE)
}

# Candidate project name patterns
proj_name_pattern = re.compile(r"^([A-Z][A-Za-z0-9 '&,-]+?(?:Project|Repairs|Improvements|Repair|Replacement|Sirens|Warning|Bridge|Culvert|Drain|Road|Roadway|Resurfacing|Storm Drain|Water Treatment|Walkway|Playground|Traffic Study|Shade Structure))\b", re.MULTILINE)

for doc in civic_docs:
    text = doc.get('text','')
    if not keywords.search(text):
        continue
    # Split into paragraphs
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for i, p in enumerate(paras):
        if keywords.search(p):
            # Try to find project name in this paragraph
            name_match = proj_name_pattern.search(p)
            pname = None
            if name_match:
                pname = name_match.group(1).strip()
            else:
                # Look backwards up to 3 paragraphs for a title-like paragraph
                for j in range(max(0,i-3), i+1)[::-1]:
                    m = proj_name_pattern.search(paras[j])
                    if m:
                        pname = m.group(1).strip()
                        break
            if not pname:
                # As fallback, extract capitalized line within paragraph
                lines = p.splitlines()
                for ln in lines:
                    if len(ln.split())<=8 and re.search(r"[A-Z]", ln):
                        pname = ln.strip()
                        break
            # Determine status from nearby paragraphs (current paragraph and next two)
            status = 'unknown'
            window = ' '.join(paras[max(0,i-2):min(len(paras), i+3)])
            for st_key, pattern in status_map.items():
                if pattern.search(window):
                    status = st_key
                    break
            if pname:
                project_entries.append({'Project_Name': pname, 'Status': status, 'Source_File': doc.get('filename')})

# Deduplicate project entries by normalized name
for entry in project_entries:
    entry['Project_Name_norm'] = re.sub(r"\(.*?\)", "", entry['Project_Name']).strip().lower()

proj_df = pd.DataFrame(project_entries).drop_duplicates(subset=['Project_Name_norm'])

# Now match with funding entries. We will include funding records where funding project name normalized contains the project norm or vice versa, or funding project name contains 'fema'.
results = []
seen = set()

for idx, prow in proj_df.iterrows():
    pnorm = prow['Project_Name_norm']
    # find funding matches
    matches = funding_df[funding_df['Project_Name_norm'].str.contains(re.escape(pnorm), na=False) | funding_df['Project_Name'].str.contains(r'(?i)fema')]
    # also attempt substring matching the other way
    if matches.empty:
        matches = funding_df[funding_df['Project_Name_norm'].str.contains(pnorm.split()[0], na=False)]
    if matches.empty:
        # add a record with no funding found
        key = (prow['Project_Name'], None, None)
        if key not in seen:
            results.append({'Project_Name': prow['Project_Name'], 'Funding_Source': None, 'Amount': None, 'Status': prow['Status']})
            seen.add(key)
    else:
        for _, frow in matches.iterrows():
            key = (prow['Project_Name'], frow['Funding_Source'], frow['Amount'])
            if key in seen:
                continue
            results.append({'Project_Name': frow['Project_Name'], 'Funding_Source': frow['Funding_Source'], 'Amount': int(frow['Amount']) if frow['Amount'] not in (None, '') else None, 'Status': prow['Status']})
            seen.add(key)

# Additionally include funding entries that explicitly reference FEMA even if not captured from civic docs
fema_funding = funding_df[funding_df['Project_Name'].str.contains(r'(?i)fema')]
for _, frow in fema_funding.iterrows():
    key = (frow['Project_Name'], frow['Funding_Source'], int(frow['Amount']))
    # Check if already in results
    already = any(r['Project_Name']==frow['Project_Name'] and r['Funding_Source']==frow['Funding_Source'] for r in results)
    if not already:
        # Try to find status by matching normalized name to proj_df
        norm = frow['Project_Name_norm']
        status = 'unknown'
        match = proj_df[proj_df['Project_Name_norm'].str.contains(norm) | norm.contains if False else proj_df['Project_Name_norm'].str.contains(norm.split()[0], na=False)]
        # simpler: try to match on first two words
        first_two = ' '.join(norm.split()[:2])
        m = proj_df[proj_df['Project_Name_norm'].str.contains(re.escape(first_two), na=False)]
        if not m.empty:
            status = m.iloc[0]['Status']
        results.append({'Project_Name': frow['Project_Name'], 'Funding_Source': frow['Funding_Source'], 'Amount': int(frow['Amount']) if frow['Amount'] not in (None, '') else None, 'Status': status})

# Final dedupe by Project_Name + Funding_Source
final = []
seen = set()
for r in results:
    key = (r['Project_Name'], r['Funding_Source'])
    if key in seen:
        continue
    final.append(r)
    seen.add(key)

# Sort by Project_Name
final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

import json
print('__RESULT__:')
print(json.dumps(final_sorted))"""

env_args = {'var_call_RYDoXwHwQP3C6w3KWpeJg1hA': 'file_storage/call_RYDoXwHwQP3C6w3KWpeJg1hA.json', 'var_call_SDrwtL7qxx6JOB3NWS3moZfR': 'file_storage/call_SDrwtL7qxx6JOB3NWS3moZfR.json'}

exec(code, env_args)
