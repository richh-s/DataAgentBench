code = """import json, re
# Load the query_db result stored in the file path variable
path = var_call_9wQ7vn4CR1fSbTxXKjr8pRsi
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
seen = set()
for doc in docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'(?i)\b(fema|emergency)\b', ln):
            # look back up to 6 previous non-empty lines for a project heading containing keywords
            pname = None
            status = None
            for j in range(max(0, i-6), i+6):
                if j<0 or j>=len(lines):
                    continue
                # find project name candidates: lines that end with 'Project' or contain 'Repairs' or 'Improvements' or 'Facility' or 'Plan' or 'Park' or 'Project:'
                if re.search(r'Project\b|Repairs\b|Improvements\b|Facility\b|Plan\b|Park\b|Playground\b|Treatment\b|Project:', lines[j], re.I):
                    # exclude generic headings like 'DISCUSSION:'
                    if len(lines[j])>3 and not re.match(r'^[A-Z ]{2,20}:$', lines[j]):
                        pname = lines[j]
                        break
            if not pname:
                # as fallback take the previous non-empty line
                for j in range(i-1, max(0, i-6)-1, -1):
                    if lines[j]:
                        pname = lines[j]
                        break
            # find status clues in next 8 lines
            for k in range(i, min(len(lines), i+12)):
                l = lines[k]
                if re.search(r'construction was completed|Complete Construction|Complete Design|Begin Construction|Begin Construction:|Complete Design:|Complete Design\b|Complete Construction\b|Project is currently under construction|Updates: Project is currently under construction', l, re.I):
                    status = l
                    break
                if re.search(r'Project is in the preliminary design phase|Plans and specifications are being finalized|working with the consultant|working with the design consultant|design plans', l, re.I):
                    status = l
                    break
                if re.search(r'not started|identified|waiting for|waiting for the agreement|rejected all bids due to a budget shortfall', l, re.I):
                    status = l
                    break
            # normalize status
            norm_status = None
            if status:
                s = status.lower()
                if 'completed' in s:
                    norm_status = 'completed'
                elif 'under construction' in s or 'begin construction' in s or 'advertise' in s or 'begin construction' in s:
                    # treat as design if construction pending or underway -> map to design if not completed
                    if 'under construction' in s:
                        norm_status = 'design'
                    else:
                        norm_status = 'not started'
                elif 'design' in s or 'plans' in s or 'working with' in s or 'preliminary design' in s:
                    norm_status = 'design'
                elif 'not started' in s or 'identified' in s or 'waiting for' in s:
                    norm_status = 'not started'
                else:
                    norm_status = 'not started'
            else:
                norm_status = 'not started'

            pname_clean = pname.strip() if pname else None
            key = (pname_clean, norm_status)
            if pname_clean and key not in seen:
                seen.add(key)
                results.append({'Project_Name': pname_clean, 'status_extracted': status, 'status': norm_status, 'filename': doc.get('filename')})

# Deduplicate by Project_Name
out = []
byname = {}
for r in results:
    name = r['Project_Name']
    if name not in byname:
        byname[name] = r
out = list(byname.values())

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9wQ7vn4CR1fSbTxXKjr8pRsi': 'file_storage/call_9wQ7vn4CR1fSbTxXKjr8pRsi.json'}

exec(code, env_args)
