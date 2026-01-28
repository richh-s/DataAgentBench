code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0
fund_list = [(rec.get('Project_Name','').strip(), parse_amount(rec.get('Amount',0))) for rec in funding]

# cleaning helpers
def clean_text(s):
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def tokens(s):
    return [t.lower() for t in re.findall(r"[A-Za-z]{3,}", s)]

# find occurrences of begin construction with spring within same sentence or nearby
occurs = []
pattern = re.compile(r'begin construction[:\s\-]*([^\n]*)', re.I)
for doc in civic_docs:
    text = doc.get('text','')
    for m in pattern.finditer(text):
        span = m.span()
        context_start = max(0, span[0]-400)
        context = text[context_start:span[1]+200]
        if re.search(r'spring', context, re.I):
            occurs.append((doc.get('filename',''), span[0], context))

# For each occurrence, try to extract project title by looking backwards for typical title lines
project_titles = []
for filename, pos, context in occurs:
    # look at text before the match up to 400 chars
    before = context.split('\n')[:10]
    # Instead, search in the original doc text at position
    # find the nearest line breaks before pos
    for doc in civic_docs:
        if doc.get('filename','')==filename:
            txt = doc.get('text','')
            break
    # find line index
    prefix = txt[:pos]
    lines = txt.splitlines()
    # compute cumulative lengths to find line index
    cum = 0
    line_idx = 0
    for i, L in enumerate(lines):
        cum += len(L)+1
        if cum >= pos:
            line_idx = i
            break
    # search backward up to 15 lines
    title = None
    for j in range(max(0, line_idx-15), line_idx)[::-1]:
        cand = lines[j].strip()
        if not cand:
            continue
        # skip generic header lines
        if re.search(r'\b(updates|project schedule|project description|agenda report|agenda item|page|item|to:|prepared by|approved by|date prepared|meeting date|subject|discussion|recommended action|recommendation)\b', cand, re.I):
            continue
        # prefer lines that contain 'Project' or have Title Case words or key tokens
        if re.search(r'\bProject\b', cand, re.I) or re.search(r'\b(Park|Road|PCH|Median|Skate|Shade|Playground|Retaining Wall|Civic Center|Water Treatment|Stormwater|Drain|Resurfacing|Improvements|Repairs|Way)\b', cand, re.I):
            title = cand
            break
        # else if line looks like a title (short, title case)
        words = cand.split()
        cap_words = sum(1 for w in words if re.match(r'[A-Z][a-z]', w))
        if cap_words >= 2 and len(cand) < 120:
            title = cand
            break
    if title:
        title = re.sub(r"\s+", " ", title).strip()
        project_titles.append(title)

# deduplicate titles preserving order
seen = set()
unique_titles = []
for t in project_titles:
    key = t.lower()
    if key not in seen:
        seen.add(key)
        unique_titles.append(t)

# manual additional detection: also detect lines like 'Begin Construction: Spring/Summer 2022' preceded by project names earlier with pattern 'Project Name\n\n(cid' etc.
# (skip due to complexity)

# match to funding by token overlap >=2
matches = []
total = 0
for t in unique_titles:
    t_clean = clean_text(t)
    t_tokens = set(tokens(t_clean))
    matched_amt = 0
    matched_records = []
    for fname, famt in fund_list:
        f_clean = clean_text(fname)
        f_tokens = set(tokens(f_clean))
        if not t_tokens or not f_tokens:
            continue
        # direct substring
        if t_clean.lower() in f_clean.lower() or f_clean.lower() in t_clean.lower():
            matched_amt += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
            continue
        # token overlap
        if len(t_tokens & f_tokens) >= 2:
            matched_amt += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
    matches.append({'project_title': t, 'matched_funding': matched_amt, 'matched_records': matched_records})
    total += matched_amt

result = {'project_count': len(unique_titles), 'total_funding': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}}

exec(code, env_args)
