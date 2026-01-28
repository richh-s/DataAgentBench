code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_zOxJAXyiUvuRoRPWatEiq5lx, 'r') as f:
    funding = json.load(f)
with open(var_call_0GxLFGimWWtyZ5EaoIHD7wLd, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and project names
for r in funding:
    # Convert Amount to int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # remove commas etc
        a = re.sub(r"[^0-9]", "", str(r.get('Amount','0')))
        r['Amount'] = int(a) if a else 0
    # Normalize Project_Name
    r['Project_Name_norm'] = r['Project_Name'].lower()

# Build a single large text for civic docs with filename markers
combined_texts = []
for doc in civic_docs:
    text = doc.get('text','')
    combined_texts.append(text)
full_text = "\n".join(combined_texts).lower()

# Helper to check if project name appears in civic docs and if 2022 near occurrence
def appears_with_2022(proj_name_norm, full_text, window=400):
    idx = full_text.find(proj_name_norm)
    if idx == -1:
        return False, False
    # find all occurrences
    occurrences = [m.start() for m in re.finditer(re.escape(proj_name_norm), full_text)]
    found_2022_near = False
    for pos in occurrences:
        start = max(0, pos - window)
        end = min(len(full_text), pos + window)
        snippet = full_text[start:end]
        if '2022' in snippet:
            found_2022_near = True
            break
    return True, found_2022_near

# Keywords indicating disaster-related
disaster_keywords = ['fema', 'caloes', 'caloja', 'caljpia', 'caljpia', 'disaster', 'fire', 'woolsey', 'federal assistance', 'emergency', 'cal o es']
# Also include '(fema' patterns; but we already lowercase

# Evaluate each funding record
selected = []
for r in funding:
    name_norm = r['Project_Name_norm']
    # check disaster by name keywords
    is_disaster_name = any(k in name_norm for k in ['fema', 'caloes', 'caljpia', 'woolsey', 'disaster', 'fire', 'emergency'])
    # check civic docs for project mention and nearby keywords
    appears, has_2022 = appears_with_2022(name_norm, full_text)
    # also search for disaster keywords near project mention
    disaster_near = False
    if appears:
        # find occurrences and check for disaster keywords nearby
        for m in re.finditer(re.escape(name_norm), full_text):
            start = max(0, m.start()-300)
            end = min(len(full_text), m.end()+300)
            snippet = full_text[start:end]
            if any(k in snippet for k in ['fema', 'caloes', 'caljpia', 'woolsey', 'disaster', 'fire', 'emergency']):
                disaster_near = True
                break
    # Determine disaster-related: either name indicates or near text indicates
    is_disaster = is_disaster_name or disaster_near
    # Determine started in 2022: has_2022 near mention OR name contains 2022?
    started_2022 = has_2022
    # As fallback, if project name contains '2022' consider started in 2022
    if '2022' in name_norm:
        started_2022 = True
    if is_disaster and started_2022:
        selected.append(r)

# Compute total funding
total = sum(r['Amount'] for r in selected)

# Prepare output details for transparency
out = {
    'total_funding': total,
    'count_projects': len(selected),
    'projects': [{'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in selected]
}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_zOxJAXyiUvuRoRPWatEiq5lx': 'file_storage/call_zOxJAXyiUvuRoRPWatEiq5lx.json', 'var_call_0GxLFGimWWtyZ5EaoIHD7wLd': 'file_storage/call_0GxLFGimWWtyZ5EaoIHD7wLd.json'}

exec(code, env_args)
