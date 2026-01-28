code = """import json, re

# load civic docs
civic = var_call_dg5JVhfch06pxm1wQfiyAf8c
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

# load funding names >50k
fund = var_call_6HF3oFNFRkfp4Hk7ogXyDhPA
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)
fund_names = set(r['Project_Name'] for r in fund)

section_re = re.compile(r'Capital Improvement Projects \(Design\)', re.IGNORECASE)
end_re = re.compile(r'Capital Improvement Projects \((?:Construction|Not Started)\)|Disaster Recovery Projects', re.IGNORECASE)

skip_re = re.compile(r'^(\(cid:|Page \d+|Agenda Item|\s*$)', re.IGNORECASE)
meta_re = re.compile(r'^(Updates:|Project Schedule:|Estimated Schedule:|Project Description:|Project Updates:)', re.IGNORECASE)

cand=set()
for doc in civic:
    text=doc.get('text','') or ''
    m=section_re.search(text)
    if not m:
        continue
    sub=text[m.end():]
    m2=end_re.search(sub)
    if m2:
        sub=sub[:m2.start()]
    for ln in sub.splitlines():
        ln=ln.strip()
        if not ln or skip_re.search(ln) or meta_re.search(ln):
            continue
        if ':' in ln:
            continue
        if len(ln.split())>12:
            continue
        if not re.search(r'[A-Za-z]', ln):
            continue
        cand.add(ln)

matched=sorted([p for p in cand if p in fund_names])

print('__RESULT__:')
print(json.dumps({'design_projects_found': len(cand), 'design_projects_with_funding_gt_50k': len(matched), 'matched_projects': matched}))"""

env_args = {'var_call_8YSPtlxKUqAdVgtYrYZYfHTz': [{'cnt': '276'}], 'var_call_dg5JVhfch06pxm1wQfiyAf8c': 'file_storage/call_dg5JVhfch06pxm1wQfiyAf8c.json', 'var_call_ogMj4TmRt3AwmHHdNOMCPFls': ['Funding'], 'var_call_6HF3oFNFRkfp4Hk7ogXyDhPA': 'file_storage/call_6HF3oFNFRkfp4Hk7ogXyDhPA.json', 'var_call_bEOBsEXekaG6C5xSepof4VCl': {'count': 0, 'projects': []}, 'var_call_3uR50DXJHVsaFxUXxvjrG6L2': {'error': 'no design section found'}, 'var_call_W7cColvqRHw80B0TmzgYyERS': {'matches': 5, 'filenames': ['malibucity_agenda_03222023-2060.txt', 'malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt']}, 'var_call_83WJzBtiV7lXpv2rQlp78i1F': {'n_lines': 114, 'first_50': ['2022 Morning View Resurfacing & Storm Drain Improvements', '(cid:190) Updates:', '(cid:131) Staff is working with the consultant to finalize the design plans for this', 'project and will submit to the County for review.', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', '(cid:131) Begin Construction: Fall 2023', 'PCH Median Improvements Project', '(cid:190) Updates:', '(cid:131) On September 22, 2022, the City received four (4) construction bids', 'and rejected all bids due to a budget shortfall', '(cid:131) City will work with the design consultant to review design alternatives', 'or phasing out the project', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', 'Page 1 of 6', 'Agenda Item # 4.B.', '(cid:131) Begin Construction: Fall 2023', 'Westward Beach Road Repair Project', '(cid:190) Updates:', '(cid:131) City working with consultant on the design of the shoulder repairs', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Summer 2023', '(cid:131) Begin Construction: Fall 2023', 'Westward Beach Road Drainage Improvements Project', '(cid:190) Updates:', '(cid:131) Plans are under review by Fish and Wildlife and City is expecting', 'comments mid-April. This project required their review since the project', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'cleared the project.', '(cid:190) Project Schedule:', '(cid:131) Advertise: Summer 2023', '(cid:131) Begin Construction: Fall 2023', 'Clover Heights Storm Drainage Improvements', '(cid:190) Updates:', '(cid:131) City submitted plans to CalOES for review and working with consultant', 'to finalize plans and specifications', '(cid:190) Project Schedule:', '(cid:131) Final Design: Summer, 2023', '(cid:131) Advertise: Summer 2023', '(cid:131) Begin Construction: Fall 2023', 'Latigo Canyon Road Retaining Wall Repair Project', '(cid:190) Updates:', '(cid:131) Plans and specifications have been completed', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '(cid:190) Project Schedule:', '(cid:131) Advertise: Spring 2023']}}

exec(code, env_args)
