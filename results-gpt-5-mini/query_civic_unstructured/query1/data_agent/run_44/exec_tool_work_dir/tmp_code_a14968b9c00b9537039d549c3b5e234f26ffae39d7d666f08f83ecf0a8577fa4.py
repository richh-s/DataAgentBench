code = """import json, re
# Load data from storage-provided file paths
with open(var_call_CkTOw7owItg4Nr1WGfO0TMTR, 'r') as f:
    funding_records = json.load(f)
with open(var_call_Tw7i9VffVvctxE6jTB66qGgv, 'r') as f:
    civic_docs = json.load(f)

# Build combined capital design sections text
design_phrase = 'capital improvement projects (design)'
construction_phrase = 'capital improvement projects (construction)'
notstarted_phrase = 'capital improvement projects (not started)'
capital_design_texts = []
for doc in civic_docs:
    text = doc.get('text', '')
    lower = text.lower()
    start_idx = lower.find(design_phrase)
    if start_idx == -1:
        continue
    end_idx = len(text)
    i = lower.find(construction_phrase, start_idx+1)
    if i != -1 and i < end_idx:
        end_idx = i
    j = lower.find(notstarted_phrase, start_idx+1)
    if j != -1 and j < end_idx:
        end_idx = j
    section = lower[start_idx:end_idx]
    capital_design_texts.append(section)

combined_design_text = '\n'.join(capital_design_texts)

# Helper to normalize names
def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    s = ' '.join(s.split())
    return s.strip()

# Build funding set for amounts > 50000
funding_over_50k = []
for r in funding_records:
    amt = r.get('Amount')
    try:
        amt_num = int(str(amt))
    except:
        try:
            amt_num = int(float(str(amt)))
        except:
            continue
    if amt_num > 50000:
        funding_over_50k.append({'Project_Name': r.get('Project_Name', ''), 'Amount': amt_num})

# Match funding projects to capital design section by substring checks
matched = []
for rec in funding_over_50k:
    name = rec['Project_Name']
    name_norm = normalize(name)
    name_no_paren = name_norm.split('(')[0].strip()
    found = False
    if name_norm and name_norm in combined_design_text:
        found = True
    elif name_no_paren and name_no_paren in combined_design_text:
        found = True
    else:
        tokens = [t for t in re.findall(r"[a-z0-9]+", name_no_paren) if len(t) > 3]
        if tokens:
            if all(tok in combined_design_text for tok in tokens):
                found = True
    if found:
        matched.append({'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']})

# Deduplicate by project name
unique_matched = {m['Project_Name']: m for m in matched}
result = {'count': len(unique_matched), 'projects': list(unique_matched.values())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CkTOw7owItg4Nr1WGfO0TMTR': 'file_storage/call_CkTOw7owItg4Nr1WGfO0TMTR.json', 'var_call_Tw7i9VffVvctxE6jTB66qGgv': 'file_storage/call_Tw7i9VffVvctxE6jTB66qGgv.json'}

exec(code, env_args)
