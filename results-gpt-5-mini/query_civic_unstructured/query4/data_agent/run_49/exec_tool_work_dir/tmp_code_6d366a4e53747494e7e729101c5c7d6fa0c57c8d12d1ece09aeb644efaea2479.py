code = """import json, re

# Load context extraction and funding data
with open(var_call_8wjCUMazQ6eS7jJ3VwZHy3IP, 'r', encoding='utf-8') as f:
    contexts = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# helper cleaners
def clean(s):
    if s is None:
        return ''
    s = re.sub(r"\(cid:\d+\)", "", s)
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def clean_key(s):
    return clean(s).lower()

def parse_amount(a):
    try:
        return int(str(a).replace(',','').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0

# build funding map by cleaned name
fund_map = {}
fund_records = []
for rec in funding:
    name = rec.get('Project_Name','')
    amt = parse_amount(rec.get('Amount',0))
    key = clean_key(name)
    fund_map.setdefault(key, 0)
    fund_map[key] += amt
    fund_records.append({'orig': name, 'clean': key, 'amount': amt})

# keywords heuristics for project lines
keyword_regex = re.compile(r'\b(Project|Park|Road|PCH|Median|Skate|Shade|Playground|Retaining|Civic|Center|Water|Storm|Drain|Resurfacing|Improvements|Repairs|Way|Facility|Culvert|Bridge|Walkway|Sirens|Warning|Planting|Irrigation|Slope|Stabilization|Broad Beach|Latigo|Encinal|Trancas|Marie Canyon|Bluffs|Permanent Skate)\b', re.I)

candidates = []
for rec in contexts:
    for side in ('next_lines','prev_lines'):
        for line in rec.get(side, []):
            s = line.strip()
            if not s:
                continue
            if s.lower().startswith('(cid'):
                continue
            if len(s) < 4:
                continue
            # require keyword or Title Case
            if keyword_regex.search(s) or re.search(r'[A-Z][a-z]+\s+[A-Z][a-z]+', s):
                candidates.append(s)

# deduplicate preserving order
seen=set(); unique=[]
for c in candidates:
    k=' '.join(c.split())
    kl=k.lower()
    if kl not in seen:
        seen.add(kl); unique.append(k)

# Now match candidates to funding records
matched_funding_indices = set()
project_matches = []
for title in unique:
    tclean = clean_key(title)
    matched = []
    # exact match
    if tclean in fund_map:
        amt = fund_map[tclean]
        # collect records with this clean
        for i, fr in enumerate(fund_records):
            if fr['clean'] == tclean:
                matched.append({'name': fr['orig'], 'amount': fr['amount'], 'index': i})
    else:
        # substring or token overlap
        ttoks = set(tclean.split())
        for i, fr in enumerate(fund_records):
            fclean = fr['clean']
            if not fclean:
                continue
            if tclean in fclean or fclean in tclean:
                matched.append({'name': fr['orig'], 'amount': fr['amount'], 'index': i})
            else:
                ftoks = set(fclean.split())
                if len(ttoks & ftoks) >= 2:
                    matched.append({'name': fr['orig'], 'amount': fr['amount'], 'index': i})
    # record matched indices
    for m in matched:
        matched_funding_indices.add(m['index'])
    total_matched = sum(m['amount'] for m in matched)
    project_matches.append({'project_title': title, 'matched_funding': total_matched, 'matched_records': [{'name': m['name'], 'amount': m['amount']} for m in matched]})

total_funding = sum(fund_records[i]['amount'] for i in matched_funding_indices)

output = {'spring_2022_project_count': len(unique), 'total_funding': total_funding, 'projects': project_matches}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_S8IREuYmLCNjVrY7EghsnWgz': {'project_count': 42, 'total_funding': 0, 'projects': [{'project_title': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Award Contract and', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: April 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: December 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: March 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Awaiting approved maintenance agreement', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: late Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Need approved maintenance agreement to', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Project Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021 (Out to bid now)', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Estimated Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: August 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids were received on June 10th. Staff is currently reviewing the bids', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: September 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids Received: September 7, 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: Summer 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_TB1AvEW6E5jkLFSJi4Ro5jgP': {'project_count': 0, 'total_funding': 0, 'projects': []}, 'var_call_DtVcIuMLxAlBC4FkRGa5Zt9I': {'project_count': 14, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_8wjCUMazQ6eS7jJ3VwZHy3IP': 'file_storage/call_8wjCUMazQ6eS7jJ3VwZHy3IP.json', 'var_call_rRtZD3glH5SfOiG3OZLkVRsp': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise: Spring 2022', 'Agenda Item # 4.A.', '(cid:131) Complete Design: Fall 2022', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Complete Design: Winter 2022', '(cid:131) Advertise: Winter 2022', '(cid:131) Complete Design: Spring 2023', '(cid:131) Complete Design: January 2022'], 'var_call_RILmMGGIxOmBeP77wXgYMPwT': {'spring_2022_project_count': 0, 'total_funding': 0, 'projects': []}}

exec(code, env_args)
