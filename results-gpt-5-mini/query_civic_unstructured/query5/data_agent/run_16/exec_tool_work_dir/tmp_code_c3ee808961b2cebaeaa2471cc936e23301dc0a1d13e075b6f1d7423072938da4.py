code = """import json
import re

# Load files from storage-provided keys
with open(var_call_zOxJAXyiUvuRoRPWatEiq5lx, 'r') as f:
    funding = json.load(f)
with open(var_call_0GxLFGimWWtyZ5EaoIHD7wLd, 'r') as f:
    civic_docs = json.load(f)

# Prepare full combined text of civic docs (lowercased)
texts = [d.get('text','').lower() for d in civic_docs]
full_text = '\n'.join(texts)

# Normalize funding records and amounts
for r in funding:
    amt = r.get('Amount', 0)
    try:
        r['Amount'] = int(amt)
    except Exception:
        cleaned = re.sub("[^0-9]", "", str(amt))
        r['Amount'] = int(cleaned) if cleaned else 0
    r['Project_Name_norm'] = r.get('Project_Name','').lower()

# Disaster indicators
disaster_name_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'emergency']

# Helper to find occurrences and nearby keywords
def find_nearby_flags(name_norm, text, window=400):
    if not name_norm:
        return False, False
    positions = [m.start() for m in re.finditer(re.escape(name_norm), text)]
    if not positions:
        return False, False
    found_2022 = False
    found_disaster_kw = False
    for pos in positions:
        start = max(0, pos - window)
        end = min(len(text), pos + window)
        snippet = text[start:end]
        if '2022' in snippet:
            found_2022 = True
        for kw in disaster_name_keywords:
            if kw in snippet:
                found_disaster_kw = True
        if found_2022 and found_disaster_kw:
            break
    return found_2022, found_disaster_kw

selected = []
for r in funding:
    name_norm = r['Project_Name_norm']
    # Name suggests disaster
    name_suggests_disaster = any(kw in name_norm for kw in disaster_name_keywords)
    # If project name contains '2022', treat as started in 2022
    name_contains_2022 = '2022' in name_norm
    appears_2022, disaster_near = find_nearby_flags(name_norm, full_text)
    started_2022 = name_contains_2022 or appears_2022
    is_disaster = name_suggests_disaster or disaster_near
    if is_disaster and started_2022:
        selected.append(r)

total = sum(r['Amount'] for r in selected)

out = {
    'total_funding': total,
    'count_projects': len(selected),
    'projects': [{'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in selected]
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_zOxJAXyiUvuRoRPWatEiq5lx': 'file_storage/call_zOxJAXyiUvuRoRPWatEiq5lx.json', 'var_call_0GxLFGimWWtyZ5EaoIHD7wLd': 'file_storage/call_0GxLFGimWWtyZ5EaoIHD7wLd.json', 'var_call_fWleDfLyPaPnAG17iseqd9Gk': {'test': True}}

exec(code, env_args)
