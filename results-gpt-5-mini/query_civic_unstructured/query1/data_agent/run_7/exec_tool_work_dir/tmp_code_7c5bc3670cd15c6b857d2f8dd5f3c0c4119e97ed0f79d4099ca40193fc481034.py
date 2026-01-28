code = """import json
import re
import pandas as pd

# Load data from storage variables
with open(var_call_i016LNhktBsM0Pa9uU03XkyN, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_H4XHZByS1llC5NkeTNcB9Ya1, 'r', encoding='utf-8') as f:
    civdocs = json.load(f)

# Create funding DataFrame
df = pd.DataFrame(funding)
# Ensure Amount is int
df['Amount'] = df['Amount'].astype(int)
# Filter funding > 50000
df_gt50k = df[df['Amount'] > 50000]
project_names = df_gt50k['Project_Name'].tolist()

# Helper matching function
def name_matches_in_slice(name, text_slice):
    name_l = re.sub(r"[^\w\s]", ' ', name).lower()
    slice_l = text_slice.lower()
    # Exact substring
    if name_l.strip() in slice_l:
        return True
    # Token overlap: require 60% of tokens present
    tokens = [t for t in re.split(r"\W+", name_l) if len(t) > 2]
    if not tokens:
        return False
    matched = sum(1 for t in tokens if t in slice_l)
    return (matched / len(tokens)) >= 0.6

matched_projects = set()

# For each document, find the design section and check for project names
for doc in civdocs:
    text = doc.get('text', '')
    if not text:
        continue
    # Find design heading
    m = re.search(r'capital improvement projects\s*\(design\)', text, re.I)
    if not m:
        # try alternative heading variant
        m = re.search(r'capital improvement projects\s*\-\s*design', text, re.I)
    if not m:
        continue
    design_pos = m.start()
    # find next section headings to determine end
    next_candidates = []
    for pattern in [r'capital improvement projects\s*\(construction\)', r'capital improvement projects\s*\(not started\)']:
        mm = re.search(pattern, text, re.I)
        if mm and mm.start() > design_pos:
            next_candidates.append(mm.start())
    end_pos = min(next_candidates) if next_candidates else len(text)
    slice_text = text[design_pos:end_pos]
    # Check each funding project name for presence in slice
    for pname in project_names:
        if name_matches_in_slice(pname, slice_text):
            matched_projects.add(pname)

# Prepare result
result = {
    'count': len(matched_projects),
    'projects': sorted(list(matched_projects))
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_Ka4W7OCdQYDFnEmKkFvdUTMK': ['civic_docs'], 'var_call_6jKr6GnsPcOzra5FRfDKzYmg': ['Funding'], 'var_call_H4XHZByS1llC5NkeTNcB9Ya1': 'file_storage/call_H4XHZByS1llC5NkeTNcB9Ya1.json', 'var_call_i016LNhktBsM0Pa9uU03XkyN': 'file_storage/call_i016LNhktBsM0Pa9uU03XkyN.json'}

exec(code, env_args)
