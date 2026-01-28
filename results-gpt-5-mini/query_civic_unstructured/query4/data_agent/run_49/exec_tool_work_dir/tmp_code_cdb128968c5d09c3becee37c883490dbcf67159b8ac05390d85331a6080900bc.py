code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding into dict of cleaned name -> amount (sum duplicates)
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0

def clean_name(s):
    if s is None:
        return ''
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

fund_map = {}
fund_records = {}
for rec in funding:
    name = rec.get('Project_Name','')
    amt = parse_amount(rec.get('Amount',0))
    k = clean_name(name)
    fund_map[k] = fund_map.get(k, 0) + amt
    fund_records.setdefault(k, []).append({'orig_name': name, 'amount': amt})

# find occurrences of 'begin construction' near 'spring' in civic docs
proj_candidates = []
for doc in civic_docs:
    text = doc.get('text','')
    # normalize line endings
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'begin construction', line, re.I) and re.search(r'spring', line, re.I):
            # search upward up to 25 lines for candidate title
            title = None
            for j in range(i-1, max(-1, i-26), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                low = cand.lower()
                # skip header-ish lines
                if re.search(r'\b(updates|project schedule|project description|agenda report|agenda item|page|item|to:|prepared by|approved by|date prepared|meeting date|subject|discussion|recommended action|estimated schedule|complete design|advertise|begin design)\b', cand, re.I):
                    continue
                # prefer lines containing 'Project' or capitalized words or known keywords
                if re.search(r'\bproject\b', cand, re.I) or re.search(r'\b(pch|park|road|median|skate|shade|playground|retaining wall|civic center|water treatment|stormwater|storm drain|drainage|resurfacing|improvements|repairs|culvert|retaining|bridge|way)\b', cand, re.I):
                    title = cand
                    break
                # title-case heuristic
                words = re.findall(r"[A-Za-z]+", cand)
                cap = sum(1 for w in words if re.match(r'[A-Z][a-z]', w))
                if cap >= 2 and len(cand) < 120:
                    title = cand
                    break
            if title:
                proj_candidates.append(title)

# deduplicate preserving order
seen = set(); unique_projects = []
for p in proj_candidates:
    k = re.sub(r'\s+',' ', p).strip()
    kl = k.lower()
    if kl not in seen:
        seen.add(kl); unique_projects.append(k)

# Now match each unique project to funding entries
matches = []
total_funding = 0
for p in unique_projects:
    p_clean = clean_name(p)
    matched_amt = 0
    matched_details = []
    # exact key match
    if p_clean in fund_map:
        matched_amt += fund_map[p_clean]
        matched_details.extend(fund_records.get(p_clean, []))
    else:
        # try substring matches
        for fk, famt in fund_map.items():
            if p_clean and (p_clean in fk or fk in p_clean):
                matched_amt += famt
                matched_details.extend(fund_records.get(fk, []))
        # token overlap fallback
        if matched_amt == 0:
            p_tokens = set(p_clean.split())
            for fk, famt in fund_map.items():
                fk_tokens = set(fk.split())
                if len(p_tokens & fk_tokens) >= 2:
                    matched_amt += famt
                    matched_details.extend(fund_records.get(fk, []))
    total_funding += matched_amt
    matches.append({'project_name': p, 'matched_funding': matched_amt, 'matched_records': matched_details})

result = {'project_count': len(unique_projects), 'total_funding': total_funding, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_S8IREuYmLCNjVrY7EghsnWgz': {'project_count': 42, 'total_funding': 0, 'projects': [{'project_title': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Award Contract and', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: April 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: December 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: March 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Awaiting approved maintenance agreement', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: late Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Need approved maintenance agreement to', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Project Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021 (Out to bid now)', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Estimated Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: August 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids were received on June 10th. Staff is currently reviewing the bids', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: September 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids Received: September 7, 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: Summer 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_TB1AvEW6E5jkLFSJi4Ro5jgP': {'project_count': 0, 'total_funding': 0, 'projects': []}}

exec(code, env_args)
