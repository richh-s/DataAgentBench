code = """import json, re

# Load data
with open(var_call_3V3LBuTrnTf5FD8CAnAfAlHL, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_NT3Q3dsTFn3mJHGGbLBIEHZH, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = 0

# Combine civic texts
all_text = '\n'.join(doc.get('text', '') for doc in civic_docs)
all_text_low = all_text.lower()

# Keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'caloja', 'federal assistance', 'disaster', 'recovery', 'fire', 'woolsey', 'emergency']
start_keywords = ['begin construction', 'begin:', 'advertise', 'start', 'started', 'construction was', 'complete construction', 'begin']

matched = {}

for rec in funding:
    proj = rec.get('Project_Name', '')
    proj_low = proj.lower()
    # determine if project is disaster-related by name
    is_disaster_by_name = any(kw in proj_low for kw in disaster_keywords)
    # form base name without parenthetical suffix
    base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()
    variants = [proj_low]
    if base and base != proj_low:
        variants.append(base)

    found = False
    # search for occurrences in civic docs
    for name_variant in variants:
        if not name_variant:
            continue
        start_pos = 0
        while True:
            idx = all_text_low.find(name_variant, start_pos)
            if idx == -1:
                break
            ctx_start = max(0, idx - 200)
            ctx_end = min(len(all_text_low), idx + len(name_variant) + 200)
            context = all_text_low[ctx_start:ctx_end]
            # check for 2022 and start keywords
            if '2022' in context and any(kw in context for kw in start_keywords):
                # consider disaster-related if either name indicates disaster or context contains disaster keywords
                if is_disaster_by_name or any(kw in context for kw in disaster_keywords):
                    matched[rec['Project_Name']] = rec
                    found = True
                    break
                else:
                    # fallback: if name indicates disaster, still include
                    if is_disaster_by_name:
                        matched[rec['Project_Name']] = rec
                        found = True
                        break
            start_pos = idx + 1
        if found:
            break

# Additional fallback: include any project whose name contains disaster keyword and appears anywhere in docs near '2022'
for rec in funding:
    if rec['Project_Name'] in matched:
        continue
    proj = rec.get('Project_Name', '')
    proj_low = proj.lower()
    if any(kw in proj_low for kw in ['fema', 'caloes', 'caljpia', 'caloja']):
        base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()
        if base:
            idx = all_text_low.find(base)
            if idx != -1:
                ctx_start = max(0, idx - 200)
                ctx_end = min(len(all_text_low), idx + len(base) + 200)
                context = all_text_low[ctx_start:ctx_end]
                if '2022' in context:
                    matched[rec['Project_Name']] = rec

matched_list = list(matched.values())

total = sum(r['Amount'] for r in matched_list)

output = {
    'total_funding': total,
    'matched_projects': [{ 'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in matched_list]
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ewZx9GEvkYHuhFSdepF0EpJu': ['civic_docs'], 'var_call_P0nG1k5Ak7Vdxl9PloiZ7Cjc': ['Funding'], 'var_call_3V3LBuTrnTf5FD8CAnAfAlHL': 'file_storage/call_3V3LBuTrnTf5FD8CAnAfAlHL.json', 'var_call_NT3Q3dsTFn3mJHGGbLBIEHZH': 'file_storage/call_NT3Q3dsTFn3mJHGGbLBIEHZH.json', 'var_call_4Yfs9I5iEcW8QJz9OXfc3Bde': 500}

exec(code, env_args)
