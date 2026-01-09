code = """import json, re, pandas as pd
from pathlib import Path

# Load funding totals
p = Path(var_call_iWlvf1w9K4H2EEJVqj4PDnhd)
funding = json.loads(p.read_text())
df_f = pd.DataFrame(funding)
df_f['total_amount'] = pd.to_numeric(df_f['total_amount'])

# Load civic docs subset (contains 'disaster' somewhere)
p2 = Path(var_call_VY1KuUzWSgOAlthz2fEG5f9x)
docs = json.loads(p2.read_text())

# Extract Disaster Recovery Projects section and their schedule begin/start markers.
# We'll capture project names listed under 'Disaster Recovery Projects' and then look for 'Begin Construction'/'Begin' or similar lines for year 2022.

disaster_projects = {}  # name -> has_start_2022 bool

for d in docs:
    text = d.get('text','')
    # Normalize whitespace
    t = re.sub(r'\r', '\n', text)

    # Find blocks starting at 'Disaster Recovery Projects' up to next major heading ('Capital' or end)
    for m in re.finditer(r'(?is)Disaster Recovery Projects\b(.*?)(?:\n\s*Capital Improvement Projects\b|\Z)', t):
        block = m.group(1)
        # Project names typically appear as standalone lines (Title Case) before an 'Updates:' marker
        lines = [ln.strip() for ln in block.split('\n') if ln.strip()]
        # Identify candidate names: lines not starting with bullets and not containing ':' and not generic words
        candidates = []
        for ln in lines:
            if len(ln) < 3: 
                continue
            if re.match(r'^[\(\[\{\*\-\u2022\u00b7\u00a7\u00b6]', ln):
                continue
            if ':' in ln:
                continue
            if re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Page\s+\d+|Agenda Item)', ln, re.I):
                continue
            # likely a project name if it has letters and not too long
            if re.search(r'[A-Za-z]', ln):
                # avoid headings like 'Disaster Recovery Projects (Design)'
                if re.search(r'Disaster Recovery Projects', ln, re.I):
                    continue
                candidates.append(ln)
        # Deduplicate preserving order
        seen=set(); cand=[]
        for c in candidates:
            if c not in seen:
                seen.add(c); cand.append(c)

        # For each candidate, look ahead in the block for a schedule mentioning Begin/Start in 2022.
        # We'll search within a window around the name.
        for name in cand:
            # locate occurrences of name in block
            for nm in re.finditer(re.escape(name), block):
                start = max(0, nm.start()-0)
                end = min(len(block), nm.end()+1200)
                window = block[start:end]
                # look for begin/start lines containing 2022
                has_2022 = bool(re.search(r'(?i)(Begin|Start)(?:\s+\w+){0,3}\s*:?\s*[^\n]*2022', window)) or bool(re.search(r'(?i)2022[^\n]*(Begin|Start)', window))
                # also allow 'Begin Construction: 2022' and 'Begin construction: Spring 2022'
                if has_2022:
                    disaster_projects[name] = True
                else:
                    disaster_projects.setdefault(name, False)

# Filter to those with start in 2022
start_2022_projects = [k for k,v in disaster_projects.items() if v]

# Join funding totals
if len(start_2022_projects)==0:
    total = 0
else:
    df_join = df_f[df_f['Project_Name'].isin(start_2022_projects)]
    total = int(df_join['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects_count': int(len(start_2022_projects)),
    'matched_projects': sorted(start_2022_projects)[:50]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_1ebOZ15ayV0lFyqWtJ57nNZo': ['Funding'], 'var_call_fE7quFsgt4sJz0LUfYJgwzqP': ['civic_docs'], 'var_call_iWlvf1w9K4H2EEJVqj4PDnhd': 'file_storage/call_iWlvf1w9K4H2EEJVqj4PDnhd.json', 'var_call_VY1KuUzWSgOAlthz2fEG5f9x': 'file_storage/call_VY1KuUzWSgOAlthz2fEG5f9x.json'}

exec(code, env_args)
