code = """import json, re

docs = var_call_P7HqHpGj32kLZOFohlVR3oSo
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

projects = set()
for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    low = text.lower()
    if not any(k in low for k in ['park', 'playground', 'bluffs']):
        continue
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if not re.search(r"construction was completed", ln, re.I):
            continue
        # check 2022 in same or next 2 lines
        neighborhood = " ".join([lines[i+k] for k in range(0,3) if i+k < len(lines)])
        if '2022' not in neighborhood:
            continue
        # backtrack for project name: nearest prior non-empty line without (cid
        for j in range(i-1, max(-1, i-30), -1):
            cand = lines[j].strip()
            if not cand:
                continue
            if cand.startswith('(cid') or cand.startswith('Page') or cand.startswith('Agenda'):
                continue
            if ':' in cand:
                continue
            if len(cand) > 120:
                continue
            if re.search(r"\bpark\b|playground|bluffs", cand, re.I):
                projects.add(cand)
                break

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'count': len(projects)}))"""

env_args = {'var_call_NIvwffJWG7drgKEX0ouuonTU': ['Funding'], 'var_call_70lRMmxwkBojNg4RiHXBaK0L': ['civic_docs'], 'var_call_P7HqHpGj32kLZOFohlVR3oSo': 'file_storage/call_P7HqHpGj32kLZOFohlVR3oSo.json', 'var_call_DvFCvwPxOzQtBKBdG9HiZTyv': {'projects_completed_2022_park_related': [], 'count': 0}, 'var_call_RSTg9AxLTI6rwEUks3N6ebvO': {'docs_with_completed_2022_and_park': 19, 'sample_contexts': []}, 'var_call_v1VDr1Wa3VLr3ahpXokkKnYQ': {'docs': 19, 'samples': [{'filename': 'malibucity_agenda_03222023-2060.txt', 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'context': ['', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023', '', 'Page 4 of 6', '', 'Agenda Item # 4.B.']}, {'filename': 'malibucity_agenda__01262022-1835.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning', 'context': ['(cid:190) Updates:', '(cid:131)', '', 'In May 2021, the Council approved funding for additional engineering', 'work related to the project. Staff has worked with the consultant over', 'the past several months to complete the engineering work, and the final', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', 'review by the Council.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022']}, {'filename': 'malibucity_agenda__01272021-1626.txt', 'line': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'context': ['(cid:131) A Los Angeles County Flood Control maintenance agreement is', 'required for this project. Staff is waiting for the County’s approval of', 'the agreement.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', '', 'the County.', '', '(cid:131) Begin Construction: Estimated Summer 2021', '', 'Westward Beach Road Improvements Project']}, {'filename': 'malibucity_agenda__03022021-1648.txt', 'line': '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', 'context': ['(cid:131) A Los Angeles County Flood Control maintenance agreement is', 'required for this project. Staff is waiting for the County’s approval of', 'the agreement.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Completed. Awaiting maintenance agreement from', '', 'the County.', '', '(cid:131) Begin Construction: Estimated Summer 2021', '', 'Westward Beach Road Improvements Project']}, {'filename': 'malibucity_agenda__03232022-1869.txt', 'line': 'draft plans are expected to be completed in early 2022. The Planning', 'context': ['(cid:190) Updates:', '(cid:131)', '', 'In May 2021, the Council approved funding for additional engineering', 'work related to the project. Staff has worked with the consultant over', 'the past several months to complete the engineering work, and the final', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', 'review by the Council.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022']}]}}

exec(code, env_args)
