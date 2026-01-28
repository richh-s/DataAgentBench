code = """import json
import re
import pandas as pd

# Load large results from files provided in storage
with open(var_call_Nyq3v81i5J3FccBQWicS4yfP, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_2NecHsc1qpk3uh6At4Qi5mYr, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

fund_df = pd.DataFrame(funding_rows)
if not fund_df.empty:
    # ensure Amount numeric
    fund_df['Amount'] = fund_df['Amount'].astype(int)
else:
    fund_df = pd.DataFrame(columns=['Funding_ID','Project_Name','Funding_Source','Amount'])

# helper to detect spring 2022 mentions
spring_re = re.compile(r"(Spring|March|April|May)\s*[, ]*2022|2022[-/ ]?(?:Spring|03|04|05)|\b2022\b.*?(?:March|April|May)", flags=re.IGNORECASE)

# keywords to identify project title lines
title_keywords = ['project', 'improvements', 'repair', 'repairs', 'resurfacing', 'study', 'facility', 'renovation', 'replacement', 'phase', 'resurfacing', 'playground', 'park', 'road', 'drainage', 'master plan']

candidate_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    if not isinstance(text, str):
        continue
    # Split into lines and also keep full text for window searches
    lines = text.splitlines()
    # create cumulative positions for each line to map line index to char pos
    positions = []
    pos = 0
    for ln in lines:
        positions.append(pos)
        pos += len(ln) + 1
    full = text
    for i, ln in enumerate(lines):
        ln_stripped = ln.strip()
        if len(ln_stripped) < 5 or len(ln_stripped) > 200:
            continue
        low = ln_stripped.lower()
        if any(k in low for k in title_keywords) or '2022' in low:
            # consider this a candidate title
            start = positions[i]
            end = start + len(ln)
            # search window around this line (200 chars before and after)
            window_start = max(0, start-200)
            window_end = min(len(full), end+500)
            window = full[window_start:window_end]
            if spring_re.search(window):
                # Clean title: remove leading bullets or numbers
                title = re.sub(r"^[\W_]+|[\W_]+$", '', ln_stripped)
                # additional cleanup: collapse whitespace
                title = re.sub(r"\s+", ' ', title)
                candidate_projects.append({'Project_Name': title, 'source_file': doc.get('filename')})

# Also look for headings formatted as lines that end with 'Project' with preceding context
for doc in civic_docs:
    text = doc.get('text','')
    if not isinstance(text, str):
        continue
    for m in re.finditer(r"([A-Z][A-Za-z0-9 &'\-/,\.\(\)]+?(?:Project|Improvements|Repairs|Resurfacing|Study|Facility|Renovation|Replacement))", text):
        title = m.group(1).strip()
        # window around match
        window = text[max(0, m.start()-200): m.end()+200]
        if spring_re.search(window):
            title_clean = re.sub(r"\s+", ' ', re.sub(r"^[\W_]+|[\W_]+$", '', title))
            candidate_projects.append({'Project_Name': title_clean, 'source_file': doc.get('filename')})

# Deduplicate by normalized name
seen = set()
projects = []
for p in candidate_projects:
    name = p['Project_Name']
    norm = re.sub(r"\s+", ' ', name).strip().lower()
    if norm not in seen:
        seen.add(norm)
        projects.append(name)

# If none found, as fallback, search for any mention of 'Spring 2022' and grab nearest Title-like preceding line
if not projects:
    for doc in civic_docs:
        text = doc.get('text','')
        for m in spring_re.finditer(text):
            start = m.start()
            # look back for previous newline and take the previous non-empty line
            prev = text[:start].rstrip('\n')
            lines = prev.splitlines()
            if lines:
                candidate = lines[-1].strip()
                if len(candidate)>5 and len(candidate)<200:
                    title = re.sub(r"\s+", ' ', re.sub(r"^[\W_]+|[\W_]+$", '', candidate))
                    norm = title.lower()
                    if norm not in seen:
                        seen.add(norm)
                        projects.append(title)

# Now join with funding
results = []
for pname in projects:
    pname_low = pname.lower()
    # exact match
    matches = fund_df[fund_df['Project_Name'].astype(str).str.lower() == pname_low]
    # if no exact match, try contains
    if matches.empty:
        matches = fund_df[fund_df['Project_Name'].astype(str).str.lower().str.contains(pname_low, na=False)]
    if matches.empty:
        # try reverse contains: project name contains funding name fragment
        matches = fund_df[fund_df['Project_Name'].astype(str).apply(lambda x: pname_low in x.lower() if isinstance(x,str) else False)]
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
