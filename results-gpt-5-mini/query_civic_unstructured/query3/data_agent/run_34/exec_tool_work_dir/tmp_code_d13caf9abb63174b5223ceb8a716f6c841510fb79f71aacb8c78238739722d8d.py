code = """import json, re

# Load data from previous tool calls
with open(var_call_RpKhjqFTVlsT3xmU5phuCvLx, 'r') as f:
    funding = json.load(f)
with open(var_call_OTsZFSddYbanLEHhV1oqAEar, 'r') as f:
    civic_docs = json.load(f)

# Combine civic docs texts
full_text = "\n\n".join(d.get('text','') for d in civic_docs)
full_text_lower = full_text.lower()

# Extract project titles that precede '(cid:190) Updates:' or '(cid:190) Project Description:'
pattern = re.compile(r"(?m)^(.+?)\n\n\(cid:190\) Updates:")
pattern2 = re.compile(r"(?m)^(.+?)\n\n\(cid:190\) Project Description:")

titles = set()
for m in pattern.finditer(full_text):
    title = m.group(1).strip()
    if title:
        titles.add(title)
for m in pattern2.finditer(full_text):
    title = m.group(1).strip()
    if title:
        titles.add(title)

# Determine which titles are related to 'fema' or 'emergency' by checking nearby context
related_titles = set()
for title in titles:
    # locate title in full_text (first occurrence)
    idx = full_text_lower.find(title.lower())
    if idx == -1:
        continue
    snippet = full_text_lower[max(0, idx-200): idx+800]
    if ('fema' in snippet) or ('emergency' in snippet) or ('outdoor warning' in title.lower()) or ('sirens' in title.lower()):
        related_titles.add(title.lower())

# Also include titles that themselves contain fema or emergency
for title in titles:
    tl = title.lower()
    if 'fema' in tl or 'emergency' in tl:
        related_titles.add(tl)

# Build results by joining funding records that are related by name or funding source
results = []

# helper: normalize project name by removing parenthetical suffixes and punctuation
def normalize_name(n):
    n2 = re.sub(r"\s*\(.*?\)", "", n)
    return re.sub(r"[^a-z0-9 ]+", " ", n2.lower()).strip()

# status inference function
def infer_status_for_name(name):
    base = normalize_name(name)
    # search occurrences
    idx = full_text_lower.find(base)
    snippet = ''
    if idx != -1:
        snippet = full_text_lower[max(0, idx-200): idx+800]
    else:
        # try partial matching by words
        words = base.split()
        for w in words[:5]:
            if len(w) > 3:
                i = full_text_lower.find(w)
                if i!=-1:
                    snippet = full_text_lower[max(0, i-200): i+800]
                    break

    s = 'unknown'
    if snippet:
        if any(k in snippet for k in [ 'construction was completed', 'complete construction', 'notice of completion', 'construction was completed', 'complete construction:', 'completed' ]):
            s = 'completed'
        elif any(k in snippet for k in [ 'complete design', 'preliminary design', 'final design', 'working with the consultant', 'working with the design', 'finalizing the design', 'project is in the preliminary design phase', 'design plans' ]):
            s = 'design'
        elif any(k in snippet for k in [ 'not started', 'identified', 'awaiting', 'waiting for', 'advertise:', 'begin construction:' , 'begin construction' ]):
            s = 'not started'
        elif 'under construction' in snippet or 'currently under construction' in snippet:
            # map under construction -> not started (construction in progress or imminent)
            s = 'not started'
    return s

# Precompute normalized related titles for substring matching
norm_related = [normalize_name(t) for t in related_titles]

for rec in funding:
    pname = rec.get('Project_Name','')
    p_lower = pname.lower()
    fund_src = rec.get('Funding_Source','')
    fund_src_low = fund_src.lower()
    amount = rec.get('Amount')
    try:
        amount_val = int(amount)
    except:
        try:
            amount_val = int(float(amount))
        except:
            amount_val = None

    include = False
    # direct FEMA or emergency mentions in project name or funding source
    if 'fema' in p_lower or 'fema' in fund_src_low or 'emergency' in p_lower or 'emergency' in fund_src_low:
        include = True
    else:
        # match against related titles
        base = normalize_name(pname)
        for rt in norm_related:
            if rt and (rt in base or base in rt):
                include = True
                break

    if include:
        status = infer_status_for_name(pname)
        results.append({
            'Project_Name': pname,
            'Funding_Source': fund_src,
            'Amount': amount_val,
            'Status': status
        })

# Remove duplicates by Project_Name (keep first)
seen = set()
final = []
for r in results:
    if r['Project_Name'] not in seen:
        final.append(r)
        seen.add(r['Project_Name'])

# Sort by Project_Name
final_sorted = sorted(final, key=lambda x: x['Project_Name'].lower())

import json
print("__RESULT__:")
print(json.dumps(final_sorted))"""

env_args = {'var_call_OTsZFSddYbanLEHhV1oqAEar': 'file_storage/call_OTsZFSddYbanLEHhV1oqAEar.json', 'var_call_RpKhjqFTVlsT3xmU5phuCvLx': 'file_storage/call_RpKhjqFTVlsT3xmU5phuCvLx.json'}

exec(code, env_args)
