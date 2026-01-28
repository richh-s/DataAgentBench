code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_B2hfmP0foXcqmfeCROE6YrpQ
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

# Heuristically extract project blocks: split on two newlines followed by a capitalized line
blocks = re.split(r'\n\n(?=[A-Z0-9].+)', full_text)

projects = []
for blk in blocks:
    # project name is first line if it's not too generic
    lines = [l.strip() for l in blk.split('\n') if l.strip()]
    if not lines:
        continue
    name = lines[0]
    # Skip non-project headers
    if len(name.split()) < 2:
        continue
    # Determine topic keywords
    lower_blk = blk.lower()
    topics = []
    for kw in ['park','playground','road','highway','bridge','storm drain','drainage','water treatment','guardrail','fema','fire','emergency warning','warning','skate','walkway','median','traffic']:
        if kw in lower_blk:
            topics.append(kw)
    if not topics:
        continue
    topic_str = ','.join(sorted(set(topics)))
    # Status
    status = None
    if re.search(r'construction was completed|construction was complete|construction was completed,', lower_blk):
        status = 'completed'
    elif re.search(r'construction was completed november 2022|construction was completed, november 2022', lower_blk):
        status = 'completed'
    elif 'design' in lower_blk:
        status = 'design'
    elif 'not started' in lower_blk:
        status = 'not started'
    # Dates: look for year patterns
    dates = re.findall(r'(20\d{2}[^\n]{0,15})', blk)
    st = dates[0] if dates else None
    et = None
    for d in dates[::-1]:
        if 'complete' in d.lower() or 'completed' in d.lower() or 'construction was completed' in lower_blk:
            et = d
            break
    projects.append({'Project_Name': name, 'topic': topic_str, 'status': status, 'st': st, 'et': et, 'raw': blk[:400]})

# Filter to park-related (topic contains 'park' or 'playground') and completed with 2022 in any date string
park_projects_2022 = []
for p in projects:
    if not p['status'] == 'completed':
        continue
    if not any(t in p['topic'] for t in ['park','playground']):
        continue
    datestrs = [d for d in [p['st'], p['et']] if d]
    if not any('2022' in d for d in datestrs) and '2022' not in p['raw']:
        continue
    park_projects_2022.append(p)

# Load funding table preview from storage variable (already full list, not a path)
funding_records = var_call_dtporwjtaL2GbdQyGrIJb6eA
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_df = pd.DataFrame(park_projects_2022)

# Fuzzy/loose merge by checking if names are substrings of each other (case-insensitive)
funding_total = 0
matched = []
for _, prow in proj_df.iterrows():
    pname = prow['Project_Name']
    pl = pname.lower()
    mask = fund_df['Project_Name'].str.lower().apply(lambda x: pl in x or x in pl)
    sub = fund_df[mask]
    if not sub.empty:
        s = int(sub['Amount'].sum())
        funding_total += s
        matched.append({'project': pname, 'funding_matches': sub['Project_Name'].tolist(), 'amount_sum': s})

result = {'total_funding_park_completed_2022': funding_total, 'matched_projects': matched}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_B2hfmP0foXcqmfeCROE6YrpQ': 'file_storage/call_B2hfmP0foXcqmfeCROE6YrpQ.json', 'var_call_dtporwjtaL2GbdQyGrIJb6eA': 'file_storage/call_dtporwjtaL2GbdQyGrIJb6eA.json'}

exec(code, env_args)
