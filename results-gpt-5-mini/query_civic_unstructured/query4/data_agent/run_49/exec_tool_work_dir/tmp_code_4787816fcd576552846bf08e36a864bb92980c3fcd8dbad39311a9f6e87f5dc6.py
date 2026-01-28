code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# parse amounts
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0

# build funding map list
fund_list = [(rec.get('Project_Name','').strip(), parse_amount(rec.get('Amount',0))) for rec in funding]

# helper to clean names
def clean_name(s):
    s = re.sub(r"\(.*?\)", "", s)  # remove parentheticals
    s = re.sub(r"[^0-9a-zA-Z\s]"," ", s)
    s = re.sub(r"\s+"," ", s)
    return s.strip().lower()

# find projects that begin construction in spring 2022 (or spring generally in 2022)
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'begin construction', line, re.I) and re.search(r'spring', line, re.I):
            # search upwards for a project title containing key words
            title = None
            for j in range(max(0,i-12), i)[::-1]:
                cand = lines[j].strip()
                if not cand:
                    continue
                # prefer lines with key words
                if re.search(r'\b(Project|Park|Road|PCH|Improvements|Facility|Skate|Shade|Playground|Median|Resurfacing|Repair|Repairs|Culvert|Retaining Wall|Storm|Water|Center|Way|Drain)\b', cand, re.I):
                    # skip generic header words
                    if len(cand) < 6:
                        continue
                    title = cand
                    break
            if not title:
                # fallback: take first non-empty previous line
                for j in range(max(0,i-6), i)[::-1]:
                    cand = lines[j].strip()
                    if cand and len(cand) > 4 and not cand.endswith('.'):
                        title = cand
                        break
            if title:
                # clean multiple spaces
                title = re.sub(r"\s+"," ", title).strip()
                projects.append(title)

# deduplicate, normalize
unique = []
seen = set()
for p in projects:
    kp = p.lower()
    if kp not in seen:
        seen.add(kp)
        unique.append(p)

# match funding by cleaned substring matching
project_matches = []
total = 0
for p in unique:
    p_clean = clean_name(p)
    amt = 0
    matched_records = []
    for fname, famt in fund_list:
        fclean = clean_name(fname)
        if not fclean:
            continue
        # match if cleaned project name is substring of funding name or vice versa
        if p_clean and (p_clean in fclean or fclean in p_clean):
            amt += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
        else:
            # also match by token overlap: require at least 2 shared tokens
            p_tokens = set([t for t in p_clean.split() if len(t)>2])
            f_tokens = set([t for t in fclean.split() if len(t)>2])
            if len(p_tokens & f_tokens) >= 2:
                amt += famt
                matched_records.append({'fund_name': fname, 'amount': famt})
    project_matches.append({'project_name': p, 'matched_funding': amt, 'matched_records': matched_records})
    total += amt

result = {'project_count': len(unique), 'total_funding': total, 'projects': project_matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}}

exec(code, env_args)
