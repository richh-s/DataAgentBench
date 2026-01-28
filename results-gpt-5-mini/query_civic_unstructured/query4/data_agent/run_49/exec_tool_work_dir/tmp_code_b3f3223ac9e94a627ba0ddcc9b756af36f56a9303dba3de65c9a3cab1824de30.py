code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# prepare funding list
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0
fund_list = [(rec.get('Project_Name','').strip(), parse_amount(rec.get('Amount',0))) for rec in funding]

# helper cleaners
def clean(s):
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^0-9A-Za-z\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

def tokens(s):
    return set([t for t in re.findall(r"[A-Za-z]{3,}", s.lower())])

# title detection regex
title_regex = re.compile(r"\b(Project|Park|Road|PCH|Median|Skate|Shade|Playground|Retaining Wall|Civic Center|Water Treatment|Stormwater|Drain|Resurfacing|Improvements|Repairs|Way|Center|Facility|Culvert|Bridge|Walkway|Playground)\b", re.I)

candidates = []
for doc in civic_docs:
    lines = doc.get('text','').splitlines()
    for i, line in enumerate(lines):
        line_str = line.strip()
        if not line_str:
            continue
        if title_regex.search(line_str):
            # lookahead block
            block = '\n'.join(lines[i:i+12])
            if re.search(r'begin construction', block, re.I) and re.search(r'spring', block, re.I) and re.search(r'2022', block, re.I):
                candidates.append(line_str)
            else:
                # sometimes title is after the schedule lines; check previous 6 lines too
                prev_block = '\n'.join(lines[max(0,i-6):i+6])
                if re.search(r'begin construction', prev_block, re.I) and re.search(r'spring', prev_block, re.I) and re.search(r'2022', prev_block, re.I):
                    candidates.append(line_str)

# deduplicate preserving order
seen=set(); unique=[]
for c in candidates:
    k=' '.join(c.split())
    kl=k.lower()
    if kl not in seen:
        seen.add(kl); unique.append(k)

# match funding by cleaned substring or token overlap >=2
matches=[]; total=0
for title in unique:
    tclean=clean(title)
    ttoks=tokens(tclean)
    matched_amt=0
    matched_recs=[]
    for fname, famt in fund_list:
        fclean=clean(fname)
        ftoks=tokens(fclean)
        if not fclean:
            continue
        if tclean and (tclean in fclean or fclean in tclean):
            matched_amt += famt
            matched_recs.append({'fund_name': fname, 'amount': famt})
            continue
        if len(ttoks & ftoks) >= 2:
            matched_amt += famt
            matched_recs.append({'fund_name': fname, 'amount': famt})
    matches.append({'project': title, 'matched_funding': matched_amt, 'matched_records': matched_recs})
    total += matched_amt

result={'project_count': len(unique), 'total_funding': total, 'projects': matches}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_oP8kOxEcb4mMZvwC3n7icGtt': {'project_count': 13, 'total_funding': 0, 'projects': [{'project': '(cid:131) Complete Design: March 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring/Summer 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: February 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021', 'funding': 0}, {'project': '(cid:131) Advertise for Bidding: December 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Spring 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Fall 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2021/2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Winter 2022', 'funding': 0}, {'project': '(cid:131) Advertise: Winter 2022', 'funding': 0}, {'project': '(cid:131) Complete Design: Spring 2023', 'funding': 0}, {'project': '(cid:131) Complete Design: January 2022', 'funding': 0}]}, 'var_call_ShyXxXrZaHYgx7z2HcwaxXmf': {'project_count': 13, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_S8IREuYmLCNjVrY7EghsnWgz': {'project_count': 42, 'total_funding': 0, 'projects': [{'project_title': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Award Contract and', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: April 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: February 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: December 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: March 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Awaiting approved maintenance agreement', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: July 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: late Summer 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed. Need approved maintenance agreement to', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Project Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2021 (Out to bid now)', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: May 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:190) Estimated Schedule:', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: August 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids were received on June 10th. Staff is currently reviewing the bids', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: September 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Bids Received: September 7, 2021', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Final Design: Completed.', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise for Bidding: Summer 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_title': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_TB1AvEW6E5jkLFSJi4Ro5jgP': {'project_count': 0, 'total_funding': 0, 'projects': []}, 'var_call_DtVcIuMLxAlBC4FkRGa5Zt9I': {'project_count': 14, 'total_funding': 0, 'projects': [{'project_name': '(cid:131) Complete Design: March 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring/Summer 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: February 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise for Bidding: December 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Spring 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Agenda Item # 4.A.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Fall 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2021/2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Advertise: Winter 2022', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: Spring 2023', 'matched_funding': 0, 'matched_records': []}, {'project_name': '(cid:131) Complete Design: January 2022', 'matched_funding': 0, 'matched_records': []}]}, 'var_call_8wjCUMazQ6eS7jJ3VwZHy3IP': 'file_storage/call_8wjCUMazQ6eS7jJ3VwZHy3IP.json', 'var_call_rRtZD3glH5SfOiG3OZLkVRsp': ['(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise: Spring 2022', 'Agenda Item # 4.A.', '(cid:131) Complete Design: Fall 2022', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Complete Design: Winter 2022', '(cid:131) Advertise: Winter 2022', '(cid:131) Complete Design: Spring 2023', '(cid:131) Complete Design: January 2022']}

exec(code, env_args)
