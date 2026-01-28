code = """import json
import pandas as pd
import re
from pathlib import Path

# Load variables

def load_var(var):
    if isinstance(var, str) and Path(var).exists():
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

civic_docs = load_var(var_call_RYDoXwHwQP3C6w3KWpeJg1hA)
funding = load_var(var_call_SDrwtL7qxx6JOB3NWS3moZfR)

funding_df = pd.DataFrame(funding)
# ensure columns exist
if 'Project_Name' not in funding_df.columns:
    funding_df['Project_Name'] = ''

funding_df['Project_Name_norm'] = funding_df['Project_Name'].astype(str).str.replace(r"\(.*?\)", "", regex=True).str.strip().str.lower()

# Search civic docs for relevant project names
keyword_pattern = re.compile(r"\b(emergency|fema)\b", re.IGNORECASE)
project_keyword_words = [
    'Project','Repairs','Improvements','Repair','Replacement','Sirens','Warning','Bridge','Culvert','Drain','Road','Roadway','Resurfacing','Storm Drain','Water Treatment','Walkway','Playground','Traffic Study','Shade Structure','Slope Repairs','Culvert Repairs','Retaining Wall Repair'
]
proj_kw_regex = re.compile(r"\b(?:" + '|'.join([re.escape(w) for w in project_keyword_words]) + r")\b", re.IGNORECASE)

status_map = {
    'design': re.compile(r"\b(design|preliminary design|complete design)\b", re.IGNORECASE),
    'completed': re.compile(r"\b(construction was completed|complete construction|completed|notice of completion|complete construction:)\b", re.IGNORECASE),
    'not started': re.compile(r"\b(not started|identified|waiting for|awaiting|will be|to be discussed|scheduled for|pending|rejected all bids)\b", re.IGNORECASE)
}

found_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    if not keyword_pattern.search(text):
        continue
    lines = [ln.rstrip() for ln in text.splitlines()]
    # candidate title lines
    candidate_lines = []
    for idx, ln in enumerate(lines):
        if proj_kw_regex.search(ln) and re.search(r"[A-Za-z]", ln):
            s = re.sub(r"\s+", ' ', ln).strip()
            s = re.sub(r"^\(cid:\d+\)\s*", '', s)
            if len(s) > 3:
                candidate_lines.append((idx, s))
    # find keyword occurrences and associate
    for m in keyword_pattern.finditer(text):
        char_pos = m.start()
        cum = 0
        line_idx = 0
        for i, ln in enumerate(lines):
            cum += len(ln) + 1
            if cum > char_pos:
                line_idx = i
                break
        chosen = None
        min_dist = None
        for idx, s in candidate_lines:
            if idx <= line_idx and (line_idx - idx) <= 20:
                dist = line_idx - idx
                if min_dist is None or dist < min_dist:
                    chosen = (idx, s)
                    min_dist = dist
        if chosen:
            pname = chosen[1]
            start = max(0, chosen[0]-2)
            end = min(len(lines), chosen[0]+8)
            window = ' '.join(lines[start:end])
            status = 'unknown'
            for st_key, pat in status_map.items():
                if pat.search(window):
                    status = st_key
                    break
            found_projects.append({'Project_Name': pname, 'Project_Name_norm': re.sub(r"\(.*?\)", "", pname).strip().lower(), 'Status': status, 'Source_File': doc.get('filename')})

# Deduplicate
proj_df = pd.DataFrame(found_projects)
if proj_df.empty:
    proj_df = pd.DataFrame(columns=['Project_Name','Project_Name_norm','Status','Source_File'])
else:
    proj_df = proj_df.drop_duplicates(subset=['Project_Name_norm'])

# Build results by matching funding records that are related to FEMA or emergency or match extracted projects
results = []
seen = set()

# list of normalized project names extracted
extracted_norms = proj_df['Project_Name_norm'].tolist()

for _, frow in funding_df.iterrows():
    fname = str(frow.get('Project_Name',''))
    fnorm = str(frow.get('Project_Name_norm',''))
    include = False
    # include if funding project name mentions FEMA or emergency
    if re.search(r"\b(fema|emergency)\b", fname, re.IGNORECASE):
        include = True
    # include if any extracted project norm is substring of funding project name norm
    for en in extracted_norms:
        if en and en in fnorm:
            include = True
            break
    if include:
        # determine status by matching to extracted
        status = 'unknown'
        for en in extracted_norms:
            if en and en in fnorm:
                row = proj_df[proj_df['Project_Name_norm']==en]
                if not row.empty:
                    status = row.iloc[0]['Status']
                    break
        amt = None
        try:
            amt = int(frow.get('Amount'))
        except Exception:
            try:
                amt = int(float(frow.get('Amount')))
            except Exception:
                amt = None
        key = (fname, frow.get('Funding_Source'))
        if key in seen:
            continue
        results.append({'Project_Name': fname, 'Funding_Source': frow.get('Funding_Source'), 'Amount': amt, 'Status': status})
        seen.add(key)

# If no extracted projects and no funding matched, as a fallback include any funding rows with 'FEMA' in name
if not results:
    fema_rows = funding_df[funding_df['Project_Name'].str.contains(r'(?i)fema')]
    for _, frow in fema_rows.iterrows():
        amt = None
        try:
            amt = int(frow.get('Amount'))
        except Exception:
            amt = None
        results.append({'Project_Name': frow.get('Project_Name'), 'Funding_Source': frow.get('Funding_Source'), 'Amount': amt, 'Status': 'unknown'})

# Final sort and dedupe
final = []
seen = set()
for r in results:
    key = (r['Project_Name'], r['Funding_Source'])
    if key in seen:
        continue
    final.append(r)
    seen.add(key)

final_sorted = sorted(final, key=lambda x: (x['Project_Name'] or '').lower())

print('__RESULT__:')
print(json.dumps(final_sorted))"""

env_args = {'var_call_RYDoXwHwQP3C6w3KWpeJg1hA': 'file_storage/call_RYDoXwHwQP3C6w3KWpeJg1hA.json', 'var_call_SDrwtL7qxx6JOB3NWS3moZfR': 'file_storage/call_SDrwtL7qxx6JOB3NWS3moZfR.json'}

exec(code, env_args)
