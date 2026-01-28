code = """import json
import re
from pathlib import Path

# Load data from storage-provided file paths
funding_path = Path(var_call_4wM5k3GTyzdYzrzkX7moL6ZN)
docs_path = Path(var_call_rAaA0qkh81fh2IyO6Se144fH)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]", "", str(r.get('Amount','0')))
        r['Amount'] = int(s) if s else 0

# Build combined civic text
all_texts = [d.get('text','') for d in docs]
combined_text = "\n".join(all_texts)

# Helper to strip parenthetical suffix
def base_name(name):
    return re.sub(r"\s*\([^)]*\)", "", name).strip()

# Keywords for disaster classification and start detection
disaster_keywords = ['fema', 'caloes', 'cal o es', 'calo es', 'caloes', 'disaster', 'fire', 'woolsey', 'emergency']
start_indicators = ['begin construction', 'begin construction:', 'begin construction -', 'begin construction.','begin construction)']
# Also consider 'Construction was started' or 'construction started' or 'start construction'
start_indicators += ['construction started', 'start construction', 'beginning construction']

# We'll search per funding record
matches = []
for r in funding:
    pname = r['Project_Name']
    pname_low = pname.lower()
    bname = base_name(pname).lower()
    found = False
    contexts = []
    # search for exact or base-name occurrences
    for txt in all_texts:
        txt_low = txt.lower()
        idx = txt_low.find(pname_low)
        if idx==-1:
            idx = txt_low.find(bname)
        if idx!=-1:
            found = True
            start = max(0, idx-300)
            end = min(len(txt_low), idx+300)
            contexts.append(txt_low[start:end])
    # classify disaster if project name contains keywords or any context contains
    is_disaster = False
    for kw in disaster_keywords:
        if kw in pname_low:
            is_disaster = True
            break
    if not is_disaster:
        for c in contexts:
            for kw in disaster_keywords:
                if kw in c:
                    is_disaster = True
                    break
            if is_disaster:
                break
    # detect start in 2022: look for start indicators in context with '2022' nearby
    started_2022 = False
    for c in contexts:
        if '2022' in c:
            for si in start_indicators:
                if si in c:
                    started_2022 = True
                    break
        # also consider patterns like 'begin construction: fall 2022' or 'begin construction: summer 2022'
        if re.search(r'begin construction:\s*[^\n]{0,30}2022', c):
            started_2022 = True
        if 'begin construction' in c and '2022' in c:
            started_2022 = True
        if 'advertise:' in c and '2022' in c and 'begin construction' in c:
            started_2022 = True
        if 'begin construction' in c and re.search(r'\b2022\b', c):
            started_2022 = True
        if started_2022:
            break
    # Also handle cases like 'Construction was completed, November 2022' with 'Begin Construction: 2022' absent
    # But we won't count completions as starts.

    if found:
        matches.append({
            'Project_Name': pname,
            'Amount': r['Amount'],
            'is_disaster': is_disaster,
            'started_2022': started_2022,
            'contexts_count': len(contexts)
        })

# Also consider funding entries that weren't found in civic docs but have disaster keywords in name and maybe started in 2022 (hard to determine) -> we'll ignore unknown starts

# Sum amounts for those that are disaster and started_2022
total = sum(m['Amount'] for m in matches if m['is_disaster'] and m['started_2022'])

# For transparency in output, include matched records that met criteria
selected = [m for m in matches if m['is_disaster'] and m['started_2022']]

result = {
    'total_funding_for_disaster_projects_started_in_2022': total,
    'matched_projects': selected
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ppCisfN2tRpTi42dyxTwHA6j': ['civic_docs'], 'var_call_nCM4EklzTtjpxEpVDK5Li7Kx': ['Funding'], 'var_call_4wM5k3GTyzdYzrzkX7moL6ZN': 'file_storage/call_4wM5k3GTyzdYzrzkX7moL6ZN.json', 'var_call_rAaA0qkh81fh2IyO6Se144fH': 'file_storage/call_rAaA0qkh81fh2IyO6Se144fH.json'}

exec(code, env_args)
