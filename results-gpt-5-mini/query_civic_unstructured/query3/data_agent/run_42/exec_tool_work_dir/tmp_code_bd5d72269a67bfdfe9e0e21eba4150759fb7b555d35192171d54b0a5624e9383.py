code = """import json
import re
import pandas as pd

# Load data from storage variables
# var_call_T7kVCxI35Rb96wVLxFptILKp and var_call_Kf6WvGDTE8OWsd75wFh8A3Zf are provided by the tool results

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

funding = load_var(var_call_T7kVCxI35Rb96wVLxFptILKp)
docs = load_var(var_call_Kf6WvGDTE8OWsd75wFh8A3Zf)

funding_df = pd.DataFrame(funding)
# Normalize column types
funding_df['Project_Name'] = funding_df['Project_Name'].astype(str)
funding_df['Funding_Source'] = funding_df['Funding_Source'].astype(str)
# convert Amount to int where possible
funding_df['Amount'] = funding_df['Amount'].apply(lambda x: int(x) if (isinstance(x, (int, float)) or (isinstance(x, str) and x.isdigit())) else int(float(x)) if isinstance(x, str) and re.match(r"^\d+\.?\d*$", x) else None)

# Combine all doc texts into one large text for searching
all_text = "\n\n".join([d.get('text','') for d in docs])
all_text_lower = all_text.lower()

# Find candidate project titles by locating occurrences of 'fema' or 'emergency' and extracting nearby headings
keywords = ['fema', 'emergency']
found_projects = []

for m in re.finditer(rf"({'|'.join(keywords)})", all_text, flags=re.IGNORECASE):
    idx = m.start()
    window_start = max(0, idx - 500)
    window = all_text[window_start: idx+500]
    # try to find a heading before the match: look for double newline and take following line
    parts = window.split('\n\n')
    if len(parts) >= 1:
        candidate = parts[-1].strip()
        # candidate may include '(cid' markers; take first line
        candidate_line = candidate.split('\n')[0].strip()
        # filter out non-title lines
        if candidate_line and len(candidate_line) > 3 and not candidate_line.lower().startswith('agenda') and not candidate_line.lower().startswith('page'):
            found_projects.append((candidate_line, m.group(0)))

# Also add direct known project mentions that are likely emergency-related
# Search for 'Outdoor Warning Sirens' and 'Outdoor Warning Signs' explicitly
explicit_projects = ['Outdoor Warning Sirens', 'Outdoor Warning Signs', 'Outdoor Warningn Sirens - Design']
for ep in explicit_projects:
    if ep.lower() in all_text_lower:
        found_projects.append((ep, 'emergency'))

# Deduplicate project titles
project_titles = []
for title, kw in found_projects:
    t = re.sub(r"\s+", " ", title).strip()
    if t not in project_titles:
        project_titles.append(t)

# Helper to extract status near a position of interest
status_map = {
    'design': ['complete design', 'preliminary design', 'design phase', 'final design', 'design is', 'design plans', 'design services'],
    'completed': ['construction was completed', 'complete construction', 'notice of completion', 'completed'],
    'not started': ['not started', 'identified', 'awaiting', 'awaiting final', 'awaiting final fema', 'awaiting final fema/']
}

def infer_status_near(text, idx):
    snippet = text[max(0, idx-300): idx+300].lower()
    for status, kwlist in status_map.items():
        for kw in kwlist:
            if kw in snippet:
                return status
    # fallback checks
    if 'under construction' in snippet or 'begin construction' in snippet or 'begin construction' in snippet:
        return 'in construction'
    return None

# Build results by matching project titles to funding records
results = []

# First, include funding records whose Project_Name contains 'fema' or whose Project_Name matches extracted titles
for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    if 'fema' in pname.lower() or any(pname.lower().find(pt.lower()) != -1 for pt in project_titles):
        # try to infer status by searching civic docs for the project name
        status = None
        # try direct find
        idx = all_text_lower.find(pname.lower())
        if idx != -1:
            status = infer_status_near(all_text, idx)
        else:
            # try base name without parenthesis suffix
            base = re.sub(r"\s*\(.*?\)\s*", "", pname).strip()
            idx2 = all_text_lower.find(base.lower())
            if idx2 != -1:
                status = infer_status_near(all_text, idx2)
        results.append({
            'Project_Name': pname,
            'Funding_Source': row['Funding_Source'],
            'Amount': int(row['Amount']) if row['Amount'] is not None else None,
            'Status': status
        })

# Next, include any extracted project titles that didn't match funding but might be emergency-related (try to find funding by partial match)
for pt in project_titles:
    # check if already included via funding match
    matched = any(pt.lower() in (r['Project_Name'].lower()) or r['Project_Name'].lower() in pt.lower() for r in results)
    if matched:
        continue
    # try to find funding records with high overlap
    candidates = []
    pt_words = set(re.findall(r"\w+", pt.lower()))
    for _, row in funding_df.iterrows():
        fn_words = set(re.findall(r"\w+", row['Project_Name'].lower()))
        if len(pt_words & fn_words) >= 2:
            candidates.append(row)
    if candidates:
        for row in candidates:
            idx = all_text_lower.find(row['Project_Name'].lower())
            status = None
            if idx != -1:
                status = infer_status_near(all_text, idx)
            else:
                # try using pt location
                idx2 = all_text_lower.find(pt.lower())
                if idx2 != -1:
                    status = infer_status_near(all_text, idx2)
            results.append({
                'Project_Name': row['Project_Name'],
                'Funding_Source': row['Funding_Source'],
                'Amount': int(row['Amount']) if row['Amount'] is not None else None,
                'Status': status
            })
    else:
        # no funding found; skip since user asked for funding sources and amounts
        pass

# Deduplicate results by Project_Name (keep first occurrence)
seen = set()
unique_results = []
for r in results:
    key = r['Project_Name']
    if key not in seen:
        seen.add(key)
        # if status is None, set to 'unknown'
        if r['Status'] is None:
            r['Status'] = 'unknown'
        unique_results.append(r)

# Sort results by Project_Name
unique_results = sorted(unique_results, key=lambda x: x['Project_Name'].lower())

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_T7kVCxI35Rb96wVLxFptILKp': 'file_storage/call_T7kVCxI35Rb96wVLxFptILKp.json', 'var_call_Kf6WvGDTE8OWsd75wFh8A3Zf': 'file_storage/call_Kf6WvGDTE8OWsd75wFh8A3Zf.json'}

exec(code, env_args)
