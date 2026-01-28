code = """import json
import re
import pandas as pd

# Load funding data
funding_data = None
if isinstance(var_call_zabsscRi2sX7fjOAPL7SaYEO, str):
    with open(var_call_zabsscRi2sX7fjOAPL7SaYEO, 'r', encoding='utf-8') as f:
        funding_data = json.load(f)
else:
    funding_data = var_call_zabsscRi2sX7fjOAPL7SaYEO

# Load civic docs data
civic_docs = None
if isinstance(var_call_uQTGczZVLvj89WNp2jZEZjri, str):
    with open(var_call_uQTGczZVLvj89WNp2jZEZjri, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_call_uQTGczZVLvj89WNp2jZEZjri

funding_df = pd.DataFrame(funding_data)
# Normalize columns
if 'Amount' in funding_df.columns:
    # convert to int where possible
    def to_int(x):
        try:
            return int(x)
        except:
            try:
                return int(float(x))
            except:
                return None
    funding_df['Amount'] = funding_df['Amount'].apply(to_int)

# Filter funding records related to FEMA or emergency (and related warning/siren)
pattern = re.compile(r'(fema|emergency|warning|siren)', re.IGNORECASE)
mask = funding_df['Project_Name'].apply(lambda x: bool(pattern.search(x)) if isinstance(x, str) else False)
selected = funding_df[mask].copy()

# Prepare civic texts concatenated for searching
texts = []
for doc in civic_docs:
    txt = doc.get('text','')
    texts.append(txt)

# Helper to determine status from surrounding text
def infer_status(project_name, texts):
    core = re.sub(r"\s*\(.*?\)", "", project_name).strip()
    core_l = core.lower()
    for txt in texts:
        t = txt.lower()
        idx = t.find(core_l)
        if idx >= 0:
            start = max(0, idx-300)
            end = min(len(t), idx+300)
            win = t[start:end]
            # Check completed
            if any(kw in win for kw in ['construction was completed', 'complete construction', 'notice of completion', 'completed,', 'construction: complete', 'complete construction:']):
                return 'completed'
            if 'construction was completed' in win or 'construction was completed' in win:
                return 'completed'
            # Check not started
            if any(kw in win for kw in ['not started', 'not begun', 'identified but not begun']):
                return 'not started'
            # Check design
            if any(kw in win for kw in ['complete design', 'final design', 'design', 'design plans', 'preliminary design', 'awaiting final fema', 'awaiting final fema/caloes', 'awaiting final fema/caloes approval', 'awaiting final fema/caloes approval','awaiting final fema/caloes']):
                return 'design'
            # Under construction -> treat as design (in absence of exact mapping)
            if 'under construction' in win or 'currently under construction' in win:
                return 'design'
            # If beginning construction soon -> design
            if 'begin construction' in win or 'begin construction:' in win:
                return 'design'
            # If project schedule indicates complete design and advertise -> design
            if 'complete design:' in win:
                return 'design'
    return 'unknown'

results = []
for _, row in selected.iterrows():
    pname = row['Project_Name']
    source = row.get('Funding_Source')
    amount = row.get('Amount')
    status = infer_status(pname, texts)
    results.append({'Project_Name': pname, 'Funding_Source': source, 'Amount': amount, 'Status': status})

# Also check for civic-only projects that mention FEMA/emergency but may not be in funding table
# Find unique project-like lines in civic docs that mention 'fema' or 'emergency' or 'warning' or 'sirens'
extra_projects = []
for txt in texts:
    t = txt
    # split into lines and look for lines that are short and title-cased or contain keywords
    for line in t.splitlines():
        if len(line.strip())==0:
            continue
        low = line.lower()
        if any(k in low for k in ['fema','emergency','warning','sirens','outdoor warning','outdoor warning signs']):
            # Heuristic: if line length < 120 and contains letters
            if len(line) < 120:
                name = line.strip()
                # check if already in results
                if not any(r['Project_Name'].lower()==name.lower() for r in results):
                    status = infer_status(name, texts)
                    extra_projects.append({'Project_Name': name, 'Funding_Source': None, 'Amount': None, 'Status': status})

# Combine, preferring funding info where available
all_results = results.copy()
# add extras that are not duplicates
for e in extra_projects:
    if not any(e['Project_Name'].lower() == r['Project_Name'].lower() for r in all_results):
        all_results.append(e)

# Output JSON string
out = json.dumps(all_results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zabsscRi2sX7fjOAPL7SaYEO': 'file_storage/call_zabsscRi2sX7fjOAPL7SaYEO.json', 'var_call_uQTGczZVLvj89WNp2jZEZjri': 'file_storage/call_uQTGczZVLvj89WNp2jZEZjri.json'}

exec(code, env_args)
