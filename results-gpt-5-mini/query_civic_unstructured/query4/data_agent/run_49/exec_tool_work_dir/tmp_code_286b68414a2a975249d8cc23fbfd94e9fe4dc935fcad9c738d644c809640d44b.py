code = """import json, re

with open(var_call_mE21EkZMD6kWWBeEVNBTfcmh, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_9dDVhlsKhiCUoWoIszsMD5pk, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# build funding dict
def parse_amount(a):
    try:
        return int(str(a).replace(',', '').strip())
    except:
        try:
            return int(float(a))
        except:
            return 0
fund_index = {}
for rec in funding:
    name = rec.get('Project_Name','').strip()
    key = name.lower()
    amt = parse_amount(rec.get('Amount',0))
    fund_index[key] = fund_index.get(key, 0) + amt

# find lines indicating begin construction in spring
spring_patterns = [r'begin construction[:\s].*spring', r'begin construction[:\s].*spring/summer', r'begin construction[:\s].*spring\/?summer', r'begin construction[:\s].*spring 2022', r'begin construction[:\s].*spring\s*2022']
proj_names = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(re.search(pat, low) for pat in spring_patterns):
            # search upward up to 12 lines for title-like line
            title = None
            for j in range(max(0,i-12), i)[::-1]:
                cand = lines[j].strip()
                if not cand:
                    continue
                # skip sentences (end with period) or lines with many lowercase words
                if cand.endswith('.'):
                    continue
                # skip lines that are section headers or contain digits like dates
                if re.search(r'\b(updates|project schedule|project description|agenda|page|item|approved|date prepared|meeting date|subject|discussion|complete design|estimate|begin design)\b', cand, re.I):
                    continue
                # heuristics for title-like: has at least two words starting with capital letter or contains word 'Project' or 'Park' etc
                words = cand.split()
                cap_count = sum(1 for w in words if re.match(r'[A-Z][a-z]', w))
                keywords = ['Project','Park','Road','PCH','Civic','Center','Improvements','Facility','Skate','Shade','Playground','Median','Trancas','Latigo','Broad Beach','Storm','Walkway']
                if cap_count >= 2 or any(k.lower() in cand.lower() for k in keywords):
                    title = cand
                    break
            if title:
                # clean title
                title_clean = re.sub(r'\s+', ' ', title).strip()
                proj_names.append(title_clean)

# deduplicate
seen = set()
unique = []
for p in proj_names:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        unique.append(p)

# match funding
project_funding = []
total = 0
for p in unique:
    p_low = p.lower()
    amt = 0
    # exact
    if p_low in fund_index:
        amt = fund_index[p_low]
    else:
        # try contains either way
        for fname, famt in fund_index.items():
            if p_low in fname or fname in p_low:
                amt += famt
    project_funding.append({'project': p, 'funding': amt})
    total += amt

result = {'project_count': len(unique), 'total_funding': total, 'projects': project_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_BdeM6JKXvXUPFcVEkoVfqh0j': ['civic_docs'], 'var_call_wQRCfEJDSwaLWyNdD3LMZpRO': ['Funding'], 'var_call_mE21EkZMD6kWWBeEVNBTfcmh': 'file_storage/call_mE21EkZMD6kWWBeEVNBTfcmh.json', 'var_call_9dDVhlsKhiCUoWoIszsMD5pk': 'file_storage/call_9dDVhlsKhiCUoWoIszsMD5pk.json', 'var_call_vr1SSVHcC9KdqdCKjVCsDvBQ': {'project_count': 19, 'total_funding': 0, 'projects': [{'project_name': 'advertised for construction bids shortly after this date.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'agreement will be sent to City Council in March.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'project will begin in conjunction with the PCH Median Improvement', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'sending this project out to bid during the Spring of 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is finalizing the bid documents.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'that was damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'property owners.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'scheduled for the April 11, 2022 Council meeting.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'timber with non-combustible materials.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2022.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'beginning in Spring 2023.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'update regarding the proposed time extension to the MOU deadlines.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'shade structures at Malibu Bluffs Park.', 'matched_funding': 0, 'matched_records': []}, {'project_name': '2022-2023 budget.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'guardrails within the project limits.', 'matched_funding': 0, 'matched_records': []}, {'project_name': 'is working on the project plans to prepare for public bidding.', 'matched_funding': 0, 'matched_records': []}]}}

exec(code, env_args)
