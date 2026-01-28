code = """import json
import pandas as pd

# load data from storage file paths
with open(var_call_Nyq3v81i5J3FccBQWicS4yfP, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2NecHsc1qpk3uh6At4Qi5mYr, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

fund_df = pd.DataFrame(funding_rows)
if not fund_df.empty:
    # convert Amount to int safely
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

season_keys = ['spring 2022','2022 spring','march 2022','april 2022','may 2022','2022-03','2022-04','2022-05','2022/03','2022/04','2022/05']
title_indicators = ['project','improvements','repairs','resurfacing','study','facility','renovation','replacement','phase','playground','park','road','drainage','master plan','repair']

found_projects = []
seen = set()

for doc in civic_docs:
    text = doc.get('text','')
    if not isinstance(text, str) or not text:
        continue
    lines = text.splitlines()
    n = len(lines)
    # normalize lines
    norm_lines = [ln.strip() for ln in lines]
    # for each line index, check a window of next 6 lines for season keywords
    for i in range(n):
        window = ' '.join(norm_lines[i:i+6]).lower()
        if any(k in window for k in season_keys):
            # search backwards up to 6 lines for a title-like line
            for j in range(max(0, i-6), i+1):
                ln = norm_lines[j]
                if not ln or len(ln) < 5 or len(ln) > 200:
                    continue
                low = ln.lower()
                if any(ind in low for ind in title_indicators) or ln.isupper() or (ln[0].isupper() and ' ' in ln):
                    # clean title
                    title = ' '.join(ln.split())
                    norm = title.lower()
                    if norm not in seen:
                        seen.add(norm)
                        found_projects.append(title)
                    break
            else:
                # fallback: take the line immediately before the season mention if plausible
                if i-1 >= 0:
                    ln = norm_lines[i-1]
                    if ln and 5 <= len(ln) <= 200:
                        title = ' '.join(ln.split())
                        norm = title.lower()
                        if norm not in seen:
                            seen.add(norm)
                            found_projects.append(title)

# As an additional pass, directly search for lines that themselves contain title indicators and also have season mention nearby in full text
full_text = '\n'.join([d.get('text','') for d in civic_docs if isinstance(d.get('text',''), str)])
for idx, line in enumerate(full_text.splitlines()):
    ln = line.strip()
    if not ln:
        continue
    low = ln.lower()
    if any(ind in low for ind in title_indicators):
        # check nearby chars for season mention
        pos = full_text.find(line)
        window = full_text[max(0,pos-200): pos+len(line)+200].lower()
        if any(k in window for k in season_keys):
            title = ' '.join(ln.split())
            norm = title.lower()
            if norm not in seen:
                seen.add(norm)
                found_projects.append(title)

# Deduplicate final list
projects = []
for p in found_projects:
    if p not in projects:
        projects.append(p)

# Join with funding table
results = []
for pname in projects:
    pname_low = pname.lower()
    # exact match
    matches = fund_df[fund_df['Project_Name'].astype(str).str.lower() == pname_low]
    if matches.empty:
        # contains
        matches = fund_df[fund_df['Project_Name'].astype(str).str.lower().str.contains(pname_low, na=False)]
    if matches.empty:
        # try partial token match: any funding name token in pname
        tokens = [t for t in re.split(r'\W+', pname_low) if t]
        if tokens:
            mask = fund_df['Project_Name'].astype(str).str.lower().apply(lambda x: all(tok in x for tok in tokens) if isinstance(x,str) else False)
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
