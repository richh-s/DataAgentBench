code = """import json, re

# Load funding project names > 50k
raw_f = var_call_eVADGvohvJvsx0jSLElayY4V
if isinstance(raw_f, str) and raw_f.endswith('.json'):
    with open(raw_f, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = raw_f
funding_names = set(r['Project_Name'] for r in funding if r.get('Project_Name'))

# Load mongo docs
raw = var_call_kZN5vnZ1R2hyRTBYRZjd2yDZ
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

start_pat = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
stop_pat = re.compile(r"Capital Improvement Projects\s*\((Construction|Not Started)\)|Disaster Recovery Projects\s*\(", re.IGNORECASE)

projects_design = set()

for d in docs:
    text = d.get('text') or ''
    for m in start_pat.finditer(text):
        sub = text[m.end():]
        sm = stop_pat.search(sub)
        if sm:
            sub = sub[:sm.start()]
        for line in sub.splitlines():
            ln = line.strip()
            if not ln:
                continue
            if ln.startswith('(cid:'):
                continue
            if re.match(r"^(Page\s+\d+|Agenda Item|RECOMMENDED ACTION|DISCUSSION)\b", ln, re.IGNORECASE):
                continue
            if re.match(r"^(Updates|Project Schedule|Estimated Schedule|Project Description)\b", ln, re.IGNORECASE):
                continue
            # exclude lines containing ':' as they are schedule lines
            if ':' in ln:
                continue
            # basic heuristic for titlecase-ish project names
            if len(ln) < 4 or len(ln) > 120:
                continue
            # must contain at least one letter
            if not re.search(r"[A-Za-z]", ln):
                continue
            # exclude sentences with verbs
            if re.search(r"\b(is|are|will|working|submitted|expecting|received|rejected|awaiting|field|cleared|discussed|delayed)\b", ln, re.IGNORECASE):
                continue
            # exclude headers
            if re.search(r"^Capital Improvement Projects\b", ln, re.IGNORECASE):
                continue
            projects_design.add(ln)

# Intersection count
count = sum(1 for p in projects_design if p in funding_names)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_8LTewYVZ6vCazy4Nbo67HRc1': [{'cnt': '276'}], 'var_call_kZN5vnZ1R2hyRTBYRZjd2yDZ': 'file_storage/call_kZN5vnZ1R2hyRTBYRZjd2yDZ.json', 'var_call_9OZmTToKiqurGP8ipT2hKY6p': {'design_projects_extracted_count': 456, 'sample': ['(cid:131)', '(cid:131) 65% design package was submitted to Caltrans in November 2020 and', '(cid:131) 65% design package was submitted to Caltrans in November 2020.', '(cid:131) A Los Angeles County Flood Control maintenance agreement is', '(cid:131) A bid opening was held on June 9, 2022 an agreement was approved', '(cid:131) A bid opening was held on June 9, 2022, and the agreement is', '(cid:131) A bid opening was held on June 9, 2022. The construction agreement', '(cid:131) A hydrology report was prepared and will be used to size the pre-', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Advertise for Bidding: Summer 2023', '(cid:131) Advertise: August 2021', '(cid:131) Advertise: Fall 2022', '(cid:131) Advertise: Fall 2023', '(cid:131) Advertise: February 2022', '(cid:131) Advertise: July 2021', '(cid:131) Advertise: November 2021', '(cid:131) Advertise: October 2021', '(cid:131) Advertise: September 2021', '(cid:131) Advertise: Spring 2023', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Advertise: Summer 2022', '(cid:131) Advertise: Summer 2023', '(cid:131) Advertise: TBD', '(cid:131) An agreement for construction management services was approved by', '(cid:131) An assessment engineer has been hired by the City and a new', '(cid:131) At the June 13, 2022 City Council meeting, the Council approved an', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '(cid:131) Award Contract and Begin Construction: Fall 2021', '(cid:131) Award Contract and Begin Construction: Fall 2022']}, 'var_call_eVADGvohvJvsx0jSLElayY4V': 'file_storage/call_eVADGvohvJvsx0jSLElayY4V.json'}

exec(code, env_args)
