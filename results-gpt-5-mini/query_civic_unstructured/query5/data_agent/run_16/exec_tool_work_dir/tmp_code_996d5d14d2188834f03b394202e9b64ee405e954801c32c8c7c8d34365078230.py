code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_zOxJAXyiUvuRoRPWatEiq5lx, 'r') as f:
    funding = json.load(f)
with open(var_call_0GxLFGimWWtyZ5EaoIHD7wLd, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and project names
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except Exception:
        a = re.sub(r"[^0-9]", "", str(r.get('Amount', '0')))
        r['Amount'] = int(a) if a else 0
    r['Project_Name_norm'] = r.get('Project_Name', '').lower()

# Combine civic docs text into one lowercase string
texts = []
for d in civic_docs:
    texts.append(d.get('text', '').lower())
full_text = '\n'.join(texts)

# Helper to find occurrences and check nearby content for '2022' and disaster keywords
def check_project_in_docs(name_norm, text, window=400):
    occurrences = [m.start() for m in re.finditer(re.escape(name_norm), text)]
    if not occurrences:
        return False, False, False
    found = True
    found_2022 = False
    found_disaster_kw = False
    disaster_kw_list = ['fema', 'caloes', 'caljpia', 'woolsey', 'disaster', 'fire', 'emergency', 'federal assistance']
    for pos in occurrences:
        start = max(0, pos - window)
        end = min(len(text), pos + window)
        snippet = text[start:end]
        if '2022' in snippet:
            found_2022 = True
        if any(k in snippet for k in disaster_kw_list):
            found_disaster_kw = True
        if found_2022 and found_disaster_kw:
            break
    return found, found_2022, found_disaster_kw

selected = []
for r in funding:
    name_norm = r['Project_Name_norm']
    # Check if name itself suggests disaster
    name_suggests_disaster = any(k in name_norm for k in ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'emergency'])
    appears, has_2022, disaster_near = check_project_in_docs(name_norm, full_text)
    # If name contains '2022', treat as started in 2022
    if '2022' in name_norm:
        has_2022 = True
    is_disaster = name_suggests_disaster or disaster_near
    if is_disaster and has_2022:
        selected.append(r)

total = sum(r['Amount'] for r in selected)

out = {
    'total_funding': total,
    'count_projects': len(selected),
    'projects': [{'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in selected]
}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_zOxJAXyiUvuRoRPWatEiq5lx': 'file_storage/call_zOxJAXyiUvuRoRPWatEiq5lx.json', 'var_call_0GxLFGimWWtyZ5EaoIHD7wLd': 'file_storage/call_0GxLFGimWWtyZ5EaoIHD7wLd.json'}

exec(code, env_args)
