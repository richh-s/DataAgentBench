code = """import json, re
# Load data from storage-provided file paths
with open(var_call_CkTOw7owItg4Nr1WGfO0TMTR, 'r') as f:
    funding_records = json.load(f)
with open(var_call_Tw7i9VffVvctxE6jTB66qGgv, 'r') as f:
    civic_docs = json.load(f)

# Build combined capital design sections text
capital_design_texts = []
for doc in civic_docs:
    text = doc.get('text','')
    start_idx = text.find('Capital Improvement Projects (Design)')
    if start_idx == -1:
        # also try without exact case or slight variants
        start_idx = text.lower().find('capital improvement projects (design)')
        if start_idx == -1:
            continue
    # find end by searching common next headers
    possible_ends = [
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)',
        'Capital Improvement Projects (Construction)',
        'Capital Improvement Projects (Not Started)'
    ]
    end_idx = len(text)
    for pe in possible_ends:
        i = text.find(pe, start_idx+1)
        if i != -1 and i < end_idx:
            end_idx = i
    # also stop at 'Capital Improvement Projects (Construction)' case-insensitive
    m = re.search(r'Capital Improvement Projects \(Construction\)', text[start_idx+1:], re.IGNORECASE)
    if m:
        mi = start_idx+1 + m.start()
        if mi < end_idx:
            end_idx = mi
    section = text[start_idx:end_idx]
    capital_design_texts.append(section)

combined_design_text = "\n".join(capital_design_texts).lower()

# Helper to normalize names
def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    s = re.sub(r"\s+", ' ', s)
    s = s.strip()
    return s

# Build funding set for amounts > 50000
funding_over_50k = []
for r in funding_records:
    # Amount may be string
    amt = r.get('Amount')
    try:
        amt_num = int(str(amt))
    except:
        try:
            amt_num = int(float(str(amt)))
        except:
            continue
    if amt_num > 50000:
        funding_over_50k.append({'Project_Name': r.get('Project_Name',''), 'Amount': amt_num})

# Match funding projects to capital design section by substring checks
matched = []
for rec in funding_over_50k:
    name = rec['Project_Name']
    name_norm = normalize(name)
    # variant without parenthetical suffix
    name_no_paren = re.sub(r"\s*\([^)]*\)", '', name_norm).strip()
    found = False
    if name_norm and name_norm in combined_design_text:
        found = True
    elif name_no_paren and name_no_paren in combined_design_text:
        found = True
    else:
        # also try token subset matching: check if main words (remove short words) appear
        tokens = [t for t in re.findall(r"[a-z0-9]+", name_no_paren) if len(t)>3]
        if tokens:
            if all(tok in combined_design_text for tok in tokens):
                found = True
    if found:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# Deduplicate by project name
unique_matched = {m['Project_Name']: m for m in matched}
result = {'count': len(unique_matched), 'projects': list(unique_matched.values())}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CkTOw7owItg4Nr1WGfO0TMTR': 'file_storage/call_CkTOw7owItg4Nr1WGfO0TMTR.json', 'var_call_Tw7i9VffVvctxE6jTB66qGgv': 'file_storage/call_Tw7i9VffVvctxE6jTB66qGgv.json'}

exec(code, env_args)
