code = """import json
import pandas as pd

# Load data files from storage variables
with open(var_call_Nyq3v81i5J3FccBQWicS4yfP, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2NecHsc1qpk3uh6At4Qi5mYr, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

fund_df = pd.DataFrame(funding_rows)
if not fund_df.empty:
    def to_int(x):
        try:
            return int(x)
        except Exception:
            try:
                return int(float(x))
            except Exception:
                return 0
    fund_df['Amount'] = fund_df['Amount'].apply(to_int)
else:
    fund_df = pd.DataFrame(columns=['Funding_ID','Project_Name','Funding_Source','Amount'])

season_markers = ['spring 2022','march 2022','april 2022','may 2022','2022-03','2022-04','2022-05','2022/03','2022/04','2022/05','2022 spring']
title_indicators = ['project','improvements','repairs','resurfacing','study','facility','renovation','replacement','phase','playground','park','road','drainage','master plan','repair']

found_projects = []
seen = set()

for doc in civic_docs:
    text = doc.get('text','')
    if not isinstance(text, str) or not text:
        continue
    lowtext = text.lower()
    for marker in season_markers:
        start = 0
        while True:
            idx = lowtext.find(marker, start)
            if idx == -1:
                break
            # look back up to 400 chars for a candidate title line
            start_idx = max(0, idx - 400)
            prev_segment = text[start_idx:idx]
            lines = prev_segment.splitlines()
            candidate = ''
            for ln in reversed(lines):
                ln = ln.strip()
                if ln:
                    candidate = ln
                    break
            if candidate:
                if 5 <= len(candidate) <= 200:
                    lown = candidate.lower()
                    if any(ind in lown for ind in title_indicators) or candidate.isupper() or (candidate[0].isupper() and ' ' in candidate):
                        norm = ' '.join(candidate.split())
                        if norm.lower() not in seen:
                            seen.add(norm.lower())
                            found_projects.append(norm)
            start = idx + len(marker)

# Additional pass: lines that look like titles and have season markers nearby
for doc in civic_docs:
    text = doc.get('text','')
    if not isinstance(text, str) or not text:
        continue
    lines = text.splitlines()
    pos = 0
    for ln in lines:
        ln_stripped = ln.strip()
        length = len(ln) + 1
        if 5 <= len(ln_stripped) <= 200:
            low = ln_stripped.lower()
            if any(ind in low for ind in title_indicators) or ln_stripped.isupper() or (ln_stripped[0].isupper() and ' ' in ln_stripped):
                # check nearby for season markers
                window = text[max(0, pos-300): pos+len(ln_stripped)+300].lower()
                if any(m in window for m in season_markers):
                    norm = ' '.join(ln_stripped.split())
                    if norm.lower() not in seen:
                        seen.add(norm.lower())
                        found_projects.append(norm)
        pos += length

# Final dedup
projects = []
for p in found_projects:
    if p not in projects:
        projects.append(p)

# Join with funding
results = []
for pname in projects:
    pname_low = pname.lower()
    matches = fund_df[fund_df['Project_Name'].astype(str).str.lower() == pname_low]
    if matches.empty:
        matches = fund_df[fund_df['Project_Name'].astype(str).str.lower().str.contains(pname_low, na=False)]
    if matches.empty:
        tokens = [t for t in pname_low.split() if t]
        if tokens:
            mask = fund_df['Project_Name'].astype(str).str.lower().apply(lambda x: all(tok in x for tok in tokens) if isinstance(x, str) else False)
            matches = fund_df[mask]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    rows = matches.to_dict(orient='records')
    results.append({'Project_Name': pname, 'Funding': total, 'Funding_Records': rows})

count = len(projects)
total_funding = sum(r['Funding'] for r in results)

out = {'count': count, 'total_funding': total_funding, 'projects': results}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Y6KliHUVetrVzq4id2vRDGuk': ['civic_docs'], 'var_call_GXwgmB9PEiwyXVvvgDY0YcyO': ['Funding'], 'var_call_Nyq3v81i5J3FccBQWicS4yfP': 'file_storage/call_Nyq3v81i5J3FccBQWicS4yfP.json', 'var_call_2NecHsc1qpk3uh6At4Qi5mYr': 'file_storage/call_2NecHsc1qpk3uh6At4Qi5mYr.json'}

exec(code, env_args)
