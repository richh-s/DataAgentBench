code = """import json

# Load data from storage-provided file paths
with open(var_call_3V3LBuTrnTf5FD8CAnAfAlHL, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_NT3Q3dsTFn3mJHGGbLBIEHZH, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding amounts to int
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = 0

# Combine all civic texts
all_text = "\n".join(doc.get('text', '') for doc in civic_docs)
all_text_low = all_text.lower()

disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'recovery', 'fire', 'woolsey', 'emergency']

matched = {}

for rec in funding:
    proj = rec.get('Project_Name', '')
    proj_low = proj.lower()
    found = False
    # prepare base name without parenthetical suffix
    import re
    base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()

    # check occurrences for proj_low and base
    for name_variant in [proj_low, base] if base and base != proj_low else [proj_low]:
        if not name_variant:
            continue
        start = 0
        while True:
            idx = all_text_low.find(name_variant, start)
            if idx == -1:
                break
            # context window
            ctx_start = max(0, idx - 200)
            ctx_end = min(len(all_text_low), idx + len(name_variant) + 200)
            context = all_text_low[ctx_start:ctx_end]
            # check if '2022' appears in context
            if '2022' in context:
                # check if disaster keyword in context or in project name
                if any(kw in context for kw in disaster_keywords) or any(kw in proj_low for kw in disaster_keywords):
                    matched[rec['Project_Name']] = rec
                    found = True
                    break
            start = idx + 1
        if found:
            break

# As fallback, include records whose project name includes disaster keywords and appear anywhere with 2022 in the documents
if not matched:
    # if matched is empty, still run fallback, but we'll always run to capture others
    pass
for rec in funding:
    if rec['Project_Name'] in matched:
        continue
    proj = rec.get('Project_Name', '')
    proj_low = proj.lower()
    if any(kw in proj_low for kw in ['fema', 'caloes', 'caljpia']):
        # check if project base appears near any '2022' in the docs
        base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()
        if base:
            # find occurrences of base and see if '2022' nearby
            idx = all_text_low.find(base)
            if idx != -1:
                ctx_start = max(0, idx - 200)
                ctx_end = min(len(all_text_low), idx + len(base) + 200)
                context = all_text_low[ctx_start:ctx_end]
                if '2022' in context:
                    matched[rec['Project_Name']] = rec

# Prepare unique matched list
matched_list = list(matched.values())

total = sum(r['Amount'] for r in matched_list)

output = {
    'total_funding': total,
    'matched_projects': [{ 'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in matched_list]
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ewZx9GEvkYHuhFSdepF0EpJu': ['civic_docs'], 'var_call_P0nG1k5Ak7Vdxl9PloiZ7Cjc': ['Funding'], 'var_call_3V3LBuTrnTf5FD8CAnAfAlHL': 'file_storage/call_3V3LBuTrnTf5FD8CAnAfAlHL.json', 'var_call_NT3Q3dsTFn3mJHGGbLBIEHZH': 'file_storage/call_NT3Q3dsTFn3mJHGGbLBIEHZH.json'}

exec(code, env_args)
