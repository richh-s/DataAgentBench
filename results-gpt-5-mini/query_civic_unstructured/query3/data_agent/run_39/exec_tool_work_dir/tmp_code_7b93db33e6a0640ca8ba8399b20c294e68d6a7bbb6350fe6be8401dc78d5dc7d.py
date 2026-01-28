code = """import json
import pandas as pd
import re
from pathlib import Path

# Load variables provided in storage

def load_var(var):
    if isinstance(var, str) and Path(var).exists():
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return var

civic_docs = load_var(var_call_RYDoXwHwQP3C6w3KWpeJg1hA)
funding = load_var(var_call_SDrwtL7qxx6JOB3NWS3moZfR)

funding_df = pd.DataFrame(funding)

# Normalize funding project name
funding_df['Project_Name_norm'] = funding_df['Project_Name'].astype(str).str.replace(r"\(.*?\)", "", regex=True).str.strip().str.lower()

# Patterns
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
    # Find candidate project title lines: lines that contain project keywords and start with capital letter
    candidate_lines = []
    for idx, ln in enumerate(lines):
        if proj_kw_regex.search(ln) and re.search(r"[A-Za-z]", ln):
            # normalize whitespace
            s = re.sub(r"\s+", ' ', ln).strip()
            # remove leading bullets like (cid:190) or numbering
            s = re.sub(r"^\(cid:\d+\)\s*", '', s)
            if len(s) > 3 and any(ch.isupper() for ch in s.split()[0]):
                candidate_lines.append((idx, s))
    # For each keyword occurrence, find nearest candidate line within 20 lines before
    for m in keyword_pattern.finditer(text):
        # determine line number of match
        char_pos = m.start()
        # find line index
        cum = 0
        line_idx = 0
        for i, ln in enumerate(lines):
            cum += len(ln) + 1
            if cum > char_pos:
                line_idx = i
                break
        # search backwards up to 20 lines for candidate
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
            # find status by looking in window of lines around chosen index
            start = max(0, chosen[0]-2)
            end = min(len(lines), chosen[0]+8)
            window = ' '.join(lines[start:end])
            status = 'unknown'
            for st_key, pat in status_map.items():
                if pat.search(window):
                    status = st_key
                    break
            found_projects.append({'Project_Name': pname, 'Project_Name_norm': re.sub(r"\(.*?\)", "", pname).strip().lower(), 'Status': status, 'Source_File': doc.get('filename')})

# Deduplicate by normalized name
proj_df = pd.DataFrame(found_projects).drop_duplicates(subset=['Project_Name_norm'])

results = []
seen = set()

# Match funding records
for _, prow in proj_df.iterrows():
    pnorm = prow['Project_Name_norm']
    # find funding matches where normalized funding contains pnorm or vice versa
    matches = funding_df[funding_df['Project_Name_norm'].str.contains(re.escape(pnorm), na=False) | funding_df['Project_Name_norm'].apply(lambda x: pnorm in str(x))]
    # also include funding rows that have 'fema' in Project_Name
    fema_rows = funding_df[funding_df['Project_Name'].str.contains(r'(?i)fema')]
    matches = pd.concat([matches, fema_rows]).drop_duplicates()
    if matches.empty:
        key = (prow['Project_Name'], None)
        if key not in seen:
            results.append({'Project_Name': prow['Project_Name'], 'Funding_Source': None, 'Amount': None, 'Status': prow['Status']})
            seen.add(key)
    else:
        for _, frow in matches.iterrows():
            key = (frow['Project_Name'], frow['Funding_Source'])
            if key in seen:
                continue
            amt = None
            try:
                amt = int(frow['Amount'])
            except Exception:
                try:
                    amt = int(float(frow['Amount']))
                except Exception:
                    amt = None
            results.append({'Project_Name': frow['Project_Name'], 'Funding_Source': frow['Funding_Source'], 'Amount': amt, 'Status': prow['Status']})
            seen.add(key)

# Also add any funding entries that explicitly reference FEMA even if not matched above
fema_funding = funding_df[funding_df['Project_Name'].str.contains(r'(?i)fema')]
for _, frow in fema_funding.iterrows():
    key = (frow['Project_Name'], frow['Funding_Source'])
    if key in seen:
        continue
    amt = None
    try:
        amt = int(frow['Amount'])
    except Exception:
        amt = None
    # attempt to find status from proj_df by partial match
    status = 'unknown'
    norm = re.sub(r"\(.*?\)", "", frow['Project_Name']).strip().lower()
    m = proj_df[proj_df['Project_Name_norm'].str.contains(re.escape(norm.split()[0]), na=False)]
    if not m.empty:
        status = m.iloc[0]['Status']
    results.append({'Project_Name': frow['Project_Name'], 'Funding_Source': frow['Funding_Source'], 'Amount': amt, 'Status': status})
    seen.add(key)

# Final dedupe and sort
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
