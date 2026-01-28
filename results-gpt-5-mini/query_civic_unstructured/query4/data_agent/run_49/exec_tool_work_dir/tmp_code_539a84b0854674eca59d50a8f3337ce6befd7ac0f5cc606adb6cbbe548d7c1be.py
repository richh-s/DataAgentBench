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

keywords = re.compile(r'\b(Project|Park|Road|PCH|Median|Skate|Shade|Playground|Retaining Wall|Civic Center|Water Treatment|Stormwater|Drain|Resurfacing|Improvements|Repairs|Way|Center|Facility|Culvert|Bridge|Resurfacing|Improvement|Storm|Playground)\b', re.I)

found_projects = []
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i, line in enumerate(lines):
        line_str = line.strip()
        if not line_str:
            continue
        # if line looks like a title and contains keyword
        if keywords.search(line_str):
            # look ahead for Begin Construction within next 12 lines
            lookahead = ' '.join(lines[i:i+12])
            if re.search(r'begin construction', lookahead, re.I) and re.search(r'spring', lookahead, re.I):
                found_projects.append(line_str)
        # also sometimes project title is on previous line and current line contains 'Project Description' header
        if re.search(r'project description', line_str, re.I) and i>0:
            candidate = lines[i-1].strip()
            if candidate and keywords.search(candidate):
                # check lookahead from i for begin construction
                lookahead = ' '.join(lines[i:i+12])
                if re.search(r'begin construction', lookahead, re.I) and re.search(r'spring', lookahead, re.I):
                    found_projects.append(candidate)

# deduplicate preserving order
seen = set(); unique = []
for p in found_projects:
    key = re.sub(r'\s+',' ', p).strip()
    kl = key.lower()
    if kl not in seen:
        seen.add(kl); unique.append(key)

# match funding by cleaned substring or token overlap >=2

def clean(s):
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

def tokens(s):
    return set([t for t in re.findall(r"[A-Za-z]{3,}", s)])

project_matches = []
total = 0
for p in unique:
    pclean = clean(p)
    ptoks = tokens(pclean)
    matched_amt = 0
    matched_records = []
    for fname, famt in fund_list:
        fclean = clean(fname)
        ftoks = tokens(fclean)
        if not fclean:
            continue
        if pclean and (pclean in fclean or fclean in pclean):
            matched_amt += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
            continue
        if len(ptoks & ftoks) >= 2:
            matched_amt += famt
            matched_records.append({'fund_name': fname, 'amount': famt})
    project_matches.append({'project_name': p, 'matched_funding': matched_amt, 'matched_records': matched_records})
    total += matched_amt

result = {'project_count': len(unique), 'total_funding': total, 'projects': project_matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_S8IREuYmLCNjVrY7EghsnWgz': {'project_count': 42, 'total_funding': 0, 'projects': [{'project_title': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Award Contract and', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: April 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: December 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: March 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Awaiting approved maintenance agreement', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: late Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Need approved maintenance agreement to', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Project Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021 (Out to bid now)', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Estimated Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: August 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids were received on June 10th. Staff is currently reviewing the bids', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: September 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids Received: September 7, 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: Summer 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}}

exec(code, env_args)
