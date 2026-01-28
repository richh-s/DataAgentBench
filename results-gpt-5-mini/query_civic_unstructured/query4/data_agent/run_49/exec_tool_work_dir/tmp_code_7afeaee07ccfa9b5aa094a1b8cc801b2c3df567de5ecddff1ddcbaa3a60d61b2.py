code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0

fund_list = [(rec.get('Project_Name','').strip(), parse_amount(rec.get('Amount',0))) for rec in funding]

def clean_text(s):
    if s is None:
        return ''
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

def tokens(s):
    return [t for t in re.findall(r"[A-Za-z]{3,}", s.lower())]

extracted = []
for doc in civic_docs:
    text = doc.get('text','')
    for m in re.finditer(r'begin construction', text, re.I):
        pos = m.start()
        before_text = text[:pos]
        lines = before_text.splitlines()
        title = None
        for j in range(len(lines)-1, max(-1, len(lines)-21), -1):
            cand = lines[j].strip()
            if not cand:
                continue
            # skip obvious non-title lines
            if re.search(r'\b(updates|project schedule|project description|agenda report|agenda item|page|item|to:|prepared by|approved by|date prepared|meeting date|subject|discussion|recommended action|complete design|advertise|begin design)\b', cand, re.I):
                continue
            if len(cand) > 200:
                continue
            # accept if contains key words or Title Case
            if re.search(r'\b(Project|Park|Road|PCH|Median|Skate|Shade|Playground|Retaining Wall|Civic Center|Water Treatment|Stormwater|Drain|Resurfacing|Improvements|Repairs|Way|Center|Facility)\b', cand, re.I):
                title = cand
                break
            words = cand.split()
            cap_count = sum(1 for w in words if re.match(r'[A-Z][a-z]', w))
            if cap_count >= 2 and len(cand) < 120:
                title = cand
                break
        if title:
            t = re.sub(r"\s+", " ", title).strip()
            extracted.append(t)

# deduplicate preserving order
seen = set()
unique = []
for t in extracted:
    key = t.lower()
    if key not in seen:
        seen.add(key)
        unique.append(t)

# match funding
project_matches = []
total = 0
for title in unique:
    title_clean = clean_text(title)
    title_tokens = set(tokens(title_clean))
    matched_amount = 0
    matched_records = []
    for fname, famt in fund_list:
        fclean = clean_text(fname)
        f_tokens = set(tokens(fclean))
        if not fclean:
            continue
        if title_clean and (title_clean in fclean or fclean in title_clean):
            matched_amount += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
            continue
        if len(title_tokens & f_tokens) >= 2:
            matched_amount += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
    project_matches.append({'project_title': title, 'matched_funding': matched_amount, 'matched_records': matched_records})
    total += matched_amount

result = {'project_count': len(unique), 'total_funding': total, 'projects': project_matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}}

exec(code, env_args)
